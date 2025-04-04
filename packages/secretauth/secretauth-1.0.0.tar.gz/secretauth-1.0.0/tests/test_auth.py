"""indus-secret_providerAuth test module"""
import os
import time
from unittest.mock import patch, MagicMock
import pytest
from secretauth import SecretProvider, Auth

# Test cases for each use case


@pytest.mark.parametrize("secret_key", [
    ("")
])
def test_auth_valuerror_secret_name_not_provided(secret_key):
    """
    Test the Auth secret_name validation.
    """
    with pytest.raises(ValueError):
        Auth.use_hmac256_token(secret_key=secret_key)


@pytest.mark.parametrize("secret_name", [
    ("")
])
def test_auth_valuerror_secret_name_empty(secret_name):
    """
    Test the Auth secret_name validation.
    """
    with pytest.raises(ValueError):
        Auth.use_hmac256_token(secret_name=secret_name)


@pytest.mark.parametrize("secret_name, secret_provider", [
    ("mysecret_keyid", "")
])
def test_auth_typeerror_secret_provider_not_provided(secret_name, secret_provider):
    """
    Test the Auth secret_provider validation.
    """
    with pytest.raises(TypeError):
        Auth.use_hmac256_token(secret_name=secret_name,
                               secret_provider=secret_provider)


@pytest.mark.parametrize("secret_key", [
    ("qwertyuioA"),
    ("asdfghjklB"),
    ("zxcvbnmvC")
])
def test_auth_secrekkey(secret_key):
    """
    Test the Auth token using secret_key.
    """
    _auth = Auth.use_hmac256_token(secret_key=secret_key)
    token = _auth.generate_token()
    valid, auth_id, msg = _auth.validate_token(token)
    assert valid is True


@pytest.fixture
def set_env_var(monkeypatch):
    """mocks enviroment variable"""
    def _set_env_var(key):
        value = str(os.urandom(8)) + str(hash(key))
        monkeypatch.setenv(key,  value)
    return _set_env_var


@pytest.mark.parametrize("secret_name, secret_provider", [
    ("mysecret_name1", SecretProvider.LOCAL),
    ("mysecret_name2", SecretProvider.LOCAL)
])
def test_auth_secret_provider_local(set_env_var, secret_name, secret_provider):
    """
    Test the Auth token using secret_provider= 'local'.
    """
    set_env_var(secret_name)
    _auth = Auth.use_hmac256_token(
        secret_name=secret_name, secret_provider=secret_provider)
    token = _auth.generate_token()
    valid, auth_id, msg = _auth.validate_token(token)
    assert valid is True


@pytest.mark.parametrize("secret_key, authid, expiry", [
    (str(os.urandom(8)), "auth1", 2),
    (str(os.urandom(8)), "auth2", 4)
])
def test_auth_expiry(secret_key, authid, expiry):
    """
    Test the Auth token using authid and expiry.
    """
    _auth = Auth.use_hmac256_token(secret_key=secret_key)
    token = _auth.generate_token(auth_id=authid, expiry_seconds=expiry)
    valid, auth_id, msg = _auth.validate_token(token)
    assert valid is True
    assert auth_id == authid
    time.sleep(expiry)
    valid, auth_id, msg = _auth.validate_token(token)
    assert valid is False
    assert auth_id is None


@pytest.mark.parametrize("secret_name, secret_provider", [
    ("dev/beta2/indus-clouthAuth-secret", SecretProvider.AWS)
])
def test_auth_secret_provider_aws(secret_name, secret_provider):
    """
    Test the Auth token using secret_provider= 'aws'.
    """
    mock_get_secret = MagicMock(return_value=str(os.urandom(8)))
    secret_providers = {SecretProvider.AWS: mock_get_secret}
    with patch.dict("secretauth.secret.secret_providers", secret_providers, True):
        _auth = Auth.use_hmac256_token(
            secret_name=secret_name, secret_provider=secret_provider)
        token = _auth.generate_token()
        valid, auth_id, msg = _auth.validate_token(token)
        assert valid is True
