"""
Module resposibility:
"""

import os


def get_path_pem_file(pem_file_name: str) -> str:
    # pylint:disable = C0116

    directory_path = os.getenv("DIRECTORY_PATH_PEM_FILE")

    path = f"{directory_path}\\{os.getenv(pem_file_name)}"

    return path
