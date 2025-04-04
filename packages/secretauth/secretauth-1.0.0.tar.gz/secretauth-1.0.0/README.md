# secretauth
``secretauth`` is a secure, unified solution for generating and validating authentication tokens using secret from multiple cloud platforms.

## Features

* Standardizes authentication with a consistent interface for token management and authentication.
* Simplifies secret key retrieval from AWS Secrets Manager. Azure Key Vault, GCP Secret Manager and more coming soon.
* Enhances security by eliminating manual credential handling.
* Provided option to encrypt more information using `auth_id` and set token expiry using `expiry_seconds`.
* Reduces boilerplate code with easy-to-use methods for token generation and validation.

## Requirements

Python 3.9+

## Installallation

```console
$ pip install secretauth
```

## Usage

You can use the `secretauth` package in your Python code to generate authentication token using cloud provider of your choice for accessing the secret.

### Example 1 - using secret key stored in aws secret manager

It uses your local aws credentials and configs from `~/.aws` see [Using Boto3](https://github.com/boto/boto3). Only key stored as plaintext will work.

```python
from secretauth import SecretProvider, Auth

secret_name = "secret_name_in_your_aws_secret_manager"
_auth = Auth.use_hmac256_token(secret_name=secret_name, secret_provider=SecretProvider.AWS) # initializes the auth module
token = _auth.generate_token() # generates your token
valid, auth_id, msg = _auth.validate_token(token) # validates your token

```

### Example 2 - using secret key stored in environment variable

```python
from secretauth import SecretProvider, Auth

secret_name = "secret_name_in_your_enviroment"
_auth = Auth.use_hmac256_token(secret_name=secret_name, secret_provider=SecretProvider.LOCAL) # initializes the auth module
token = _auth.generate_token() # generates your token
valid, auth_id, msg = _auth.validate_token(token) # validates your token

```

### Example 3 - using secret key directly

```python
from secretauth import SecretProvider, Auth

secret_key = "any_secret_key_can_be_used"
_auth = Auth.use_hmac256_token(secret_key=secret_key) # initializes the auth module
token = _auth.generate_token() # generates your token
valid, auth_id, msg = _auth.validate_token(token) # validates your token

```


### Example 4 - using token expiry_seconds and auth_id

By default the token expiry time set to 1 hour. You can encrypt any useful information using auth_id.

```python
from secretauth import SecretProvider, Auth

secret_name = "secret_name_in_your_enviroment"
authid = "userid_etc"
expiry = 60 # 1 minute
_auth = Auth.use_hmac256_token(secret_name=secret_name, secret_provider=SecretProvider.LOCAL) # initializes the auth module
token = _auth.generate_token(auth_id=authid, expiry_seconds=expiry) # generates your token
valid, auth_id, msg = _auth.validate_token(token) # validates your token

```





