from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    base_url = "https://gitflic.ru"

    # Данные первого пользователя
    user1_cookie = {
        "name": "SESSION",
        "value": "MzEwNTllZDItZDRkZi00NmY1LWI5MGUtNTA3Y2Q3YWQwM2Yy",
        "path": "/",
    }
    user1_profile_url = "https://gitflic.ruuser/alexroi"

    # Данные второго пользователя
    user2_cookie = {
        "name": "SESSION",
        "value": "YzQzODlhZGEtNGViNC00MjFlLWIzMWItMDU2YWQzZWI5MWMz",
        "path": "/",
    }
    user2_profile_url = "https://gitflic.ruuser/lihanova-nadejda"

    try:
        # 1. Откройте страницу https://gitflic.ru
        driver.get(base_url)

        # 2. Установите cookie пользователя 1 и обновите страницу
        driver.delete_all_cookies()
        driver.add_cookie(user1_cookie)
        driver.refresh()

        # Проверяем, что кука применилась до перехода на страницу пользователя
        wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "a[href*='/auth/signup']")
            )
        )

        # 3. Перейдите на страницу пользователя 1 и сохраните URL
        driver.get(user1_profile_url)
        wait.until(EC.url_to_be(user1_profile_url))
        url_user_1 = driver.current_url

        # 4. Разлогиньтесь (очистите куки)
        driver.delete_all_cookies()
        driver.get(base_url)

        # 5. Установите cookie пользователя 2 и обновите страницу
        driver.add_cookie(user2_cookie)
        driver.refresh()

        # Проверяем, что кука применилась до перехода на страницу пользователя
        wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "a[href*='/auth/signup']")
            )
        )

        # 6. Перейдите на страницу пользователя 2 и сохраните URL
        driver.get(user2_profile_url)
        wait.until(EC.url_to_be(user2_profile_url))
        url_user_2 = driver.current_url

        # 7. Проверьте, что URL для пользователя 1 и пользователя 2 различаются
        assert url_user_1 != url_user_2, (
            f"URL пользователей совпадают: {url_user_1}"
        )

    finally:
        driver.quit()
