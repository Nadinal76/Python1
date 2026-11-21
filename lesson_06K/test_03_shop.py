from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_checkout():
    # Указываем путь к браузеру Firefox
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    # 1. Откройте сайт магазина в Firefox
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://saucedemo.com")

        # 2. Авторизуйтесь как пользователь standard_user
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавьте в корзину товары
        wait.until(
            EC.visibility_of_element_located((By.ID, "inventory_container"))
        )
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # 4. Перейдите в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 5. Нажмите Checkout
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # 6. Заполните форму своими данными
        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Сергей")
        driver.find_element(By.ID, "last-name").send_keys("Давыдов")
        driver.find_element(By.ID, "postal-code").send_keys("632022")

        # 7. Нажмите кнопку Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Прочитайте со страницы итоговую стоимость (Total)
        total_element = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        total_price = total_element.text.replace("Total: ", "").strip()

    finally:
        # 9. Закройте браузер
        driver.quit()

    # 10. Проверьте, что итоговая сумма равна $58.29
    assert total_price == "$58.29", (
        f"Ожидалась сумма $58.29, но получена {total_price}"
    )
