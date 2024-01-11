"""
This module provides functionalities to load private and public keys from PEM files.
"""

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


def load_private_pem_file(path: str) -> rsa.RSAPrivateKey:
    """
    This function loads a private key from a PEM file.

    :param path: The path to the PEM file.

    :return: The private key.
    """

    private_key = None
    with open(path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(), password=None, backend=default_backend()
        )

    return private_key


def load_public_pem_file(path: str) -> rsa.RSAPublicKey:
    """
    This function loads a public key from a PEM file.

    :param path: The path to the PEM file.

    :return: The public key.
    """

    public_key = None
    with open(path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(), backend=default_backend()
        )

    return public_key
