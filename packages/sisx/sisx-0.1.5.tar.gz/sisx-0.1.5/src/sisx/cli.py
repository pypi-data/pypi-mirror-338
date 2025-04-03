from __future__ import annotations

import shutil
import subprocess
from importlib.metadata import PackageNotFoundError
from pathlib import Path
from typing import Annotated, Any

import typer
import yaml

from .utils.secrets import create_secrets_file
from .utils.snowcli import (
    deploy_streamlit,
    drop_spcs_services,
    drop_streamlit,
    init_app,
    list_streamlit_apps,
)
from .utils.templates import (
    get_template_dir,
    get_template_variables,
)
from .utils.toml_config import (
    get_connection_by_name,
    get_default_connection,
)
from .utils.yaml_config import _read_snowflake_config

app = typer.Typer(help="sisx CLI tool for Streamlit in Snowflake applications")

# Type aliases for better readability
ComputeConfig = dict[str, Any]


def _version_callback(value: bool) -> None:
    """Print the version of sisx and exit."""
    if value:
        from importlib.metadata import version

        try:
            v = version("sisx")
            typer.echo(f"sisx version: {v}")
        except PackageNotFoundError:
            typer.echo("sisx version: unknown")
        raise typer.Exit()


@app.callback()
def main_callback(
    version: bool = typer.Option(
        False,
        "--version",
        help="Show the version and exit.",
        callback=_version_callback,
    ),
) -> None:
    """
    sisx CLI tool for Streamlit in Snowflake applications.
    """


@app.command()
def deploy(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
    replace: bool = typer.Option(
        False, "--replace", "-r", help="Replace the Streamlit app if it already exists"
    ),
    open_browser: Annotated[
        bool,
        typer.Option(
            "--no-open", help="Don't open the deployed Streamlit app in a browser"
        ),
    ] = False,
    connection: str | None = typer.Option(
        None, "--connection", "-c", help="Connection to use for deployment"
    ),
    query_warehouse: str | None = typer.Option(
        None, "--query-warehouse", help="Override the query warehouse to use"
    ),
    app_warehouse: str | None = typer.Option(
        None, "--app-warehouse", help="Override the app warehouse to use"
    ),
    debug: bool = typer.Option(False, "--debug", help="Enable debug output"),
) -> None:
    """
    Deploy a Streamlit application using the Snowflake CLI.

    This command wraps the `snow streamlit deploy` command, providing a convenient
    interface for deploying Streamlit applications to Snowflake.

    By default, opens the app in your browser. Use --no-open to disable.
    """
    config = _read_snowflake_config()

    if verbose:
        typer.echo(config)

    # Get configuration from env section
    env = config.get("env", {})
    name = env.get("name")
    database = env.get("database")
    schema = env.get("schema")
    role = env.get("role")

    if not all([name, database, schema, role]):
        typer.echo("Missing required configuration in snowflake.yml")
        raise typer.Exit(code=1)

    try:
        deploy_streamlit(
            name=name,
            database=database,
            schema=schema,
            role=role,
            replace=replace,
            open_browser=not open_browser,
            connection=connection,
            query_warehouse=query_warehouse,
            app_warehouse=app_warehouse,
            verbose=verbose,
            debug=debug,
        )
        typer.echo(f"App '{name}' successfully deployed!")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error deploying app: {e}")
        if e.stderr:
            typer.echo(f"Error details: {e.stderr}")
        raise typer.Exit(code=1) from e


