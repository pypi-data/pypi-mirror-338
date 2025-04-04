"""secretauth secret providers"""
from enum import Enum

class SecretProvider(Enum):
    """Enumeration of supported secret providers."""
    LOCAL = 'local'
    AWS = 'aws'
