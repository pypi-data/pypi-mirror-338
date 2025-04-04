"""secretauth using aws secret manager"""
import json
import boto3


def get_secret_from_aws(secret_name: str) -> str:
    """
    Retrieve a secret from AWS Secrets Manager. uses your local .aws credentials and config.

    Args:
        secret_name (str): Name or ARN of the secret.

    Returns:
        str: The value of secret name provided.

    Raises:
        ResourceNotFoundException: If the secret doesn't exist.
        AccessDeniedException: If lacking permissions.
        ClientError: For other AWS service errors.
        ValueError: If secret parsing fails.

    Examples:
        >>> secret = get_secret("prod/beta/indus-clouthauth-secret")
    """
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')

    try:
        response = client.get_secret_value(SecretId=secret_name)
        if 'SecretString' in response:
            return response['SecretString']
        else:
            raise ValueError(
                "The requested secret name was not found in aws secret manager.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse secret JSON: {e}") from e
    except client.exceptions.ResourceNotFoundException:
        raise
    except client.exceptions.AccessDeniedException:
        raise
    except Exception as e:
        raise RuntimeError(f"Unexpected error retrieving secret: {e}") from e
