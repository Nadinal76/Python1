import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    options = Options()
    options.page_load_strategy = "eager"
    options.add_argument(
        "--dns-over-https-templates=https://dns.google"
    )
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    parts = [
        "https:",
        "",
        "bonigarcia.dev",
        "selenium-webdriver-java",
        "slow-calculator.html",
    ]
    driver.get("/".join(parts))

    wait = WebDriverWait(driver, 15)
    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    long_wait = WebDriverWait(driver, 50)
    is_result_ready = long_wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    assert is_result_ready
    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"
