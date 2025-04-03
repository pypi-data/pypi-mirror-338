# ruff: noqa: ARG001

import json
import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import yaml
from typer.testing import CliRunner

from sisx.cli import app


@pytest.fixture
def mock_config_file(tmp_path):
    """Create a mock snowflake.yml file."""
    config = {
        "env": {
            "name": "test_app",
            "database": "TEST_DB",
            "schema": "PUBLIC",
            "role": "ACCOUNTADMIN",
        },
        "streamlit": {"database": "TEST_DB", "schema": "PUBLIC"},
    }
    config_path = tmp_path / "snowflake.yml"
    with open(config_path, "w") as f:
        yaml.dump(config, f)
    return config_path


@pytest.fixture
def mock_snow_info():
    """Mock snow --info command."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value.stdout = json.dumps(
            [
                {
                    "key": "default_config_file_path",
                    "value": "/home/user/.snowflake/config.toml",
                }
            ]
        )
        yield mock_run


def test_drop_basic(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test basic drop command."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["drop", "--force"])

    assert result.exit_code == 0
    assert "Successfully dropped app 'TEST_DB.PUBLIC.test_app'" in result.stdout

    # Verify snow object drop was called with correct args
    mock_subprocess.assert_called_once()
    cmd_args = mock_subprocess.call_args[0][0]
    assert "uv" in cmd_args
    assert "run" in cmd_args
    assert "snow" in cmd_args
    assert "object" in cmd_args
    assert "drop" in cmd_args
    assert "streamlit" in cmd_args
    assert "TEST_DB.PUBLIC.test_app" in cmd_args


def test_drop_with_connection(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test drop command with connection override."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["drop", "--connection", "test_conn", "--force"])

    assert result.exit_code == 0

    cmd_args = mock_subprocess.call_args[0][0]
    assert "--connection" in cmd_args
    assert "test_conn" in cmd_args


def test_drop_with_spcs(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test drop command with SPCS cleanup."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["drop", "--drop-spcs", "--force"])

    assert result.exit_code == 0
    assert "Successfully dropped app 'TEST_DB.PUBLIC.test_app'" in result.stdout

    # Should have 2 calls - SPCS cleanup and drop
    assert mock_subprocess.call_count == 2

    # Check SPCS cleanup call
    spcs_args = mock_subprocess.call_args_list[0][0][0]
    assert "uv" in spcs_args
    assert "run" in spcs_args
    assert "snow" in spcs_args
    assert "sql" in spcs_args
    assert "-q" in spcs_args
    assert "CALL SYSTEM\\$DELETE_RUNNING_STREAMLIT_INSTANCES('test_app')" in " ".join(
        spcs_args
    )


def test_drop_without_force(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test drop command without force flag (should prompt)."""
    os.chdir(tmp_path)

    # Simulate user answering "n" to prompt
    result = runner.invoke(app, ["drop"], input="n\n")

    assert result.exit_code == 0
    assert "Are you sure" in result.stdout
    assert mock_subprocess.call_count == 0


