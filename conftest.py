from datetime import datetime
import pytest
from py.xml import html

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login():
    return LoginPage()


@pytest.fixture
def inventory():
    return InventoryPage()


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
