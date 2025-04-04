"""secretauth secret module mapper"""
from secretauth.secret.aws import get_secret_from_aws
from secretauth.secret.local import get_secret_from_env
from secretauth.secret.provider import SecretProvider

# wrap all secret provider function to one
secret_providers = {
    SecretProvider.AWS: get_secret_from_aws,
    SecretProvider.LOCAL: get_secret_from_env
}
