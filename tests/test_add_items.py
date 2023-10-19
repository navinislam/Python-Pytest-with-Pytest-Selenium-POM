from time import sleep

import pytest


def test_add_one_item_to_cart(inventory, login):

    login.visit()
    login.login_as("standard_user", "secret_sauce")
    inventory.add_backpack_to_cart()
    assert inventory.get_items_in_cart() == "1"


def test_add_two_items_to_cart(login, inventory):
    login.visit()
    login.login_as("standard_user", "secret_sauce")
    inventory.add_backpack_to_cart()
    inventory.add_light_to_cart()
    assert inventory.get_items_in_cart() == "2"
