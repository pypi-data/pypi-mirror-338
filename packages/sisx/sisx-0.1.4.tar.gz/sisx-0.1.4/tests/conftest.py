import json
import subprocess
from pathlib import Path
from typing import Generator
from unittest.mock import MagicMock, patch

import pytest
import toml
import yaml
from typer.testing import CliRunner


@pytest.fixture
def runner() -> CliRunner:
    """Create a CLI runner for testing."""
    return CliRunner()


@pytest.fixture
def mock_subprocess(mock_config_toml: Path) -> Generator[MagicMock, None, None]:
    """Mock subprocess.run for testing."""
    with patch("subprocess.run") as mock_run:

        def side_effect(cmd_args: list[str], *args, **kwargs) -> MagicMock:  # noqa: ARG001
            mock_result = MagicMock()
            mock_result.returncode = 0

            # Handle snow --info command
            if "snow" in cmd_args and "--info" in cmd_args:
                mock_result.stdout = json.dumps(
                    [
                        {
                            "key": "default_config_file_path",
                            "value": str(mock_config_toml),
                        }
                    ]
                )
            # Handle all other commands
            else:
                mock_result.stdout = ""

            return mock_result

        mock_run.side_effect = side_effect
        yield mock_run


@pytest.fixture
def mock_snowflake_connection() -> Generator[MagicMock, None, None]:
    """Mock snowflake connection.

    Returns:
        Generator[MagicMock, None, None]: A mock object that simulates a Snowflake connection with cursor.
    """
    with patch("snowflake.connector.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        yield mock_connect


@pytest.fixture
def mock_config_file(tmp_path: Path) -> Path:
    """Create a mock snowflake.yml file.

    Args:
        tmp_path: Pytest fixture that provides a temporary directory unique to each test function.

    Returns:
        Path: Path to the created mock config file.
    """
    config = {
        "env": {
            "name": "test_app",
            "database": "TEST_DB",
            "schema": "PUBLIC",
            "role": "ACCOUNTADMIN",
            "preview_database": "PREVIEW_DB",
            "preview_schema": "PREVIEW_SCHEMA",
            "preview_role": "PREVIEW_ROLE",
        },
        "streamlit": {"database": "TEST_DB", "schema": "PUBLIC"},
    }
    config_path = tmp_path / "snowflake.yml"
    with open(config_path, "w") as f:
        yaml.dump(config, f)
    return config_path


@pytest.fixture
def mock_config_toml(tmp_path: Path) -> Path:
    """Create a mock config.toml file.

    Args:
        tmp_path: Pytest fixture that provides a temporary directory unique to each test function.

    Returns:
        Path: Path to the created mock config.toml file.
    """
    config = {
        "connections": {
            "default": {
                "account": "test_account",
                "user": "test_user",
                "role": "ACCOUNTADMIN",
                "database": "TEST_DB",
                "schema": "PUBLIC",
                "warehouse": "COMPUTE_WH",
                "is_current": True,
            }
        },
    }
    config_path = tmp_path / ".snowflake" / "config.toml"
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with open(config_path, "w") as f:
        toml.dump(config, f)
    return config_path


@pytest.fixture
def mock_snow_info(mock_config_toml: Path) -> Generator[MagicMock, None, None]:
    """Mock snow --info command, but let other subprocess calls run normally."""
    real_subprocess_run = subprocess.run  # Store the original function

    def mock_run_impl(cmd_args, *args, **kwargs):
        # Only mock snow --info command
        if isinstance(cmd_args, list) and "snow" in cmd_args and "--info" in cmd_args:
            mock_result = MagicMock()
            mock_result.stdout = json.dumps(
                [
                    {
                        "key": "default_config_file_path",
                        "value": str(mock_config_toml),
                    }
                ]
            )
            mock_result.returncode = 0
            return mock_result
        # Use the original subprocess.run for all other calls
        return real_subprocess_run(cmd_args, *args, **kwargs)

    with patch("subprocess.run", side_effect=mock_run_impl) as mock_run:
        yield mock_run
