import importlib
from pathlib import Path
from typing import Any, Optional
from fastapi import FastAPI
import tomllib


def find_pyproject_toml() -> Optional[Path]:
    current = Path.cwd()
    while current != current.parent:
        pyproject_path = current / "pyproject.toml"
        if pyproject_path.exists():
            return pyproject_path
        current = current.parent
    return None

def load_pyproject_config() -> Optional[dict[str, Any]]:
    pyproject_path = find_pyproject_toml()
    if not pyproject_path:
        return None

    with open(pyproject_path, "rb") as f:
        return tomllib.load(f)

def get_app_entrypoint(config: dict[str, Any]) -> tuple[str, str] | None:
    try:
        config_value = config.get("tool", {}).get("nephyx", {}).get("app")
        module_path, obj = config_value.split(":")
        return module_path, obj
    except (KeyError, AttributeError):
        return None

def import_app_entrypoint() -> FastAPI:
    config = load_pyproject_config()
    app_entrypoint = get_app_entrypoint(config)
    if not app_entrypoint:
        raise ValueError("Could not find app entrypoint in pyproject.toml")
    module_path, app_name = app_entrypoint
    module = importlib.import_module(module_path)
    return getattr(module, app_name)
