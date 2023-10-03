# pylint: disable=R0904
# pylint: disable=W0614
import logging
import os
import sys
import time
from typing import Any

import structlog
# from PageObjectLibrary import PageObject
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseFactory(object):
    
    def __init__(self ):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        self.driver = driver

    def open(self, path):
        self.driver.get(path)

    def get_date_time(self):
        """ Static Method: get_date_time """
        timestamp = time.strftime("%m%d%Y%H%M%S")
        return timestamp

    def initialize_logging(self):
        """Initialize logging configuration. set LOG_MODE=LOCAL to get readable console logs or JSON to get json logs"""

        if structlog.is_configured():
            return
        handler = logging.StreamHandler(sys.stdout)
        root_logger = logging.getLogger()
        root_logger.addHandler(handler)
        root_logger.setLevel(logging.INFO)
        chain = [
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
        ]

        # defaults to JSON
        if os.getenv("LOG_MODE", "JSON") == "LOCAL":
            chain.append(structlog.dev.ConsoleRenderer())
        else:
            chain.append(structlog.processors.JSONRenderer())

        structlog.configure_once(
            processors=chain,  # type: ignore
            context_class=dict,
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )

    def get_logger(self, name: str) -> Any:
        """Initializes a logging and returns a logger with given name.

        Args:
          name: name of the logger

        Returns: structlog.BoundLogger
        """
        self.initialize_logging()
        return structlog.get_logger(name)

    def wait_for_element_present(self, element, timeout=10):

        try:
            WebDriverWait(self.driver, timeout=timeout).until(EC.presence_of_element_located(element))
            return True
        except Exception as error:
            screenshot = "element_not_found_" + self.get_date_time() + ".png"
            self.driver.save_screenshot(screenshot)
            raise Exception("Element not found: " + str(element))

    def wait_for_element_visible(self, element, timeout=10):

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
            return True
        except Exception as error:
            screenshot = "element_not_visible_" + self.get_date_time() + ".png"
            self.driver.save_screenshot(screenshot)
            raise Exception("Element not visible: " + str(element))

    def is_element_present(self, locator=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        elements = None

        logger = self.get_logger("get_pipeline_info")
        if locator:  # This means if locator is not empty
            elements = self.driver.find_elements(*locator)
        if len(elements) > 0:
            logger.info("Found locator ", locator_name=locator)
            return True
        else:
            logger.info("Element not present with locator: ", locator_name=locator)
            return False

    def is_element_displayed(self, locator=None, element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_displayed = False
        logger = self.get_logger("get_pipeline_info")
        try:
            if locator:  # This means if locator is not empty
                element = self.driver.find_element(*locator)
            if element is not None:
                is_displayed = element.is_displayed()
                logger.info("Element is displayed", element=element)
            else:
                logger.info("Element not displayed", element=element)
            return is_displayed
        except:
            print("Element not found")
            return False

    def wait_for_element_clickable(self, locator=None, timeout=10):
        """ Waits for element to be clickable """
        logger = self.get_logger("wait for element clickable")

        try:
            logger.info("Waiting for element to be clickable", element=locator)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            logger.info("Element is clickable", element=locator)
            return True
        except Exception as error:
            logger.info("Element not clickable", element=locator)
            screenshot = "element_not_clickable_" + self.get_date_time() + ".png"
            self.driver.save_screenshot(screenshot)
            raise Exception("Element not clickable: " + str(locator))

    def wait_for_text_to_be_present(self, locator=None,  text=None, timeout=10 ):
        """ Wait for element text to be changed"""
        logger = self.get_logger("wait for text to be present")

        try:
            logger.info("Waiting for text to be present", element=locator)
            WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            logger.info("Text is displayed", element=locator)
            return True
        except Exception as error:
            logger.info("Text is not present", element=locator)
            screenshot = "text_is_not_displayed_" + self.get_date_time() + ".png"
            self.driver.save_screenshot(screenshot)
            raise Exception("Text is not present: " + str(locator))

    def click_element(self, locator, timeout=10):
        """ Waits for element to be clickable and clicks element"""
        logger = self.get_logger("click_element")
        self.wait_for_element_clickable(locator, timeout=timeout)
        logger.info("Clicking element", element=locator)
        self.driver.find_element(*locator).click()
        logger.info("Element clicked", element=locator)

    def click_element_and_hold(self, locator, timeout=10):
        """ Waits for element to be clickable and clicks element"""
        logger = self.get_logger("click_element")
        # self.wait_for_element_clickable(locator, timeout=timeout)
        logger.info("Clicking element", element=locator)
        self.driver.find_element(*locator).click()
        logger.info("Element clicked", element=locator)
    def send_keys_to_element(self, locator, text, timeout=10, submit=False, sensitive=False):
        """ Waits for element to be clickable and clicks element"""
        logger = self.get_logger("click_element")
        self.wait_for_element_present(element=locator, timeout=timeout)
        if not sensitive:
            logger.info(f"Sending keys {text} to element", element=locator)
        self.driver.find_element(*locator).send_keys(text)
        if not sensitive:
            logger.info(f"Sent {text} to element", element=locator)
        if submit is True:
            self.driver.find_element(*locator).submit()

    def get_text_from_element(self, locator, timeout=10):
        logger = self.get_logger("get_text")
        self.wait_for_element_present(locator, timeout=timeout)
        text = self.driver.find_element(*locator).text
        logger.info(f"Getting {text} as text from element", element=locator)
        return text

    def get_attribute_value(self, locator, timeout=10):
        logger = self.get_logger("get_text")
        self.wait_for_element_present(locator, timeout=timeout)
        text = (self.driver.find_element(*locator)).get_attribute("value")
        logger.info(f"Getting {text} as text from element", element=locator)
        return text

    def get_attribute_size(self, locator, timeout=10):
        logger = self.get_logger("get_size")
        self.wait_for_element_present(locator, timeout=timeout)
        width = (self.driver.find_element(*locator)).get_attribute("width")
        logger.info(f"Getting {width} as width for the element", element=locator)
        return width

    def clear_element_text(self, locator,  timeout=10):
        """ Waits for element to be present and clear"""
        logger = self.get_logger("clear_text")
        self.wait_for_element_present(locator, timeout=timeout)
        self.driver.find_element(*locator).click()
        text = (self.driver.find_element(*locator)).get_attribute("value")
        if text != '':
            i = 0
            while i <= len(text):
                self.driver.find_element(*locator).send_keys(Keys.BACK_SPACE)
                i += 1
        logger.info(f"Setting {' '} as text from element", element=locator)

    def is_element_enabled(self, locator=None, element=None):
        """
        NEW METHOD
        Check if element is enabled
        Either provide element or a combination of locator and locatorType
        """
        is_enabled = False
        logger = self.get_logger("get_pipeline_info")
        try:
            if locator:  # This means if locator is not empty
                element = self.driver.find_element(*locator)
            if element is not None:
                is_enabled = element.is_enabled()
                logger.info("Element is enabled", element=element)
            else:
                logger.info("Element not enabled", element=element)
            return is_enabled
        except:
            print("Element not found")
            return False

    def quit_driver(self):
        self.driver.quit()

    def generate_screenshot(self, error_file_name):
        """ Method: generate_screenshot
        :type error_file_name: string
        :param error_file_name: this is the file name
         """
        screenshot = f"screenshots/{error_file_name}_{self.get_date_time()}.png"
        self.driver.save_screenshot(screenshot)
        print("Generated screenshot: {}".format(screenshot))