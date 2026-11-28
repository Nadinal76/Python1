from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".inventory_item_name")

    def get_cart_items(self):
        return self.cart_items.all_text_contents()

    def click_checkout(self):
        self.checkout_button.click()
