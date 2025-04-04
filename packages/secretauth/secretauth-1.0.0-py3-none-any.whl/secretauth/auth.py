"""indus-cloudauth auth module"""
from typing import Optional

from secretauth.crypto.hmac256 import HMACSHA256
from secretauth.secret import secret_providers, SecretProvider


class Auth:
    """A class supporting multiple ways to get secret key from cloud and generate token for 
    authentication based on multiple algorithms.
    """

    @staticmethod
    def use_hmac256_token(
        secret_name: str = None,
        secret_provider: SecretProvider = SecretProvider.LOCAL,
        secret_key: Optional[str] = None

    ) -> HMACSHA256:
        """Initialize the crypto instance using one of several supported methods.

        Exactly one initialization method must be provided.

        Args:
            secret_name (str): The name of secret key to be used for token generation
            secret_provider (SecretProvider): Secret provider to get secret key from (default LOCAL):
                - 'local' (LOCAL): Gets secret key from enviroment variable
                - 'aws' (AWS): Gets secret key from aws secret manager stored as plaintext
            secret_key (str):  Optional overrides the above two and directly used to generate token

        Raises:
            ValueError: If no valid secret_name provided
            TypeError: If secret provided is of wrong type
        """
        if secret_key:
            return HMACSHA256(secret_key)
        if not secret_name:
            raise ValueError(
                "Must provide the secret_name if not provided secret_key"
            )
        if secret_provider not in secret_providers:
            raise TypeError(
                "Must provide one of secret provider for secret_name: 'local', 'aws'")

        return HMACSHA256(secret_providers.get(secret_provider)(secret_name))
