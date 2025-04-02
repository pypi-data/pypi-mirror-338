"""indus-cloudauth test module"""
import os
import time
from unittest.mock import patch, MagicMock
import pytest
from indus_cloudauth import cloud_provider, auth

# Test cases for each use case


@pytest.mark.parametrize("secretkey", [
    ("")
])
def test_auth_valuerror_keyname_not_provided(secretkey):
    """
    Test the auth keyname validation.
    """
    with pytest.raises(ValueError):
        auth.use_hmac256_token(secretkey=secretkey)


@pytest.mark.parametrize("keyname", [
    ("")
])
def test_auth_valuerror_keyname_empty(keyname):
    """
    Test the auth keyname validation.
    """
    with pytest.raises(ValueError):
        auth.use_hmac256_token(keyname=keyname)


@pytest.mark.parametrize("keyname, cloud", [
    ("mysecretkeyid", "")
])
def test_auth_typeerror_cloud_not_provided(keyname, cloud):
    """
    Test the auth cloud validation.
    """
    with pytest.raises(TypeError):
        auth.use_hmac256_token(keyname=keyname, cloud=cloud)


@pytest.mark.parametrize("secretkey", [
    ("qwertyuioA"),
    ("asdfghjklB"),
    ("zxcvbnmvC")
])
def test_auth_secrekkey(secretkey):
    """
    Test the auth token using secretkey.
    """
    _auth = auth.use_hmac256_token(secretkey=secretkey)
    token = _auth.generate_token()
    valid, auth_id, message = _auth.validate_token(token)
    assert valid is True


@pytest.fixture
def set_env_var(monkeypatch):
    def _set_env_var(key):
        value = str(os.urandom(8)) + str(hash(key))
        monkeypatch.setenv(key,  value)
    return _set_env_var


@pytest.mark.parametrize("keyname, cloud", [
    ("mysecretkeyid1", cloud_provider.LOCAL),
    ("mysecretkeyid2", cloud_provider.LOCAL)
])
def test_auth_cloud_local(set_env_var, keyname, cloud):
    """
    Test the auth token using cloud= 'local'.
    """
    set_env_var(keyname)
    _auth = auth.use_hmac256_token(keyname=keyname, cloud=cloud)
    token = _auth.generate_token()
    valid, auth_id, message = _auth.validate_token(token)
    assert valid is True


@pytest.mark.parametrize("secretkey, authid, expiry", [
    (str(os.urandom(8)), "auth1", 2),
    (str(os.urandom(8)), "auth2", 4)
])
def test_auth_expiry(secretkey, authid, expiry):
    """
    Test the auth token using authid and expiry.
    """
    _auth = auth.use_hmac256_token(secretkey=secretkey)
    token = _auth.generate_token(auth_id=authid, expiry_seconds=expiry)
    valid, auth_id, message = _auth.validate_token(token)
    assert valid is True
    assert auth_id == authid
    time.sleep(expiry)
    valid, auth_id, message = _auth.validate_token(token)
    assert valid is False
    assert auth_id is None


@pytest.mark.parametrize("keyname, cloud", [
    ("dev/beta2/indus-clouthauth-secret", cloud_provider.AWS)
])
def test_auth_cloud_aws(keyname, cloud):
    """
    Test the auth token using cloud= 'aws'.
    """
    mock_get_secret = MagicMock(return_value=str(os.urandom(8)))
    secret_provider = {cloud_provider.AWS: mock_get_secret}
    with patch.dict("indus_cloudauth.cloud.secret_provider", secret_provider, True):
        _auth = auth.use_hmac256_token(keyname=keyname, cloud=cloud)
        token = _auth.generate_token()
        valid, auth_id, message = _auth.validate_token(token)
        assert valid is True
