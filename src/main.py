"""
This module simplifies the manipulation of public and private keys
through the creation and reading of PEM files. 
In addition, it provides functionalities for encoding
messages in JSON format and decoding messages in JWT format.
"""

from feature_system_arguments.feature import system_arguments
from shared.feature_services_dictionary.feature import get_services_dictionary


def main() -> None:
    """
    Main function that handles the execution of the requested service.
    """

    arguments = system_arguments()
    services = get_services_dictionary(arguments)
    services.get(arguments.service)()


if __name__ == "__main__":
    main()
