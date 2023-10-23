def test_standard_user(login):
    """Test standard user login"""
    login.visit()
    login.login_as("standard_user", "secret_sauce")
    assert "inventory" in login.get_current_url()


def test_locked_out_user(login):
    """Test invalid login"""
    login.visit()
    login.login_as("locked_out_user", "secret_sauce")
    assert login.is_login_error_visible()
