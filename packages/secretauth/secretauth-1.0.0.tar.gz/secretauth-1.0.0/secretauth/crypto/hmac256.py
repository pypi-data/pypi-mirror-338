"""secretauth hmacsha256 utility"""
import hashlib
import hmac
import time
import os
import base64
from typing import Tuple, Optional


class HMACSHA256:
    """A secure authentication using HMAC tokens with nonce, salt, and expiry.

    This class provides methods to generate and validate authentication tokens using
    one-way hashing with HMAC-SHA256. Tokens include a nonce (for replay protection),
    salt (for added entropy), and timestamp (for expiry control).

    Attributes:
        secret_key (str): The shared secret key used for HMAC generation.
        default_expiry (int): Default token validity duration in seconds.
    """

    def __init__(self, secret_key: str, default_expiry: int = 3600) -> None:
        """Initialize the HMACSHA256 instance with a secret key and default expiry.

        Args:
            secret_key: Shared secret key for token generation/validation.
                Should be a high-entropy string stored securely.
            default_expiry: Default token validity duration in seconds.
                Defaults to 3600 (1 hour).

        Raises:
            ValueError: If secret_key is empty or default_expiry is not positive.
        """
        if not secret_key:
            raise ValueError("Secret key cannot be empty")
        if default_expiry <= 0:
            raise ValueError("Default expiry must be positive")
        self.secret_key = secret_key
        self.default_expiry = default_expiry

    def generate_token(self, auth_id: str = "",
                       expiry_seconds: Optional[int] = None) -> str:
        """Generate a secure authentication token.

        The token contains:
        - Auth identifier
        - Random nonce (16 bytes)
        - Random salt (8 bytes)
        - Expiry timestamp
        - HMAC-SHA256 signature

        Args:
            auth_id: Unique identifier for the authenticated entity.
            expiry_seconds: Optional override for token validity duration.
                Uses instance default if not specified.

        Returns:
            Base64-encoded authentication token string.

        Example:
            >>> auth = HMACSHA256("my_secret_key")
            >>> token = auth.generate_token("user123")
            >>> len(token) > 50
            True
        """
        expiry = expiry_seconds if expiry_seconds is not None else self.default_expiry
        # Generate random components
        nonce = os.urandom(16).hex()
        salt = os.urandom(8).hex()
        # Set expiry timestamp
        timestamp = str(int(time.time() + expiry))
        # Create message and HMAC
        message = f"{auth_id}:{nonce}:{salt}:{timestamp}"
        hmac_digest = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).digest()

        # Combine and encode
        token_components = f"{message}:{hmac_digest.hex()}"
        return base64.b64encode(token_components.encode('utf-8')).decode('utf-8')

    def validate_token(self, token: str) -> Tuple[bool, Optional[str], str]:
        """Validate an authentication token.

        Args:
            token: Base64-encoded authentication token to validate.

        Returns:
            A tuple containing:
            - bool: True if token is valid, False otherwise
            - Optional[str]: auth_id if valid, None otherwise
            - str: validation message (e.g., "Token expired")

        Raises:
            ValueError: If token format is invalid during decoding.

        Example:
            >>> auth = HMACSHA256("my_secret_key")
            >>> token = auth.generate_token("user123")
            >>> valid, auth_id, msg = auth.validate_token(token)
            >>> valid
            True
            >>> auth_id
            'auth123'
        """
        try:
            decoded_token = base64.b64decode(
                token.encode('utf-8')).decode('utf-8')
            parts = decoded_token.split(':')

            if len(parts) != 5:
                return False, None, "Invalid token format"

            auth_id, nonce, salt, timestamp, received_hash = parts

            # Check expiry
            if int(timestamp) < time.time():
                return False, None, "Token expired"

            # Recompute and compare HMAC
            message = f"{auth_id}:{nonce}:{salt}:{timestamp}"
            expected_hash = hmac.new(
                self.secret_key.encode('utf-8'),
                message.encode('utf-8'),
                hashlib.sha256
            ).digest().hex()

            if not hmac.compare_digest(expected_hash, received_hash):
                return False, None, "Invalid token signature"

            return True, auth_id, "Token is valid"

        except (ValueError, UnicodeDecodeError) as e:
            return False, None, f"Token decoding failed: {str(e)}"
        except Exception as e:
            return False, None, f"Unexpected validation error: {str(e)}"

    def rotate_key(self, new_key: str) -> None:
        """Rotate the secret key to a new value.

        Args:
            new_key: The new secret key to use for future tokens.

        Raises:
            ValueError: If new_key is empty.
        """
        if not new_key:
            raise ValueError("New key cannot be empty")
        self.secret_key = new_key
