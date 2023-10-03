from time import sleep

import pytest


def test_add_one_item_to_cart(inventory, login):
    inventory.visit()
    login.visit()

    login.login_as("standard_user", "secret_sauce")

    inventory.add_item_to_cart()
    sleep(10)
    assert inventory.get_items_in_cart() == '1'

# def test_add_two_items_to_cart(inventory):
#     inventory.visit()
#
#     inventory.add_item_to_cart()
#     inventory.add_item_to_cart()
#
#     assert inventory.get_items_in_cart() == '2'