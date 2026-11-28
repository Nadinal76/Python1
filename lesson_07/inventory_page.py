from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.container = (By.ID, "inventory_container")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def wait_for_load(self):
        self.wait.until(EC.visibility_of_element_located(self.container))

    def add_item_to_cart(self, item_id):
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
