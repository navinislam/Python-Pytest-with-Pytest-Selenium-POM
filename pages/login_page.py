from selenium.webdriver.common.by import By

from pages.base_page import BaseFactory


class LoginPage(BaseFactory):

    user_name = (By.ID, 'user-name')
    password_locator = (By.ID, 'password')
    btn = (By.ID, 'login-button')

    def login_as(self, username, password):
        self.send_keys_to_element(self.user_name, text=username)
        self.send_keys_to_element(self.password_locator, text=password)
        self.click_element(self.btn)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_header_text(self):
        return self.driver.find_element_by_id('header_container').text

    def is_login_error_visible(self):
        return self.driver.find_element_by_css_selector('.error-button').is_displayed()

    def visit(self):
        self.driver.get('https://www.saucedemo.com')