import os
from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BaseFactory


class InventoryPage(BaseFactory):
    def __init__(self, base_factory):
        """
        Initializes the SchedulePage object.

        Args:
            base_factory (BaseFactory): The base factory object containing the web driver.

        Returns:
            None
        """
        super().__init__(base_factory.driver)

    add_backpack_to_cart_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    add_light_to_cart_btn = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
    remove_btn = (By.CSS_SELECTOR, ".btn_secondary")
    cart_items = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.wait_for_element_present(self.add_backpack_to_cart_btn)
        self.click_element(self.add_backpack_to_cart_btn)

    def add_light_to_cart(self):
        self.wait_for_element_present(self.add_light_to_cart_btn)
        self.click_element(self.add_light_to_cart_btn)

    def remove_item_from_cart(self):
        self.click_element(self.remove_btn)

    def get_items_in_cart(self):
        return self.get_text_from_element(self.cart_items)

    def get_current_url(self):
        return self.driver.current_url()

    def visit(self):
        self.driver.get(os.getenv("URI"))
