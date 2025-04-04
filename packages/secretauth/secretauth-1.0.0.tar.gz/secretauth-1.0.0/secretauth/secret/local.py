"""secretauth using environment variable"""
import os
from secretauth.exception.custom import EnvironmentVariableNotFoundError


def get_secret_from_env(env_var: str) -> str:
    """Retrieves a sensitive environment variable or raises descriptive exception.

    This function securely fetches environment variables containing secrets/credentials.
    It provides explicit error messaging to help troubleshoot missing configurations.

    Args:
        env_var: Name of the environment variable to retrieve (case-sensitive).
            Example: "API_SECRET_KEY".

    Returns:
        The string value of the environment variable if found and non-empty.

    Raises:
        EnvironmentVariableNotFoundError: If the requested environment variable is:
            - Not set in the environment
            - Set to an empty string
        ValueError: If env_var argument is empty or not a string

    Example:
        >>> os.environ["TEST_KEY"] = "secret123"
        >>> get_secret_from_env("TEST_KEY")
        'secret123'

        >>> get_secret_from_env("MISSING_KEY")
        EnvironmentVariableNotFoundError: Required environment variable 'MISSING_KEY' not found...
    """
    if not isinstance(env_var, str) or not env_var.strip():
        raise ValueError(
            "Environment variable name must be a non-empty string")

    value = os.getenv(env_var)
    if value is None or value == "":
        raise EnvironmentVariableNotFoundError(env_var)
    return value
