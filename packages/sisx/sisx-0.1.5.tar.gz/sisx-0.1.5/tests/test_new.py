# ruff: noqa: ARG001

import os
from pathlib import Path
from unittest.mock import MagicMock

import yaml
from typer.testing import CliRunner

from sisx.cli import app


def test_new_command_warehouse_basic(
    runner: CliRunner,
    mock_snow_info: MagicMock,
    tmp_path: Path,
):
    """Test basic warehouse app creation."""
    result = runner.invoke(
        app,
        [
            "new",
            str(tmp_path),
            "--compute-type",
            "warehouse",
            "--query-warehouse",
            "COMPUTE_WH",
            "--app-warehouse",
            "STREAMLIT_WH",
            "--force",
            "--connection",
            "default",
            "--verbose",
        ],
    )

    print(result.stdout)
    # Get more error info
    print(result)
    assert result.exit_code == 0
    assert "Successfully created new Streamlit app" in result.stdout

    # Verify snow init was called with correct args
    mock_snow_info.assert_called()
    cmd_args = mock_snow_info.call_args[0][0]
    assert "uv" in cmd_args
    assert "run" in cmd_args
    assert "snow" in cmd_args
    assert "init" in cmd_args
    assert "--template" in cmd_args
    assert "warehouse_app" in cmd_args

    # Check config files were created
    assert (tmp_path / "snowflake.yml").exists()
    assert (tmp_path / ".streamlit" / "secrets.toml").exists()


def test_new_command_compute_pool_basic(
    runner: CliRunner,
    mock_snow_info: MagicMock,
    tmp_path: Path,
):
    """Test basic compute pool app creation."""
    result = runner.invoke(
        app,
        [
            "new",
            str(tmp_path),
            "--compute-type",
            "compute_pool",
            "--compute-pool",
            "TEST_POOL",
            "--force",
        ],
    )

    print(result.stdout)
    assert result.exit_code == 0
    assert "Successfully created new Streamlit app" in result.stdout

    # Verify snow init was called with correct args
    mock_snow_info.assert_called()
    cmd_args = mock_snow_info.call_args[0][0]
    assert "compute_pool_app" in cmd_args

    # Check config files were created
    assert (tmp_path / "snowflake.yml").exists()
    assert (tmp_path / ".streamlit" / "secrets.toml").exists()


def test_new_command_with_preview_settings(
    runner: CliRunner,
    mock_snow_info: MagicMock,
    tmp_path: Path,
):
    """Test app creation with preview deployment settings."""
    result = runner.invoke(
        app,
        [
            "new",
            str(tmp_path),
            "--compute-type",
            "warehouse",
            "--query-warehouse",
            "COMPUTE_WH",
            "--app-warehouse",
            "STREAMLIT_WH",
            "--force",
        ],
    )

    assert result.exit_code == 0

    snowflake_yml = tmp_path / "snowflake.yml"
    config = yaml.safe_load(snowflake_yml.read_text())

    # Check preview settings
    assert config["env"]["preview_database"] == config["env"]["database"]
    assert config["env"]["preview_schema"] == config["env"]["schema"]
    assert config["env"]["preview_role"] == config["env"]["role"]


def test_new_command_with_stage(
    runner: CliRunner,
    mock_snow_info: MagicMock,
    tmp_path: Path,
):
    """Test app creation with custom stage."""
    result = runner.invoke(
        app,
        [
            "new",
            str(tmp_path),
            "--compute-type",
            "warehouse",
            "--query-warehouse",
            "COMPUTE_WH",
            "--app-warehouse",
            "STREAMLIT_WH",
            "--stage",
            "CUSTOM_STAGE",
            "--force",
        ],
    )

    assert result.exit_code == 0
    assert "Successfully created new Streamlit app" in result.stdout

    # Verify stage was set in the generated snowflake.yml
    snowflake_yml = tmp_path / "snowflake.yml"
    assert snowflake_yml.exists()
    config = yaml.safe_load(snowflake_yml.read_text())
    assert config["env"]["stage"] == "CUSTOM_STAGE"


def test_new_command_existing_directory(
    runner: CliRunner,
    mock_snow_info: MagicMock,
    tmp_path: Path,
):
    """Test app creation when directory exists without force flag."""
    # Create the directory first
    os.makedirs(tmp_path, exist_ok=True)

    result = runner.invoke(
        app,
        [
            "new",
            str(tmp_path),
            "--compute-type",
            "warehouse",
            "--query-warehouse",
            "COMPUTE_WH",
            "--app-warehouse",
            "STREAMLIT_WH",
        ],
    )

    # Should prompt for confirmation
    assert result.exit_code == 0
    assert "already exists" in result.stdout


def test_new_command_invalid_compute_type(
    runner: CliRunner,
    mock_snow_info: MagicMock,
    tmp_path: Path,
):
    """Test app creation with invalid compute type."""
    result = runner.invoke(
        app,
        ["new", str(tmp_path), "--compute-type", "invalid", "--force"],
    )

    assert result.exit_code == 1
    assert "compute-type must be either 'warehouse' or 'compute_pool'" in result.stdout
