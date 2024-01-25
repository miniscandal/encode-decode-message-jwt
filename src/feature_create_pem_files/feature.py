"""
Module responsibility:
"""

# pylint:disable=E0401
# pylint:disable=E0611

import os
import argparse

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from shared.feature_get_path_pem_file.feature import get_path_pem_file


def generate_private_rsa_key() -> rsa.RSAPrivateKey:
    # pylint:disable = C0116

    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )

    return private_key


def generate_public_rsa_key(private_key: rsa.RSAPrivateKey) -> rsa.RSAPublicKey:
    # pylint:disable = C0116

    public_key = private_key.public_key()

    return public_key


def serialize_private_rsa_key(private_key: rsa.RSAPrivateKey) -> bytes:
    # pylint:disable = C0116

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return private_pem


def serialize_public_rsa_key(public_key: rsa.RSAPublicKey) -> bytes:
    # pylint:disable = C0116

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return public_pem


def file_write(path: str, pem: bytes) -> None:
    # pylint:disable = C0116

    try:
        with open(path, "wb") as file:
            file.write(pem)
    except IOError as exc:
        raise IOError(f"Could not write to file with path {path}") from exc


def create_pem_files(arguments: argparse.Namespace) -> None:
    # pylint:disable = C0116
    # pylint:disable = W0613

    private_key = generate_private_rsa_key()
    public_key = generate_public_rsa_key(private_key)
    private_pem = serialize_private_rsa_key(private_key)
    public_pem = serialize_public_rsa_key(public_key)

    path_pem_private = get_path_pem_file("PRIVATE_PEM_FILE_NAME")
    path_pem_public = get_path_pem_file("PUBLIC_PEM_FILE_NAME")
    file_write(path_pem_private, private_pem)
    file_write(path_pem_public, public_pem)
    directory_path = os.getenv("DIRECTORY_PATH_PEM_FILE")

    message = "The pem files have been successfully saved to the path:"
    print(f"{message} \n {directory_path} \n")
    print(private_pem.decode())
    print(public_pem.decode())
