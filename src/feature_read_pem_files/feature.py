"""
Module responsibility:

PEM File Reading: This module is responsible for reading RSA keys from PEM files
converting them into a serialized PEM format, and printing them.
"""

# pylint:disable=E0401
# pylint:disable=E0611
# pylint:disable=W0621
# pylint:disable = C0116

import argparse

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from shared.feature_load_pem_files.feature import load_private_pem_file
from shared.feature_load_pem_files.feature import load_public_pem_file
from shared.feature_get_path_pem_file.feature import get_path_pem_file


def convert_private_key_to_pem(rsa_private_pem: rsa.RSAPrivateKey) -> str:
    pem = rsa_private_pem.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return pem.decode("utf-8")


def convert_public_key_to_pem(public_key: rsa.RSAPublicKey) -> str:
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return pem.decode("utf-8")


def read_pem_files(arguments: argparse.Namespace) -> None:
    # pylint:disable = W0613

    path_pem_private = get_path_pem_file("PRIVATE_PEM_FILE_NAME")
    path_pem_public = get_path_pem_file("PUBLIC_PEM_FILE_NAME")
    rsa_private_pem = load_private_pem_file(path_pem_private)
    rsa_public_pem = load_public_pem_file(path_pem_public)
    serialized_private_pem = convert_private_key_to_pem(rsa_private_pem)
    serialized_public_pem = convert_public_key_to_pem(rsa_public_pem)
    print(serialized_private_pem)
    print(serialized_public_pem)
