# indus-cloudauth
``indus-cloudauth`` is a secure, unified solution for generating and validating authentication tokens across multiple cloud platforms.

## Features

* Standardizes authentication with a consistent interface for token management and authentication.
* Simplifies secret key retrieval from AWS Secrets Manager. Azure Key Vault, GCP Secret Manager and more coming soon.
* Enhances security by eliminating manual credential handling.
* Provided option to encrypt more information using `auth_id` and set token expiry using `expiry_seconds`.
* Reduces boilerplate code with easy-to-use methods for token generation and validation.

## Requirements

Python 3.9+

## Usage

You can use the `indus-cloudauth` package in your Python code to generate authentication token using cloud provider of your choice for accessing the secret.

### Example 1 - using secret key stored in aws secret manager

It uses your local aws credentials and configs from `~/.aws` see [Using Boto3](https://github.com/boto/boto3). Only key stored as plaintext will work.

```python
from indus_cloudauth import cloud_provider, auth

keyname = "keyname_in_your_aws_secret_manager"
_auth = auth.use_hmac256_token(keyname=keyname, cloud=cloud_provider.AWS) # initializes the auth module
token = _auth.generate_token() # generates your token
valid, auth_id, message = _auth.validate_token(token) # validates your token

```

### Example 2 - using secret key stored in environment variable

```python
from indus_cloudauth import cloud_provider, auth

keyname = "keyname_in_your_enviroment"
_auth = auth.use_hmac256_token(keyname=keyname, cloud=cloud_provider.LOCAL) # initializes the auth module
token = _auth.generate_token() # generates your token
valid, auth_id, message = _auth.validate_token(token) # validates your token

```

### Example 3 - using secret key directly

```python
from indus_cloudauth import cloud_provider, auth

secret_key = "anysecretkeyyoucanpass"
_auth = auth.use_hmac256_token(secretkey=secretkey) # initializes the auth module
token = _auth.generate_token() # generates your token
valid, auth_id, message = _auth.validate_token(token) # validates your token

```


### Example 4 - using token expiry_time and auth_id

By default the token expiry time set to 1 hour. You can encrypt any useful information using auth_id.

```python
from indus_cloudauth import cloud_provider, auth

keyname = "keyname_in_your_enviroment"
auth_id = "userid_etc"
expiry = 60 # 1 minute
_auth = auth.use_hmac256_token(keyname=keyname, cloud=cloud_provider.LOCAL) # initializes the auth module
token = _auth.generate_token(auth_id=authid, expiry_seconds=expiry) # generates your token
valid, auth_id, message = _auth.validate_token(token) # validates your token

```





