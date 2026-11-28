from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    wait = WebDriverWait(driver, 20)
    first_name = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='first-name']")
        )
    )
    first_name.send_keys("Сергей")

    driver.find_element(
        By.CSS_SELECTOR, "input[name='last-name']"
    ).send_keys("Давыдов")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='address']"
    ).send_keys("Весенняя 2-48")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']"
    ).send_keys("test@skypro.com")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']"
    ).send_keys("+7985899991212")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='city']"
    ).send_keys("Брянск")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='country']"
    ).send_keys("Россия")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='job-position']"
    ).send_keys("QA")
    driver.find_element(
        By.CSS_SELECTOR, "input[name='company']"
    ).send_keys("SkyPro")

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    ActionChains(driver).scroll_to_element(submit_btn).perform()
    submit_btn.click()

    zip_code = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert zip_code.value_of_css_property("background-color") == (
        "rgba(248, 215, 218, 1)"
    )

    green_fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_id in green_fields:
        field_bg = driver.find_element(
            By.ID, field_id
        ).value_of_css_property("background-color")
        assert field_bg == "rgba(209, 231, 221, 1)", (
            f"Поле {field_id} не подсвечено зеленым"
        )
