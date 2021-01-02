from datetime import datetime
import pytest
from py.xml import html
from page_sample import InventoryPage
from page_sample import LoginPage


@pytest.fixture
def login(selenium):
    return LoginPage(selenium)


@pytest.fixture
def inventory(selenium):
    return InventoryPage(selenium)


# Additional content for pytest results
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
