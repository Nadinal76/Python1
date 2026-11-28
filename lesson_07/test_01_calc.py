from calc_page import CalcPage


def test_slow_calculator(chrome_page):
    calc_page = CalcPage(chrome_page)
    calc_page.open()
    calc_page.set_delay(45)

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result = calc_page.get_result("15", timeout=50000)
    assert result == "15"
