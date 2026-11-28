from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_saucedemo_checkout(firefox_page):
    login_page = LoginPage(firefox_page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(firefox_page)
    inventory_page.wait_for_load()
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
    inventory_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")
    inventory_page.go_to_cart()

    cart_page = CartPage(firefox_page)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(firefox_page)
    checkout_page.fill_form("Сергей", "Давыдов", "632022")
    checkout_page.click_continue()
    total_price = checkout_page.get_total_price()

    assert total_price == "$58.29", (
        f"Ожидалась сумма $58.29, но получена {total_price}"
    )
