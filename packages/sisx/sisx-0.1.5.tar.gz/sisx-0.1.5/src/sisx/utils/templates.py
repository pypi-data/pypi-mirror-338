import json
import shutil
from importlib import resources
from pathlib import Path
from typing import Any


def get_template_dir() -> Path:
    with resources.path("sisx", "templates") as templates_path:
        return templates_path


def copy_shared_files(template_dir: Path, target_dir: Path) -> None:
    """Copy shared files from the template directory to the target directory.

    Args:
        template_dir: Path to the template directory
        target_dir: Path to copy files to
    """
    shared_dir = template_dir / "shared"

    # Create directories if they don't exist
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / ".streamlit").mkdir(parents=True, exist_ok=True)
    (target_dir / "pages").mkdir(parents=True, exist_ok=True)

    # Copy shared files
    shutil.copytree(
        shared_dir / ".streamlit", target_dir / ".streamlit", dirs_exist_ok=True
    )
    shutil.copytree(shared_dir / "pages", target_dir / "pages", dirs_exist_ok=True)
    shutil.copy2(shared_dir / "connection.py", target_dir / "connection.py")
    shutil.copy2(shared_dir / "streamlit_app.py", target_dir / "streamlit_app.py")
    shutil.copy2(shared_dir / "__init__.py", target_dir / "__init__.py")


def get_template_variables(
    output_dir: Path, compute_config: dict[str, Any]
) -> dict[str, Any]:
    variables = {
        "name": output_dir.name,
        "schema": compute_config["schema"],
        "database": compute_config["database"],
        "role": compute_config["role"],
        "preview_database": compute_config.get(
            "preview_database", compute_config["database"]
        ),
        "preview_schema": compute_config.get(
            "preview_schema", compute_config["schema"]
        ),
        "preview_role": compute_config.get("preview_role", compute_config["role"]),
    }

    # Add env section variables
    env_variables = {
        "name": variables["name"],
        "schema": variables["schema"],
        "database": variables["database"],
        "role": variables["role"],
        "preview_database": variables["preview_database"],
        "preview_schema": variables["preview_schema"],
        "preview_role": variables["preview_role"],
    }

    if compute_config["type"] == "warehouse":
        variables["query_warehouse"] = compute_config["query_warehouse"]
        variables["app_warehouse"] = compute_config["app_warehouse"]
        variables["artifacts"] = (
            '"**/*.py", "*.yml"'  # No requirements.txt for warehouse apps
        )
        env_variables["query_warehouse"] = compute_config["query_warehouse"]
        env_variables["app_warehouse"] = compute_config["app_warehouse"]
    else:
        variables["compute_pool"] = compute_config["compute_pool"]
        variables["artifacts"] = (
            '"**/*.py", "requirements.txt", "*.yml"'  # Include requirements.txt for compute pool apps
        )
        env_variables["compute_pool"] = compute_config["compute_pool"]

    if "stage" in compute_config:
        variables["stage"] = compute_config["stage"]
        env_variables["stage"] = compute_config["stage"]

    variables["env"] = json.dumps(env_variables)

    return variables
