import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument(
        "--dns-over-https-templates=https://dns.google"
    )
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
