"""indus-cloudauth cloud providers"""
from enum import Enum

class CloudProvider(Enum):
    """Enumeration of supported cloud providers."""
    LOCAL = 'local'
    AWS = 'aws'
