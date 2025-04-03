import json
import subprocess
from pathlib import Path
from typing import Any, Optional, Sequence

import typer


def run_snow_command(
    cmd_args: Sequence[str], capture_output: bool = True, check: bool = True
) -> subprocess.CompletedProcess:
    """Run a snow CLI command with proper UV wrapping."""
    full_cmd = ["uv", "run", "snow", *cmd_args]
    return subprocess.run(
        full_cmd, check=check, capture_output=capture_output, text=True
    )


def deploy_streamlit(
    *,
    name: str,
    database: str,
    schema: str,
    role: str,
    title: Optional[str] = None,
    replace: bool = False,
    open_browser: bool = False,
    connection: Optional[str] = None,
    query_warehouse: Optional[str] = None,
    app_warehouse: Optional[str] = None,
    verbose: bool = False,
    debug: bool = False,
) -> subprocess.CompletedProcess:
    """Deploy a Streamlit application using the snow CLI."""
    cmd = ["streamlit", "deploy"]

    if replace:
        cmd.append("--replace")

    if open_browser:
        cmd.append("--open")

    if connection:
        cmd.extend(["--connection", connection])

    # Add environment variables
    cmd.append(f"--env=name={name}")
    if title:
        cmd.append(f"--env=title={title}")

    # Add database, schema, and role
    cmd.extend(["--database", database])
    cmd.extend(["--schema", schema])
    cmd.extend(["--role", role])

    # Handle warehouse overrides through env variables
    if query_warehouse:
        cmd.append(f"--env=query_warehouse={query_warehouse}")
    if app_warehouse:
        cmd.append(f"--env=app_warehouse={app_warehouse}")

    cmd.append(f"--env=database={database}")
    cmd.append(f"--env=schema={schema}")
    cmd.append(f"--env=role={role}")

    if verbose:
        cmd.append("--verbose")

    if debug:
        cmd.append("--debug")

    return run_snow_command(cmd, capture_output=not verbose)


def drop_streamlit(
    app_name: str,
    database: str,
    schema: str,
    connection: Optional[str] = None,
    verbose: bool = False,
) -> subprocess.CompletedProcess:
    """Drop a Streamlit application using the snow CLI."""
    full_app_name = f"{database}.{schema}.{app_name}"
    cmd = ["object", "drop", "streamlit", full_app_name]

    if connection:
        cmd.extend(["--connection", connection])

    return run_snow_command(cmd, capture_output=not verbose)


def drop_spcs_services(
    app_name: str,
    connection: Optional[str] = None,
    verbose: bool = False,
) -> subprocess.CompletedProcess:
    """Drop SPCS services associated with a Streamlit app."""
    cmd = [
        "sql",
        "-q",
        f"CALL SYSTEM\\$DELETE_RUNNING_STREAMLIT_INSTANCES('{app_name}')",
    ]

    if connection:
        cmd.extend(["--connection", connection])

    return run_snow_command(cmd, capture_output=not verbose, check=False)


def list_streamlit_apps(
    filter_text: Optional[str] = None,
    connection: Optional[str] = None,
    verbose: bool = False,
) -> list[dict[str, Any]]:
    """List Streamlit applications in Snowflake."""
    cmd = ["object", "list", "streamlit", "--format=json"]

    if filter_text:
        cmd.extend(["--like", f"%{filter_text}%"])

    if connection:
        cmd.extend(["--connection", connection])

    if verbose:
        cmd.append("--verbose")

    result = run_snow_command(cmd, capture_output=True)
    return json.loads(result.stdout)


def init_app(
    output_path: Path,
    template_dir: Path,
    template_name: str,
    variables: dict[str, str],
    verbose: bool = False,
    debug: bool = False,
) -> subprocess.CompletedProcess:
    """Initialize a new Streamlit application using the snow CLI."""
    cmd = [
        "init",
        str(output_path),
        "--template-source",
        str(template_dir),
        "--template",
        template_name,
        "--no-interactive",
    ]

    typer.echo(f"Variables: {variables}")

    # Add all variables
    for key, value in variables.items():
        cmd.extend(["-D", f"{key}={value}"])

    if verbose:
        cmd.append("--verbose")
        typer.echo(f"Command: {' '.join(cmd)}")

    if debug:
        cmd.append("--debug")
        typer.echo(f"Command: {' '.join(cmd)}")

    return run_snow_command(cmd)


def get_snow_info() -> list[dict[str, Any]]:
    """Get information about the snow CLI configuration."""
    result = run_snow_command(["--info"])
    return json.loads(result.stdout)
