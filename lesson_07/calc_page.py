from playwright.sync_api import Page, expect


class CalcPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_input = page.locator("#delay")
        self.screen = page.locator(".screen")

    def open(self):
        self.page.goto(self.url)

    def set_delay(self, delay_value):
        self.delay_input.fill(str(delay_value))

    def click_button(self, button_text):
        self.page.locator(f"//span[text()='{button_text}']").click()

    def get_result(self, expected_result, timeout=50000):
        expect(self.screen).to_have_text(
            str(expected_result), timeout=timeout
        )
        return self.screen.text_content()
