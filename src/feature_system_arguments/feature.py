"""
Module responsibility:

Argument configuration: It sets up the necessary arguments for the script.

Argument parsing: It parses the arguments passed to the script and returns
them in a structured format.
"""

# pylint: disable=W0621

from typing import Callable

import argparse

from shared.feature_services_dictionary.feature import get_services_dictionary


def service_validator(service: str, services: dict[str, Callable[[str], None]]) -> str:
    """
    return:
        str: service name.
    """

    if service not in services:
        raise argparse.ArgumentTypeError(
            f"Error: The service {service} does not exist."
        )

    return service


def configuration_arguments_parser() -> argparse.ArgumentParser:
    # pylint:disable=C0116

    argument_parser = argparse.ArgumentParser()
    services = get_services_dictionary()
    service_names = ", ".join(services.keys())

    argument_parser.add_argument(
        "-s",
        "--service",
        required=True,
        type=lambda service: service_validator(service=service, services=services),
        help=f"Available services are: {service_names}",
    )

    return argument_parser


def system_arguments() -> argparse.Namespace:
    """
    return:
        argparse.Namespace: namespace containing the parsed arguments.
    """

    sys_arguments = configuration_arguments_parser()

    return sys_arguments.parse_args()
