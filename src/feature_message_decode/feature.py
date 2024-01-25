"""
Module responsibility:
"""

# pylint:disable=E0611
# pylint:disable=E0401
# pylint:disable = C0116

import os
import argparse
import jwt

from shared.feature_load_pem_files.feature import load_public_pem_file
from shared.feature_get_path_pem_file.feature import get_path_pem_file


def load_message(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_message(path: str, message: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(message)


def message_decode(arguments: argparse.Namespace) -> None:
    # pylint:disable = W0613

    path_jwt = os.getenv("JWT_FILE_PATH")
    path_pem_public = get_path_pem_file("PUBLIC_PEM_FILE_NAME")
    algorithm = os.getenv("ALGORITHM")

    jwt_message = load_message(path=path_jwt)  # type: ignore
    public_pem = load_public_pem_file(path=path_pem_public)
    decoded_jwt = jwt.decode(jwt_message, public_pem, algorithms=algorithm)  # type: ignore
    print(decoded_jwt)
