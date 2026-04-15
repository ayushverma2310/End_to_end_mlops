import os
import yaml
import json
import joblib
from pathlib import Path
from typing import Any

from box import ConfigBox
from ensure import ensure_annotations

from ml_project import logger


# =========================
# READ YAML FILE
# =========================
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads YAML file and returns ConfigBox

    Args:
        path_to_yaml (Path): path to yaml file

    Raises:
        ValueError: if yaml file is empty

    Returns:
        ConfigBox: yaml content
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

            if content is None:
                raise ValueError("YAML file is empty")

            logger.info(f"YAML file loaded successfully from: {path_to_yaml}")
            return ConfigBox(content)

    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e


# =========================
# CREATE DIRECTORIES
# =========================
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create list of directories

    Args:
        path_to_directories (List[Path]): list of directory paths
        verbose (bool): log creation info
    """
    for path in path_to_directories:
        Path(path).mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


# =========================
# SAVE JSON
# =========================
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data

    Args:
        path (Path): path to json file
        data (dict): data to save
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logger.info(f"JSON file saved at: {path}")


# =========================
# LOAD JSON
# =========================
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as ConfigBox
    """
    with open(path, "r") as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


# =========================
# SAVE BINARY FILE
# =========================
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file using joblib

    Args:
        data (Any): data to save
        path (Path): file path
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


# =========================
# LOAD BINARY FILE
# =========================
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file

    Args:
        path (Path): file path

    Returns:
        Any: loaded object
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


# =========================
# GET FILE SIZE
# =========================
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get file size in KB

    Args:
        path (Path): file path

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"