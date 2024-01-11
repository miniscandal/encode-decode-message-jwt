"""
This module defines the functions to generate, serialize, and write RSA keys in PEM files.
"""

# pylint:disable=E0401
# pylint:disable=E0611
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from shared.feature_read_environment_variables.feature import read_env_var_pem_file_paths


def serialize_private_rsa_key(private_key: rsa.RSAPrivateKey) -> bytes:
    """
    This function takes a private RSA key and serializes it in PEM format.

    :param private_key: The private RSA key to be serialized.
    :return: The private RSA key serialized in PEM format.
    """
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )

    return private_pem


def serialize_public_rsa_key(public_key: rsa.RSAPublicKey) -> bytes:
    """
    This function takes a public RSA key and serializes it in PEM format.

    :param public_key: The public RSA key to be serialized.
    :return: The public RSA key serialized in PEM format.
    """
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return public_pem


def generate_private_rsa_key(
    rsa_generate_private_key: rsa.generate_private_key
) -> rsa.RSAPrivateKey:
    """
    This function generates a private RSA key.

    :param rsa_generate_private_key: The function to generate the private RSA key.
    :return: The generated private RSA key.
    """
    private_key = rsa_generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )

    return private_key


def generate_public_rsa_key(private_key: rsa.RSAPrivateKey) -> rsa.RSAPublicKey:
    """
    This function generates a public RSA key from a private RSA key.

    :param private_key: The private RSA key from which the public key will be generated.
    :return: The generated public RSA key.
    """
    public_key = private_key.public_key()

    return public_key


def write_pem_file(file_path: str, pem: bytes, key_type: str) -> None:
    """
    This function writes a PEM file to the given file path.

    :param file_path: The file path where the PEM file will be written.
    :param pem: The PEM file to be written.
    :param key_type: The type of key to be written (private or public key).
    """
    try:
        with open(file_path, "wb") as file:
            file.write(pem)
    except IOError as exc:
        raise IOError(
            f"Could not write the {key_type} to file {file_path}"
        ) from exc  

def create_pem_files(*args) -> None:
    # pylint: disable=unused-argument
    """
    This function creates PEM files for private and public RSA keys.

    :param *args: The arguments that will be passed to the key generation functions.
    """

    directory_paths = read_env_var_pem_file_paths()

    private_key = generate_private_rsa_key(rsa.generate_private_key)
    public_key = generate_public_rsa_key(private_key)
    private_pem = serialize_private_rsa_key(private_key)
    public_pem = serialize_public_rsa_key(public_key)

    write_pem_file(directory_paths["private_key"], private_pem, "private key")
    write_pem_file(directory_paths["public_key"], public_pem, "public key")

    message = "The pem files have been successfully saved to the path:"
    print(f"{message} \n {directory_paths["directory"]} \n")
    print(private_pem.decode())
    print(public_pem.decode())
