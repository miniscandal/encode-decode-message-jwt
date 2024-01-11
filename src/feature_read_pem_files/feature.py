"""
This module defines the functions to convert
private and public keys to PEM format and read PEM files.
"""

# pylint:disable=E0401
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from shared.feature_load_pem_files.feature import load_private_pem_file
from shared.feature_load_pem_files.feature import load_public_pem_file
from shared.feature_read_environment_variables.feature import (
    read_env_var_pem_file_paths,
)


def convert_private_key_to_pem(
    private_pem: rsa.RSAPrivateKey, serialization_module: serialization
) -> str:
    """
    This function converts a private key to PEM format.

    :param private_pem: The private key to convert.
    :param serialization_module: The serialization module to use.

    :return: The private key in PEM format.
    """
    pem = private_pem.private_bytes(
        encoding=serialization_module.Encoding.PEM,
        format=serialization_module.PrivateFormat.PKCS8,
        encryption_algorithm=serialization_module.NoEncryption(),
    )

    return pem.decode("utf-8")


def convert_public_key_to_pem(public_key: rsa.RSAPublicKey) -> str:
    """
    This function converts a public key to PEM format.

    :param public_key: The public key to convert.

    :return: The public key in PEM format.
    """
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return pem.decode("utf-8")


def read_pem_files(*args) -> None:
    # pylint: disable=unused-argument
    """
    This function reads the PEM files specified in the environment
    variables and converts them to PEM format.

    :param *args: The arguments that will be passed to the function when it is called.

    """
    pem_file_paths = read_env_var_pem_file_paths()
    private_pem = load_private_pem_file(pem_file_paths["private_key"])
    public_pem = load_public_pem_file(pem_file_paths["public_key"])
    serialized_private_pem = convert_private_key_to_pem(private_pem, serialization)
    serialized_public_pem = convert_public_key_to_pem(public_pem)
    print(serialized_private_pem)
    print(serialized_public_pem)
