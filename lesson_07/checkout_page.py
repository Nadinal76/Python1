from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.total_label = page.locator(".summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()

    def get_total_price(self):
        total_text = self.total_label.text_content()
        return total_text.replace("Total: ", "").strip()
