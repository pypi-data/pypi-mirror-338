# sisx

A command-line interface (CLI) for managing Streamlit applications in Snowflake.

## Overview

`sisx` provides a set of commands to simplify the workflow for developing, deploying, and managing Streamlit applications on Snowflake. It handles common tasks like deploying applications, creating preview versions, and cleaning up old deployments.

## Installation

```bash
uv tool install sisx

# Or

pip install sisx
```

If you don't want to actually install the tool permanently, you can just run `uvx sisx <any command>` to use it.

## Commands

### Deploy Commands

#### `deploy`

Deploy a Streamlit application to Snowflake.

```bash
sisx deploy [--verbose] [--replace] [--no-open] [--connection NAME] [--query-warehouse NAME] [--app-warehouse NAME] [--debug]
```

Options:
- `--verbose`, `-v`: Enable verbose output
- `--replace`, `-r`: Replace existing app if it exists
- `--no-open`: Don't open the deployed app in a browser (opens by default)
- `--connection`, `-c`: Connection name to use
- `--query-warehouse`: Override the query warehouse to use
- `--app-warehouse`: Override the app warehouse to use
- `--debug`: Enable debug output

#### `deploy-preview`

Deploy a preview version of your application with "preview_" prefix and "PREVIEW:" title.

```bash
sisx deploy-preview [--preview-name NAME] [--verbose] [--replace] [--no-open] [--connection NAME] [--debug]
```

Options:
- `--preview-name`: Custom name for the preview app (defaults to "preview_" + original name)
- `--verbose`, `-v`: Enable verbose output
- `--replace`, `-r`: Replace existing preview if it exists
- `--no-open`: Don't open the deployed app in a browser (opens by default)
- `--connection`, `-c`: Connection name to use
- `--debug`: Enable debug output

### Management Commands

#### `drop`

Remove a deployed Streamlit application.

```bash
sisx drop [--verbose] [--connection NAME] [--force] [--drop-spcs]
```

Options:
- `--verbose`, `-v`: Enable verbose output
- `--connection`, `-c`: Connection name to use
- `--force`, `-f`: Force drop without confirmation
- `--drop-spcs`: Also drop any associated SPCS services

#### `drop-preview`

Remove a preview version of a Streamlit application.

```bash
sisx drop-preview [--verbose] [--connection NAME] [--force] [--drop-spcs]
```

Options:
- `--verbose`, `-v`: Enable verbose output
- `--connection`, `-c`: Connection name to use
- `--force`, `-f`: Force drop without confirmation
- `--drop-spcs`: Also drop any associated SPCS services

#### `cleanup`

Remove multiple applications matching a filter.

```bash
sisx cleanup [FILTER] [--verbose] [--connection NAME] [--force] [--drop-spcs]
```

If no filter is specified, this will remove all apps with "preview_" prefix by default.

Options:
- `--verbose`, `-v`: Enable verbose output
- `--connection`, `-c`: Connection name to use
- `--force`, `-f`: Force cleanup without confirmation
- `--drop-spcs`: Also drop any associated SPCS services

### Development Commands

#### `new`

Create a new Streamlit app from a template.

```bash
sisx new [OUTPUT_DIR] [--verbose] [--force] [--connection NAME] [--compute-type TYPE] [--query-warehouse NAME] [--app-warehouse NAME] [--compute-pool NAME] [--stage NAME]
```

Options:
- `--verbose`, `-v`: Enable verbose output
- `--force`, `-f`: Force overwrite without confirmation
- `--connection`, `-c`: Name of the Snowflake connection to use
- `--compute-type`, `-t`: Type of compute to use: 'warehouse' or 'compute_pool' (default: warehouse)
- `--query-warehouse`, `-q`: Warehouse to use for queries (when using warehouse compute type)
- `--app-warehouse`, `-a`: Warehouse to use for running the app (when using warehouse compute type)
- `--compute-pool`: Compute pool to use (when using compute_pool compute type)
- `--stage`: Stage to use for app artifacts

#### `run`

Run a Streamlit app locally for development.

```bash
sisx run [APP_PATH]
```

Default app path is `streamlit_app.py`.

#### `test`

Run tests on your app. Any app you create with `sisx new` will have a test file created for it, that will go through all the pages of your app, and make sure they
all run without errors.

```bash
sisx test [PYTEST_ARGS]
```

Any additional arguments are passed directly to pytest.

## Configuration

`sisx` uses the `snowflake.yml` file in your project directory for configuration. This defines your app's name, database, schema, and other settings.

Example `snowflake.yml` for warehouse compute type:

```yaml
definition_version: "2"
env:
  name: "my_app"
  query_warehouse: "compute_wh"
  app_warehouse: "SYSTEM$STREAMLIT_NOTEBOOK_WH"
  schema: "public"
  database: "streamlit"
  role: "ACCOUNTADMIN"
  preview_database: "streamlit"
  preview_schema: "public"
  preview_role: "ACCOUNTADMIN"
  stage: "streamlit_stage"
entities:
  streamlit_app:
    type: streamlit
    identifier:
      name: <% ctx.env.name %>
      schema: <% ctx.env.schema %>
      database: <% ctx.env.database %>
    stage: <% ctx.env.stage %>
    query_warehouse: <% ctx.env.query_warehouse %>
    main_file: streamlit_app.py
    pages_dir: pages/
    artifacts:
      - "**/*.py"
      - "*.yml"
```

Example `snowflake.yml` for compute pool type:

```yaml
definition_version: "2"
env:
  name: "my_app"
  compute_pool: "streamlit_compute_pool"
  schema: "public"
  database: "streamlit"
  preview_database: "streamlit"
  preview_schema: "public"
  preview_role: "ACCOUNTADMIN"
  stage: "streamlit_stage"
entities:
  streamlit_app:
    type: streamlit
    identifier:
      name: <% ctx.env.name %>
      schema: <% ctx.env.schema %>
      database: <% ctx.env.database %>
    stage: <% ctx.env.stage %>
    compute_pool: <% ctx.env.compute_pool %>
    main_file: streamlit_app.py
    pages_dir: pages/
    artifacts:
      - "**/*.py"
      - "requirements.txt"
      - "*.yml"
```

## Version Information

You can check the version of sisx by running:

```bash
uvx sisx --version
```

## License

MIT
