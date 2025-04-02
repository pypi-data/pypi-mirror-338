"""indus_cloudauth cloud module exports"""
from indus_cloudauth.cloud.aws import get_secret_from_aws
from indus_cloudauth.cloud.local import get_secret_from_env
from indus_cloudauth.cloud.provider import CloudProvider

# wrap all cloud provider secret function to one
secret_provider = {
    CloudProvider.AWS: get_secret_from_aws,
    CloudProvider.LOCAL: get_secret_from_env
}
