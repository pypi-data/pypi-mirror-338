# ruff: noqa: ARG001

import os
from pathlib import Path
from unittest.mock import MagicMock

import yaml
from typer.testing import CliRunner

from sisx.cli import app


def test_deploy_basic(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test basic deploy command."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["deploy"])

    assert result.exit_code == 0
    assert "App 'test_app' successfully deployed!" in result.stdout

    # Verify snow streamlit deploy was called with correct args
    mock_subprocess.assert_called_once()
    cmd_args = mock_subprocess.call_args[0][0]
    assert "uv" in cmd_args
    assert "run" in cmd_args
    assert "snow" in cmd_args
    assert "streamlit" in cmd_args
    assert "deploy" in cmd_args

    # Check environment variables were passed correctly
    env_args = [arg for arg in cmd_args if arg.startswith("--env")]
    assert any("name=test_app" in arg for arg in env_args)
    assert any("database=TEST_DB" in arg for arg in env_args)
    assert any("schema=PUBLIC" in arg for arg in env_args)
    assert any("role=ACCOUNTADMIN" in arg for arg in env_args)


def test_deploy_with_preview(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    mock_snowflake_connection: MagicMock,
    tmp_path: Path,
) -> None:
    """Test deployment with preview flag."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["deploy-preview"])

    assert result.exit_code == 0
    assert "App 'preview_test_app' successfully deployed!" in result.stdout

    cmd_args = mock_subprocess.call_args[0][0]
    env_args = [arg for arg in cmd_args if arg.startswith("--env")]
    assert any("name=preview_test_app" in arg for arg in env_args)
    assert any("title=PREVIEW:" in arg for arg in env_args)


def test_deploy_with_custom_config(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_snowflake_connection: MagicMock,
    tmp_path: Path,
) -> None:
    """Test deployment with custom config file."""
    config = {
        "env": {
            "name": "custom_app",
            "database": "CUSTOM_DB",
            "schema": "CUSTOM_SCHEMA",
            "role": "CUSTOM_ROLE",
            "warehouse": "CUSTOM_WH",
        }
    }
    config_path = tmp_path / "snowflake.yml"
    with open(config_path, "w") as f:
        yaml.dump(config, f)

    os.chdir(tmp_path)
    result = runner.invoke(app, ["deploy"])

    assert result.exit_code == 0
    assert "App 'custom_app' successfully deployed!" in result.stdout

    cmd_args = mock_subprocess.call_args[0][0]
    env_args = [arg for arg in cmd_args if arg.startswith("--env")]
    assert any("name=custom_app" in arg for arg in env_args)
    assert any("database=CUSTOM_DB" in arg for arg in env_args)
    assert any("schema=CUSTOM_SCHEMA" in arg for arg in env_args)
    assert any("role=CUSTOM_ROLE" in arg for arg in env_args)


def test_deploy_missing_config(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    tmp_path: Path,
) -> None:
    """Test deploy command with missing snowflake.yml."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["deploy"])

    assert result.exit_code == 1
    assert "Error reading app configuration from snowflake.yml" in result.stdout


def test_deploy_invalid_config(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    tmp_path: Path,
) -> None:
    """Test deploy command with invalid snowflake.yml."""
    os.chdir(tmp_path)

    # Create invalid YAML file
    Path("snowflake.yml").write_text("invalid: yaml: content:")

    result = runner.invoke(app, ["deploy"])

    assert result.exit_code == 1
    assert "Error reading app configuration from snowflake.yml" in result.stdout


def test_deploy_with_overrides(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test deploy command with overrides."""
    os.chdir(tmp_path)

    result = runner.invoke(
        app,
        [
            "deploy",
            "--query-warehouse",
            "QUERY_WH",
            "--app-warehouse",
            "APP_WH",
            "--connection",
            "test_conn",
        ],
    )

    assert result.exit_code == 0
    assert "App 'test_app' successfully deployed!" in result.stdout

    cmd_args = mock_subprocess.call_args[0][0]
    env_args = [arg for arg in cmd_args if arg.startswith("--env")]
    assert any("query_warehouse=QUERY_WH" in arg for arg in env_args)
    assert any("app_warehouse=APP_WH" in arg for arg in env_args)
    assert "--connection" in cmd_args
    assert "test_conn" in cmd_args


def test_deploy_preview_basic(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test basic deploy-preview command."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["deploy-preview"])

    assert result.exit_code == 0
    assert "App 'preview_test_app' successfully deployed!" in result.stdout

    cmd_args = mock_subprocess.call_args[0][0]
    env_args = [arg for arg in cmd_args if arg.startswith("--env")]

    # Check preview name and title
    assert any("name=preview_test_app" in arg for arg in env_args)
    assert any("title=PREVIEW:" in arg for arg in env_args)

    # Check preview settings
    assert any("database=PREVIEW_DB" in arg for arg in env_args)
    assert any("schema=PREVIEW_SCHEMA" in arg for arg in env_args)
    assert any("role=PREVIEW_ROLE" in arg for arg in env_args)


def test_deploy_preview_custom_name(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test deploy-preview command with custom preview name."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["deploy-preview", "--preview-name", "custom_preview"])

    assert result.exit_code == 0
    assert "App 'custom_preview' successfully deployed!" in result.stdout

    cmd_args = mock_subprocess.call_args[0][0]
    env_args = [arg for arg in cmd_args if arg.startswith("--env")]
    assert any("name=custom_preview" in arg for arg in env_args)
