def test_add_one_item_to_cart(inventory, login):
    """Add one item to cart and check value"""
    login.visit()
    login.login_as("standard_user", "secret_sauce")
    inventory.add_backpack_to_cart()
    assert inventory.get_items_in_cart() == "1"


def test_add_two_items_to_cart(login, inventory):
    """Add two items to cart and check value"""
    login.visit()
    login.login_as("standard_user", "secret_sauce")
    inventory.add_backpack_to_cart()
    inventory.add_light_to_cart()
    assert inventory.get_items_in_cart() == "2"


def test_remove_one_item_from_cart(inventory, login):
    """Add items to cart,remove them and check value"""

    login.visit()
    login.login_as("standard_user", "secret_sauce")
    inventory.add_backpack_to_cart()
    inventory.add_light_to_cart()
    inventory.remove_item_from_cart()
    assert inventory.get_items_in_cart() == "1"
