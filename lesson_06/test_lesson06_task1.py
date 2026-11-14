from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1. Откройте страницу dynamic_loading/2
        url = "https://herokuapp.com"
        driver.get(url)

        # 2. Найдите и нажмите на кнопку "Start"
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # 3. Дождитесь появления текста "Hello World!"
        wait = WebDriverWait(driver, 10)
        finish_text = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        # 4. Сделайте скриншот страницы
        driver.save_screenshot("hello_world.png")

        # 5. Проверьте, что появившийся текст равен "Hello World!"
        assert finish_text.text == "Hello World!", (
            f"Ожидался 'Hello World!', но получен '{finish_text.text}'"
        )

    finally:
        driver.quit()
