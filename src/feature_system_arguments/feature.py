"""
This module defines the validation and configuration functions for the system arguments.
"""

# pylint: disable=redefined-outer-name

import argparse

from shared.feature_services_dictionary.feature import get_services_dictionary


def service_validator(service: str, services: dict, argparse: argparse) -> str:
    """
    This function validates if the provided service exists in the services dictionary.

    :param service: The name of the service to validate.
    :param services: The dictionary of available services.
    :param argparse: The argparse module to handle argument errors.

    :return: The name of the service if it is valid.
    """
    if service not in services:
        raise argparse.ArgumentTypeError(
            f"Error: The service {service} does not exist."
        )

    return service


def configuration_arguments_parser(
    services: dict, argparse: argparse
) -> argparse.ArgumentParser:
    """
    This function sets up the system argument parser.

    :param services: The dictionary of available services.
    :param argparse: The argparse module to set up the argument parser.
    :param json: The json module to parse json type arguments.

    :return: The configured argument parser.
    """
    argument_parser = argparse.ArgumentParser()
    services = get_services_dictionary()
    service_names = ", ".join(services.keys())

    argument_parser.add_argument(
        "-s",
        "--service",
        required=True,
        type=lambda service: service_validator(
            service=service, services=services, argparse=argparse
        ),
        help=f"Available services are: {service_names}",
    )

    return argument_parser


def system_arguments() -> argparse.Namespace:
    """
    This function obtains and validates the system arguments.

    :return: The validated system arguments.
    """
    services = get_services_dictionary()
    sys_arguments = configuration_arguments_parser(services=services, argparse=argparse)
    parse_args = sys_arguments.parse_args()

    return parse_args
