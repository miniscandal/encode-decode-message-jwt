'''
This module provides functionalities to read environment
variables related to PEM files, algorithm, and file paths.
'''

import os

from dotenv import load_dotenv

load_dotenv()


def read_env_var_pem_file_paths() -> dict:
    """
    This function reads the environment variables related to the paths of the PEM files.

    :return: A dictionary containing the paths of the private key, public key, and the directory.
    """
    directory_path = os.getenv("DIRECTORY_PATH_PEM_FILE")
    file_paths = {
        "private_key": f"{directory_path}\\{os.getenv("PRIVATE_PEM_FILE_NAME")}",
        "public_key": f"{directory_path}\\{os.getenv("PUBLIC_PEM_FILE_NAME")}",
        "directory": directory_path
    }

    return file_paths


def read_env_var_algorithm() -> str:
    '''
    This function reads the environment variable related to the algorithm.

    :return: The algorithm as a string.
    '''
    algorithm = os.getenv("ALGORITHM")

    return algorithm


def read_env_var_jwt_file_path() -> str:
    '''
    This function reads the environment variable related to the JWT file path.

    :return: The JWT file path as a string.
    '''
    path = os.getenv("JWT_FILE_PATH")

    return path



def read_env_var_message_file_path() -> str:
    '''
    This function reads the environment variable related to the message file path.

    :return: The message file path as a string.
    '''
    path = os.getenv("MESSAGE_FILE_PATH")

    return path