def test_drop_preview_basic(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test basic drop-preview command."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["drop-preview", "--force"])

    assert result.exit_code == 0

    cmd_args = mock_subprocess.call_args[0][0]
    assert "preview_test_app" in " ".join(cmd_args)


def test_drop_preview_with_spcs(
    runner: CliRunner,
    mock_subprocess: MagicMock,
    mock_config_file: Path,
    tmp_path: Path,
) -> None:
    """Test drop-preview command with SPCS cleanup."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["drop-preview", "--drop-spcs", "--force"])

    assert result.exit_code == 0
    assert mock_subprocess.call_count == 2

    # Check SPCS cleanup call includes preview name
    spcs_args = " ".join(mock_subprocess.call_args_list[0][0][0])
    assert "preview_test_app" in spcs_args


def test_drop_missing_config(
    runner: CliRunner, mock_subprocess: MagicMock, tmp_path: Path
) -> None:
    """Test drop command with missing snowflake.yml."""
    os.chdir(tmp_path)

    result = runner.invoke(app, ["drop", "--force"])

    assert result.exit_code == 1
    assert "Error reading app configuration from snowflake.yml" in result.stdout


def test_drop_invalid_config(
    runner: CliRunner, mock_subprocess: MagicMock, tmp_path: Path
) -> None:
    """Test drop command with invalid snowflake.yml."""
    os.chdir(tmp_path)

    # Create invalid YAML file
    Path("snowflake.yml").write_text("invalid: yaml: content:")

    result = runner.invoke(app, ["drop", "--force"])

    assert result.exit_code == 1
    assert "Error reading app configuration from snowflake.yml" in result.stdout


def test_drop_requires_config(runner: CliRunner, tmp_path: Path) -> None:
    """Test drop command fails when no config file exists."""
    os.chdir(tmp_path)
    result = runner.invoke(app, ["drop", "--force"])
    assert result.exit_code == 1
    assert "Error reading app configuration from snowflake.yml" in result.stdout


def test_drop_with_config(
    runner: CliRunner, mock_subprocess: MagicMock, tmp_path: Path
) -> None:
    """Test drop command with valid config."""
    os.chdir(tmp_path)

    # Create a minimal snowflake.yml
    config = {
        "env": {"name": "test_app"},
        "streamlit": {"database": "TEST_DB", "schema": "PUBLIC"},
    }
    Path("snowflake.yml").write_text(yaml.dump(config))

    result = runner.invoke(app, ["drop", "--force"])
    assert result.exit_code == 0
    assert "Successfully dropped app 'TEST_DB.PUBLIC.test_app'" in result.stdout

    # Verify snow object drop was called with correct args
    mock_subprocess.assert_called_once()
    cmd_args = mock_subprocess.call_args[0][0]
    assert "TEST_DB.PUBLIC.test_app" in " ".join(cmd_args)


def test_drop_preview_requires_config(runner: CliRunner, tmp_path: Path) -> None:
    """Test drop-preview command fails when no config file exists."""
    os.chdir(tmp_path)
    result = runner.invoke(app, ["drop-preview", "--force"])
    assert result.exit_code == 1
    assert "Error reading app configuration from snowflake.yml" in result.stdout


def test_drop_preview_with_config(
    runner: CliRunner, mock_subprocess: MagicMock, tmp_path: Path
) -> None:
    """Test drop-preview command with valid config."""
    os.chdir(tmp_path)

    # Create a minimal snowflake.yml
    config = {
        "env": {"name": "test_app"},
        "streamlit": {"database": "TEST_DB", "schema": "PUBLIC"},
    }
    Path("snowflake.yml").write_text(yaml.dump(config))

    result = runner.invoke(app, ["drop-preview", "--force"])
    assert result.exit_code == 0
    assert "Successfully dropped app 'TEST_DB.PUBLIC.preview_test_app'" in result.stdout

    # Verify snow object drop was called with correct args
    mock_subprocess.assert_called_once()
    cmd_args = mock_subprocess.call_args[0][0]
    assert "TEST_DB.PUBLIC.preview_test_app" in " ".join(cmd_args)


def test_drop_prompts_without_force(runner: CliRunner, tmp_path: Path) -> None:
    """Test drop command prompts for confirmation without --force."""
    os.chdir(tmp_path)

    # Create a minimal snowflake.yml
    config = {
        "env": {"name": "test_app"},
        "streamlit": {"database": "TEST_DB", "schema": "PUBLIC"},
    }
    Path("snowflake.yml").write_text(yaml.dump(config))

    # Test with 'n' response
    result = runner.invoke(app, ["drop"], input="n\n")
    assert result.exit_code == 0
    assert "Are you sure" in result.stdout
    assert "Operation cancelled" in result.stdout
