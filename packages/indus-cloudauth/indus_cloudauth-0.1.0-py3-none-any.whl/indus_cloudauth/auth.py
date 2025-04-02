"""indus-cloudauth auth module"""
from typing import Optional

from indus_cloudauth.crypto.hmac256 import HMACSHA256
from indus_cloudauth.cloud.provider import CloudProvider
from indus_cloudauth.cloud import secret_provider


class Auth:
    """A class supporting multiple ways to get secret key from cloud and generate token for 
    authentication based on multiple algorithms.
    """

    @staticmethod
    def use_hmac256_token(
        keyname: str = None,
        cloud: CloudProvider = CloudProvider.LOCAL,
        secretkey: Optional[str] = None

    ) -> HMACSHA256:
        """Initialize the crypto instance using one of several supported methods.

        Exactly one initialization method must be provided.

        Args:
            keyname (str): The name of secret key to be used for token generation
            cloud (CloudProvider): Cloud provider to get secret key from securely (default LOCAL):
                - LOCAL: Gets secret key from enviroment variable
            secretkey (str):  Optional overrides the above two and directly used to generate token

        Raises:
            ValueError: If no valid secret_keyname provided
            TypeError: If provided cloud is of wrong type
        """
        if secretkey:
            return HMACSHA256(secretkey)
        if not keyname:
            raise ValueError(
                "Must provide the keyname if not provided secretkey"
            )
        if cloud not in secret_provider:
            print(secret_provider)
            raise TypeError("Must provide one of cloud provider for keyname: 'local', 'aws'")

        return HMACSHA256(secret_provider.get(cloud)(keyname))
