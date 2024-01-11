"""
This module defines the services available in this software through a service dictionary.
"""

# pylint:disable=E0401
from feature_create_pem_files.feature import create_pem_files
from feature_read_pem_files.feature import read_pem_files
from feature_message_encode_decode.feature import message_encode
from feature_message_encode_decode.feature import message_decode


def get_services_dictionary(*args) -> dict:
    """
    This function returns a dictionary that contains the services
    available in this software. Each service is a function that can be called
    with the provided arguments.

    :param *args: The arguments that will be passed to the service function when it is called.

    :return: A dictionary where the keys are the names of the services and the values
    are the corresponding functions.
    """

    services = {
        "create_pem": lambda: create_pem_files(*args),
        "read_pem": lambda: read_pem_files(*args),
        "message_encode": lambda: message_encode(*args),
        "message_decode": lambda: message_decode(*args),
    }

    return services
