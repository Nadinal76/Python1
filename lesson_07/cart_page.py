from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items(self):
        items = self.driver.find_elements(*self.cart_items)
        return [item.text for item in items]

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
