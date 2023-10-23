import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.base_page import BaseFactory


from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    service = Service()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Remote(command_executor=os.getenv("HUB"), options=chrome_options)
    # if you want to not run on selenium grid, uncomment this and comment out above driver
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def base_factory(driver):
    return BaseFactory(driver)


@pytest.fixture
def login(base_factory):
    return LoginPage(base_factory)


@pytest.fixture
def inventory(base_factory):
    return InventoryPage(base_factory)


# Additional content for pytest results
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th('Description'))
#     cells.insert(1, html.th('Time', class_='sortable time', col='time'))
#
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))
#     cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
