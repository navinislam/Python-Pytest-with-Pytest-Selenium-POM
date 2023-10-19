import pytest


def test_remove_one_item_from_cart(inventory,login):
    login.visit()
    login.login_as("standard_user", "secret_sauce")
    inventory.add_backpack_to_cart()
    inventory.add_light_to_cart()

    inventory.remove_item_from_cart()

    assert inventory.get_items_in_cart() == "1"
