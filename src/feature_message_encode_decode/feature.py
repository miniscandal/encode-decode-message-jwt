# """
# This module provides functions for working with messages encoded
# with JWT (JSON Web Tokens). It includes functions for loading and writing
# messages, as well as for encoding and decoding messages using JWT.
# """

# import json
# import jwt

# # pylint:disable=E0401
# from shared.feature_read_environment_variables.feature import read_env_var_algorithm
# from shared.feature_read_environment_variables.feature import read_env_var_jwt_file_path
# from shared.feature_read_environment_variables.feature import (
#     read_env_var_message_file_path,
# )
# from shared.feature_load_pem_files.feature import load_private_pem_file
# from shared.feature_load_pem_files.feature import load_public_pem_file
# from shared.feature_read_environment_variables.feature import (
#     read_env_var_pem_file_paths,
# )


# def load_message(file_path: str, is_json: bool) -> str | dict:
#     """
#     This function opens a file and reads its content.
#     If the file contains JSON data, it returns a Python dictionary.
#     Otherwise, it returns the content as a string.

#     :param file_path: The path to the file to be read.
#     :param is_json: A boolean value indicating whether the file contains JSON data.

#     :return: A dictionary if the file contains JSON data, or a string if it does not.
#     """
#     with open(file_path, "r", encoding="utf-8") as file:
#         return json.load(file) if is_json else file.read()


# def write_message(file_path: str, message: str) -> None:
#     """
#     This function writes a message to a file.

#     :param file_path: The path to the file to be written.
#     :param message: The message to be written to the file.
#     """
#     with open(file_path, "w", encoding="utf-8") as file:
#         file.write(message)


# def message_encode() -> None:
#     # pylint: disable=unused-argument
#     """
#     This function encodes a message using JWT.
#     It loads the message from a file, encodes it using a private key, and writes
#     the encoded message to another file.

#     :param *args: The arguments that will be passed to the function when it is called.
#     """
#     message = load_message(file_path=read_env_var_message_file_path(), is_json=True)
#     private_pem = load_private_pem_file(read_env_var_pem_file_paths()["private_key"])
#     encoded_jwt = jwt.encode(message, private_pem, algorithm=read_env_var_algorithm())
#     write_message(read_env_var_jwt_file_path(), encoded_jwt)
#     print(encoded_jwt)


# def message_decode() -> None:
#     # pylint: disable=unused-argument
#     """
#     This function decodes a JWT message.
#     It loads the encoded message from a file, decodes it using a public key, and
#     prints the decoded message.

#     :param *args: The arguments that will be passed to the function when it is called.
#     """
#     jwt_message = load_message(file_path=read_env_var_jwt_file_path(), is_json=False)
#     public_pem = load_public_pem_file(read_env_var_pem_file_paths()["public_key"])
#     decoded_jwt = jwt.decode(
#         jwt_message, public_pem, algorithms=[read_env_var_algorithm()]
#     )
#     print(decoded_jwt)
