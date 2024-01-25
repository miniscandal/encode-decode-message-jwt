"""
Module resposibility:
"""

import os


def read_env_var_algorithm() -> str:
    # pylint:disable = C0116

    algorithm = os.getenv("ALGORITHM")

    return algorithm  # type: ignore


def read_env_var_jwt_file_path() -> str:
    # pylint:disable = C0116

    path = os.getenv("JWT_FILE_PATH")

    return path  # type: ignore


def read_env_var_message_file_path() -> str:
    # pylint:disable = C0116

    path = os.getenv("MESSAGE_FILE_PATH")

    return path  # type: ignore


def get_path_pem_file(pem_file_name: str) -> str:
    # pylint:disable = C0116

    directory_path = os.getenv("DIRECTORY_PATH_PEM_FILE")

    path = f"{directory_path}\\{os.getenv(pem_file_name)}"

    return path