@app.command(name="deploy-preview")
def deploy_preview(
    preview_name: str | None = typer.Option(
        None, "--preview-name", help="Name of the preview app"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
    replace: bool = typer.Option(
        False, "--replace", "-r", help="Replace the Streamlit app if it already exists"
    ),
    open_browser: Annotated[
        bool,
        typer.Option(
            "--no-open", help="Don't open the deployed Streamlit app in a browser"
        ),
    ] = False,
    connection: str | None = typer.Option(
        None, "--connection", "-c", help="Connection to use for deployment"
    ),
    debug: bool = typer.Option(False, "--debug", help="Enable debug output"),
) -> None:
    """
    Deploy a preview version of a Streamlit application.

    This command adds 'preview_' to the beginning of the app name and also adds
    'PREVIEW: ' to the app title, making it easy to identify preview deployments.

    By default, opens the app in your browser. Use --no-open to disable.
    """
    config = _read_snowflake_config()

    # Get configuration from env section
    env = config.get("env", {})
    original_name = env.get("name")
    original_title = env.get("title", "Streamlit App")
    preview_database = env.get("preview_database", env.get("database"))
    preview_schema = env.get("preview_schema", env.get("schema"))
    preview_role = env.get("preview_role", env.get("role"))

    if not all([original_name, preview_database, preview_schema, preview_role]):
        typer.echo("Missing required configuration in snowflake.yml")
        raise typer.Exit(code=1)

    if preview_name is None:
        preview_name = f"preview_{original_name}"

    preview_title = f"PREVIEW: {original_title}"

    if verbose:
        typer.echo(f"Creating preview deployment with name: {preview_name}")
        typer.echo(f"Preview title will be: {preview_title}")
        typer.echo(f"Using database: {preview_database}")
        typer.echo(f"Using schema: {preview_schema}")
        typer.echo(f"Using role: {preview_role}")

    try:
        deploy_streamlit(
            name=preview_name,
            database=preview_database,
            schema=preview_schema,
            role=preview_role,
            title=preview_title,
            replace=replace,
            open_browser=not open_browser,
            connection=connection,
            verbose=verbose,
            debug=debug,
        )
        typer.echo(f"App '{preview_name}' successfully deployed!")
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error deploying app: {e}")
        if e.stderr:
            typer.echo(f"Error details: {e.stderr}")
        raise typer.Exit(code=1) from e


def _drop_app(
    app_name: str,
    database: str,
    schema: str,
    connection: str | None = None,
    verbose: bool = False,
    drop_spcs: bool = False,
) -> bool:
    """Helper function to drop a Streamlit app and optionally its SPCS services."""
    # First drop any SPCS services associated with the app if requested
    if drop_spcs:
        _drop_app_spcs_services(app_name, connection, verbose)

    try:
        drop_streamlit(
            app_name=app_name,
            database=database,
            schema=schema,
            connection=connection,
            verbose=verbose,
        )
        full_app_name = f"{database}.{schema}.{app_name}"
        typer.echo(f"Successfully dropped app '{full_app_name}'")
        return True
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error dropping Streamlit app: {e}")
        if e.stderr:
            typer.echo(f"Error details: {e.stderr}")
        return False


def _drop_app_spcs_services(
    app_name: str,
    connection: str | None = None,
    verbose: bool = False,
) -> bool:
    """Helper function to drop SPCS services associated with a Streamlit app."""
    if verbose:
        typer.echo(f"Dropping associated SPCS services for {app_name}")

    try:
        drop_spcs_services(
            app_name=app_name,
            connection=connection,
            verbose=verbose,
        )
        return True
    except Exception as e:
        typer.echo(
            f"Warning: Error dropping SPCS services for {app_name} (this is usually ok): {e}"
        )
        return False


@app.command()
def drop(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
    connection: str | None = typer.Option(
        None, "--connection", "-c", help="Connection to use for deployment"
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force drop without confirmation"
    ),
    drop_spcs: bool = typer.Option(
        False, "--drop-spcs", help="Also drop any associated SPCS services"
    ),
) -> None:
    """
    Drop a Streamlit application from Snowflake.

    This command will remove the Streamlit app. If --drop-spcs is specified,
    it will also clean up any associated SPCS services.
    """
    # Read the app name from the yaml file
    try:
        config = yaml.safe_load(Path("snowflake.yml").read_text())
    except Exception as e:
        typer.echo(f"Error reading app configuration from snowflake.yml: {e}")
        raise typer.Exit(code=1) from e

    # Get the app name from env section
    app_name = config.get("env", {}).get("name")
    database = config.get("streamlit", {}).get("database")
    schema = config.get("streamlit", {}).get("schema")

    if verbose:
        typer.echo(
            f"Found configuration: app={app_name}, db={database}, schema={schema}"
        )

    # Create the fully qualified name
    full_app_name = f"{database}.{schema}.{app_name}"

    if verbose:
        typer.echo(f"Dropping Streamlit app: {full_app_name}")

    # Confirm unless --force is specified
    if not force:
        confirm = typer.confirm(
            f"Are you sure you want to drop the app '{full_app_name}'?"
        )
        if not confirm:
            typer.echo("Operation cancelled.")
            raise typer.Exit()

    # Use the helper function to drop the app
    success = _drop_app(app_name, database, schema, connection, verbose, drop_spcs)
    if not success:
        raise typer.Exit(code=1)


@app.command(name="drop-preview")
def drop_preview(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
    connection: str = typer.Option(
        None, "--connection", "-c", help="Connection to use for deployment"
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force drop without confirmation"
    ),
    drop_spcs: bool = typer.Option(
        False, "--drop-spcs", help="Also drop any associated SPCS services"
    ),
):
    """
    Drop a preview version of a Streamlit application from Snowflake.

    This command will remove the preview Streamlit app (with prefix 'preview_').
    If --drop-spcs is specified, it will also clean up any associated SPCS services.
    """
    try:
        config = yaml.safe_load(Path("snowflake.yml").read_text())
    except (yaml.YAMLError, OSError) as e:
        typer.echo(f"Error reading app configuration from snowflake.yml: {e}")
        raise typer.Exit(code=1) from e

    # Get the app name from env section and add preview prefix
    original_name = config.get("env", {}).get("name")
    preview_name = f"preview_{original_name}"
    database = config.get("streamlit", {}).get("database")
    schema = config.get("streamlit", {}).get("schema")

    if verbose:
        typer.echo(
            f"Found configuration: app={preview_name}, db={database}, schema={schema}"
        )

    if not original_name or not database or not schema:
        typer.echo("Error: Missing required configuration in snowflake.yml")
        raise typer.Exit(code=1)

    # Create the fully qualified name
    full_preview_name = f"{database}.{schema}.{preview_name}"

    if verbose:
        typer.echo(f"Dropping preview Streamlit app: {full_preview_name}")

    # Confirm unless --force is specified
    if not force:
        confirm = typer.confirm(
            f"Are you sure you want to drop the preview app '{full_preview_name}'?"
        )
        if not confirm:
            typer.echo("Operation cancelled.")
            raise typer.Exit()

    # Use the helper function to drop the app
    success = _drop_app(preview_name, database, schema, connection, verbose, drop_spcs)
    if not success:
        raise typer.Exit(code=1)


@app.command()
def new(
    output_dir: str | None = typer.Argument(
        None, help="Directory where the new app will be created"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force overwrite without confirmation"
    ),
    connection: str | None = typer.Option(
        None, "--connection", "-c", help="Name of the Snowflake connection to use"
    ),
    compute_type: str | None = typer.Option(
        "warehouse",
        "--compute-type",
        "-t",
        help="Type of compute to use: 'warehouse' or 'compute_pool'",
    ),
    query_warehouse: str | None = typer.Option(
        None,
        "--query-warehouse",
        "-q",
        help="Warehouse to use for queries (when using warehouse compute type)",
    ),
    app_warehouse: str | None = typer.Option(
        None,
        "--app-warehouse",
        "-a",
        help="Warehouse to use for running the app (when using warehouse compute type)",
    ),
    compute_pool: str | None = typer.Option(
        None,
        "--compute-pool",
        help="Compute pool to use (when using compute_pool compute type)",
    ),
    stage: str | None = typer.Option(
        None, "--stage", help="Stage to use for app artifacts"
    ),
) -> None:
    """
    Create a new Streamlit in Snowflake application using a template.

    This command uses snow init to generate a new app from the appropriate template
    based on your compute choice (warehouse or compute pool).

    All configuration can be provided via command line flags for automation, or
    will be prompted for interactively if not provided.
    """
    if verbose:
        typer.echo(f"Creating new Streamlit app in {output_dir}")

    if output_dir is None:
        output_dir = _get_output_dir()

    # Get connection info - either from flag or interactive
    if connection is not None:
        current_connection = get_connection_by_name(connection)
    else:
        current_connection = get_default_connection()

    # Get compute configuration - either from flags or interactive, defaulting to
    # values from the current connection
    compute_config = {}
    if compute_type is not None and compute_type not in ["warehouse", "compute_pool"]:
        typer.echo("compute-type must be either 'warehouse' or 'compute_pool'")
        raise typer.Exit(code=1)
    if compute_type is None:
        compute_type = "warehouse"
    compute_config["type"] = compute_type

    if query_warehouse is not None:
        compute_config["query_warehouse"] = query_warehouse
    if app_warehouse is not None:
        compute_config["app_warehouse"] = app_warehouse
    if compute_pool is not None:
        compute_config["compute_pool"] = compute_pool
    if stage is not None:
        compute_config["stage"] = stage

    compute_config = _get_compute_configuration(compute_config, current_connection)

    template_name = (
        "warehouse_app" if compute_config["type"] == "warehouse" else "compute_pool_app"
    )

    template_dir = get_template_dir()

    output_path = Path(output_dir)
    # Remove existing directory if it exists and force is True
    if output_path.exists():
        if not force and not typer.confirm(
            f"Directory '{output_dir}' already exists. Do you want to overwrite it?"
        ):
            typer.echo("Operation cancelled.")
            raise typer.Exit()
        # Remove existing directory
        try:
            shutil.rmtree(output_path)
            if verbose:
                typer.echo(f"Removed existing directory: {output_dir}")
        except Exception as e:
            typer.echo(f"Error removing existing directory: {e}")
            raise typer.Exit(code=1) from e

    template_variables = get_template_variables(output_path, compute_config)

    try:
        init_app(
            output_path=output_path,
            template_dir=template_dir,
            template_name=template_name,
            variables=template_variables,
            verbose=verbose,
        )
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error creating new Streamlit app: {e}")
        if e.stderr:
            typer.echo(f"Error details: {e.stderr}")
        raise typer.Exit(code=1) from e

    # Create secrets.toml after snow init succeeds
    try:
        create_secrets_file(output_path, current_connection, compute_config)
    except OSError as e:
        typer.echo(f"Error creating secrets.toml: {e}")
        raise typer.Exit(code=1) from e

    typer.echo(f"Successfully created new Streamlit app in {output_dir}!")


def _get_output_dir() -> str:
    """Get the output directory from the user."""
    return typer.prompt("Enter the directory where the new app will be created")


def _get_compute_configuration(
    compute_config: dict[str, Any],
    current_connection: dict[str, Any],
) -> dict[str, Any]:
    """Get compute configuration interactively from the user."""

    if "database" not in compute_config:
        # Get database, schema, and role first
        compute_config["database"] = typer.prompt(
            "What database should be used?",
            default=current_connection.get("database", "streamlit"),
        )
    if "schema" not in compute_config:
        compute_config["schema"] = typer.prompt(
            "What schema should be used?",
            default=current_connection.get("schema", "public"),
        )
    if "role" not in compute_config:
        compute_config["role"] = typer.prompt(
            "What role should be used?",
            default=current_connection.get("role", "ACCOUNTADMIN"),
        )

    # Get preview database and schema
    if (
        "preview_database" not in compute_config
        or "preview_schema" not in compute_config
        or "preview_role" not in compute_config
    ):
        if typer.confirm(
            "Would you like to specify different settings for preview deployments?",
            default=False,
        ):
            compute_config["preview_database"] = typer.prompt(
                "What database should be used for preview deployments?",
                default=compute_config["database"],
            )
            compute_config["preview_schema"] = typer.prompt(
                "What schema should be used for preview deployments?",
                default=compute_config["schema"],
            )
            compute_config["preview_role"] = typer.prompt(
                "What role should be used for preview deployments?",
                default=compute_config["role"],
            )
        else:
            compute_config["preview_database"] = compute_config["database"]
            compute_config["preview_schema"] = compute_config["schema"]
            compute_config["preview_role"] = compute_config["role"]

    if "type" not in compute_config:
        compute_type = typer.prompt(
            "Choose your compute type:\n1. Warehouse (traditional Snowflake warehouse)\n2. Compute Pool (serverless compute)",
            type=str,
            default="1",
        )
        if compute_type not in ["1", "2"]:
            typer.echo("Invalid compute type selected")
            raise typer.Exit(code=1)
        compute_config["type"] = "warehouse" if compute_type == "1" else "compute_pool"

    if compute_config["type"] == "warehouse":
        if "query_warehouse" not in compute_config:
            compute_config["query_warehouse"] = typer.prompt(
                "What warehouse should be used for queries?", default="compute_wh"
            )
        if "app_warehouse" not in compute_config:
            compute_config["app_warehouse"] = typer.prompt(
                "What warehouse should be used to run the app?",
                default="SYSTEM$STREAMLIT_NOTEBOOK_WH",
            )
    else:
        if "compute_pool" not in compute_config:
            compute_config["compute_pool"] = typer.prompt(
                "What compute pool should be used?", default="streamlit_compute_pool"
            )

    if "stage" not in compute_config and typer.confirm(
        "Would you like to specify a stage for app artifacts?", default=False
    ):
        compute_config["stage"] = typer.prompt(
            "What stage should be used?", default="streamlit_stage"
        )

    return compute_config


@app.command()
def run(
    app_path: str = typer.Argument(
        "streamlit_app.py", help="Path to the Streamlit app file to run"
    ),
) -> None:
    """
    Run a Streamlit application locally.

    This command wraps the `streamlit run` command, providing a convenient
    interface for running Streamlit applications during development.
    """
    typer.echo(f"Running Streamlit app: {app_path}")

    # Base command
    cmd = ["streamlit", "run", app_path]

    try:
        # Execute the command
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error running Streamlit app: {e}")
        if hasattr(e, "stderr") and e.stderr:
            typer.echo(f"Error details: {e.stderr}")
        raise typer.Exit(code=1) from e


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def test(ctx: typer.Context) -> None:
    """
    Run the tests for the CLI.
    """
    # Arbitrary arguments are passed to pytest
    args = ctx.args

    subprocess.run(["pytest", *args])


@app.command()
def cleanup(
    filter_text: str | None = typer.Argument(
        None, help="Text to filter apps by (uses preview_ if not specified)"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
    connection: str | None = typer.Option(
        None, "--connection", "-c", help="Connection to use for deployment"
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force cleanup without confirmation"
    ),
    drop_spcs: bool = typer.Option(
        False, "--drop-spcs", help="Also drop any associated SPCS services"
    ),
) -> None:
    """
    Drop multiple Streamlit applications containing the specified filter text.

    If no filter is provided, uses the text 'preview_' as the filter.
    This is useful for cleaning up development apps in your account.
    """
    if filter_text is None:
        filter_text = "preview_"
        if verbose:
            typer.echo("No filter provided. Using 'preview_' as filter")

    try:
        apps = list_streamlit_apps(
            filter_text=filter_text,
            connection=connection,
            verbose=verbose,
        )
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error listing apps: {e}")
        if e.stderr:
            typer.echo(f"Error details: {e.stderr}")
        raise typer.Exit(code=1) from e

    if not apps:
        typer.echo(f"No apps found matching filter: {filter_text}")
        return

    # Display the apps to be deleted
    typer.echo(f"Found {len(apps)} app(s) matching filter '{filter_text}':")
    for app in apps:
        full_name = f"{app['database_name']}.{app['schema_name']}.{app['name']}"
        typer.echo(f" - {full_name}")

    # Confirm deletion unless --force is specified
    if not force:
        confirm = typer.confirm("Are you sure you want to drop all these apps?")
        if not confirm:
            typer.echo("Operation cancelled.")
            raise typer.Exit()

    # Drop each app
    dropped_count = 0
    for app in apps:
        database = app["database_name"]
        schema = app["schema_name"]
        app_name = app["name"]
        full_name = f"{database}.{schema}.{app_name}"

        typer.echo(f"Dropping app: {full_name}")

        # Use the helper function to drop the app
        success = _drop_app(app_name, database, schema, connection, verbose, drop_spcs)
        if success:
            dropped_count += 1

    typer.echo(
        f"Successfully cleaned up {dropped_count} of {len(apps)} app(s) matching filter '{filter_text}'"
    )


def main() -> None:
    """
    Main entry point for the CLI.
    """
    return app(prog_name="sisx")


if __name__ == "__main__":
    main()
