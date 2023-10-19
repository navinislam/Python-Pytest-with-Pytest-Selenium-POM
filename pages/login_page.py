import os

from selenium.webdriver.common.by import By

from pages.base_page import BaseFactory


class LoginPage(BaseFactory):
    def __init__(self, base_factory):
        """
        Initializes the SchedulePage object.

        Args:
            base_factory (BaseFactory): The base factory object containing the web driver.

        Returns:
            None
        """
        super().__init__(base_factory.driver)

    user_name = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    btn = (By.ID, "login-button")
    error_module = (By.CSS_SELECTOR, '.error-button')

    def login_as(self, username, password):
        self.send_keys_to_element(self.user_name, text=username)
        self.send_keys_to_element(self.password_locator, text=password)
        self.click_element(self.btn)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        """
        Retrieves the current URL from the web driver.

        Returns:
            str: The current URL.
        """
        return self.driver.current_url

    def is_login_error_visible(self):
        self.wait_for_element_present(self.error_module)
        return self.is_element_displayed(self.error_module)

    def visit(self):
        self.driver.get(os.getenv("URI"))
