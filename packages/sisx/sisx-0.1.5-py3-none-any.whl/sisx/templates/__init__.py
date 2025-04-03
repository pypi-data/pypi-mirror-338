"""Template management for sisx."""

import os
import shutil
from pathlib import Path
from typing import Literal

import pkg_resources

TemplateType = Literal["warehouse_app", "compute_pool_app"]


def get_template_dir() -> Path:
    """Get the directory containing the templates."""
    return Path(pkg_resources.resource_filename("sisx.templates", ""))


def copy_template(template_type: TemplateType, target_dir: Path) -> None:
    """Copy a template to the target directory.

    Args:
        template_type: Type of template to copy
        target_dir: Directory to copy the template to
    """
    template_dir = get_template_dir()
    shared_dir = template_dir / "shared"
    app_template_dir = template_dir / template_type

    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy app-specific files
    for item in app_template_dir.glob("*"):
        if item.is_symlink():  # Skip symlinks as we'll handle shared files separately
            continue
        if item.is_file():
            shutil.copy2(item, target_dir / item.name)
        elif item.is_dir():
            shutil.copytree(item, target_dir / item.name, dirs_exist_ok=True)

    # Copy shared files
    shutil.copytree(
        shared_dir / ".streamlit", target_dir / ".streamlit", dirs_exist_ok=True
    )
    shutil.copytree(shared_dir / "pages", target_dir / "pages", dirs_exist_ok=True)
    shutil.copy2(shared_dir / "connection.py", target_dir / "connection.py")
    shutil.copy2(shared_dir / "streamlit_app.py", target_dir / "streamlit_app.py")
