"""
Module responsibility:

Procedure Mapping: It maps the services codes to their respective
functions and returns them in a structured format.
"""

# pylint:disable=E0401

import argparse

from typing import Callable

from feature_create_pem_files.feature import create_pem_files
from feature_read_pem_files.feature import read_pem_files

# from feature_message_encode_decode.feature import message_encode
# from feature_message_encode_decode.feature import message_decode


def get_services_dictionary() -> dict[str, Callable[[argparse.Namespace], None]]:
    """
    Defines a dictionary with the services necessary for the script.

    return:
        dict: dictionary object that contains the available services used by this script.
    """

    services = {
        "create_pem": create_pem_files,
        "read_pem": read_pem_files,
        # "message_encode": message_encode,
        # "message_decode": message_decode,
    }

    return services
