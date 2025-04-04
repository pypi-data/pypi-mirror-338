import subprocess
import yaml
import os
import shutil
from typing import Any
from fastapi_forge.logger import logger


def git_init() -> None:
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])


def uv_init() -> None:
    subprocess.run(["uv", "lock"])


def lint() -> None:
    subprocess.run(["make", "lint"])


def make_env() -> None:
    subprocess.run(["cp", ".env.example", ".env"])


def _get_delete_flagged() -> tuple[list[str], list[str]]:
    conf_fn = "forge-config.yaml"
    with open(conf_fn) as stream:
        y = yaml.safe_load(stream)
        cwd = os.getcwd()
        files = [os.path.join(cwd, conf_fn)]
        folders = []
        config: dict[str, Any] = y["config"]

        for _, v in config.items():
            item_type = v["type"]
            if item_type != "bool":
                continue
            value: bool = v["value"]
            if value is True:
                continue
            paths: list[str] = v["paths"]
            if not paths:
                continue
            for path in paths:
                full_path = os.path.join(cwd, path)
                if path.endswith(".py") or path.endswith(".yaml"):
                    files.append(full_path)
                else:
                    folders.append(full_path)

    return files, folders


def delete_empty_init_folders(root_dir: str = "src") -> None:
    """Delete folders that only contain empty __init__.py files."""
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        if dirpath == root_dir:
            continue

        if set(filenames) == {"__init__.py"} and not dirnames:
            init_file = os.path.join(dirpath, "__init__.py")

            try:
                with open(init_file, "r") as f:
                    content = f.read()
                    has_code = any(
                        line.strip() and not line.strip().startswith("#")
                        for line in content.splitlines()
                    )
                if not has_code:
                    os.remove(init_file)
                    os.rmdir(dirpath)
                    logger.info(f"Deleted empty package: {dirpath}")
                else:
                    logger.info(f"Keeping package with code: {dirpath}")
            except OSError as exc:
                logger.info(f"Error processing package {dirpath}: {exc}")


def cleanup():
    files, folders = _get_delete_flagged()

    for file_path in files:
        try:
            os.remove(file_path)
            logger.info(f"Deleted file: {file_path}")
        except OSError as exc:
            logger.info(f"Error deleting file {file_path}: {exc}")

    for folder_path in folders:
        try:
            shutil.rmtree(folder_path)
            logger.info(f"Deleted folder: {folder_path}")
        except OSError as exc:
            logger.info(f"Error deleting folder {folder_path}: {exc}")

    delete_empty_init_folders()


if __name__ == "__main__":
    cleanup()
    uv_init()
    make_env()
    lint()
    # git_init()
