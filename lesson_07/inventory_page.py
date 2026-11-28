from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator("[data-test='inventory-container']")
        self.cart_link = page.locator(".shopping_cart_link")

    def wait_for_load(self):
        expect(self.container).to_be_visible()

    def add_item_to_cart(self, item_id):
        self.page.locator(f"#{item_id}").click()

    def go_to_cart(self):
        self.cart_link.click()
