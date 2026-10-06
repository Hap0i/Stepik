import time


def test_product_page_should_have_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза 10 секунд, чтобы визуально проверить язык кнопки
    time.sleep(10)

    # Ищем кнопку добавления в корзину
    button = browser.find_element(
        "css selector", "button.btn-add-to-basket"
    )

    # Проверяем, что кнопка есть на странице
    assert button is not None, "Кнопка добавления в корзину не найдена"
