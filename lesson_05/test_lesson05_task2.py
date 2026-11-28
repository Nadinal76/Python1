from urllib.parse import urlunparse
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    components = (
        "https", "httpbin.qa-territory.online", "/forms/post", "", "", ""
    )
    target_url = urlunparse(components)

    driver.get(target_url)

    original_url = driver.current_url + "?original"

    driver.find_element(By.NAME, "custname").send_keys("Надежда")
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    assert driver.current_url != original_url
    driver.quit()
