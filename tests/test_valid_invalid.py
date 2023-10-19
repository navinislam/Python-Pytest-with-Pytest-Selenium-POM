import pytest


def test_locked_out_user(login):
    login.visit()

    login.login_as("locked_out_user", "secret_sauce")

    assert login.is_login_error_visible()
