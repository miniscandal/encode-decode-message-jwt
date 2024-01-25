"""
Module responsibility:
"""

# pylint:disable=E0611
# pylint:disable=E0401
# pylint:disable = C0116

from typing import Any

import os
import argparse
import json
import jwt

from shared.feature_load_pem_files.feature import load_private_pem_file
from shared.feature_get_path_pem_file.feature import get_path_pem_file


def load_message(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_message(path: str, message: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(message)


def message_encode(arguments: argparse.Namespace) -> None:
    # pylint:disable = W0613

    path_payload_json = os.getenv("MESSAGE_JSON_FILE_PATH")
    path_jwt = os.getenv("JWT_FILE_PATH")
    path_pem_private = get_path_pem_file("PRIVATE_PEM_FILE_NAME")
    algorithm = os.getenv("ALGORITHM")

    message = load_message(path=path_payload_json)  # type: ignore
    private_pem = load_private_pem_file(path=path_pem_private)
    encoded_jwt = jwt.encode(message, private_pem, algorithm=algorithm)
    write_message(path=path_jwt, message=encoded_jwt)  # type: ignore
    print(encoded_jwt)
