

def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    browser.get(link)
    browser.implicitly_wait(10)

    assert len(browser.find_elements_by_css_selector("#add_to_basket_form"))>0, "Корзина не найдена"