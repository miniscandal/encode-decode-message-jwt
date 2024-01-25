"""
Module Responsibility:

RSA Key management: Simplifies the handling of public and private keys with methods
for the creation and reading of PEM files.

Message encoding and decoding: Provides functionalities for encoding messages
in JSON format and decoding messages in JWT format.
"""

# pylint:disable=C0116

from dotenv import load_dotenv
from feature_system_arguments.feature import system_arguments
from shared.feature_services_dictionary.feature import get_services_dictionary


def main() -> None:
    load_dotenv()
    arguments = system_arguments()
    services = get_services_dictionary()
    service = services.get(arguments.service)
    service(arguments=arguments)  # type: ignore


if __name__ == "__main__":
    main()
