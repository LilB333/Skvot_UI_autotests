import allure
import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage

url_product_1 = 'https://www.skvot.com/catalog/skateboarding/skate-deck-skvot-knight-CB-00020952'
url_product_2 = 'https://www.skvot.com/catalog/clothing/shirts-c1rca-victory-tee-green-bottle-CB-00013927'
url = "https://www.skvot.com/"

@pytest.mark.run(order=4)
class TestAddProductToCart:
    @allure.description("Test add product to cart")
    def test_add_product_to_cart(self, set_up):
        driver = set_up(url=url_product_1)

        cart_title = 'Моя корзина (1)'
        cart_item = """Дека Для Скейта СКВОТ Knight
5 900 ₽
Удалить
Размер: 8.64"""
        cart_total_sum = '5 900 ₽'

        product_page = ProductPage(driver)

        product_page.close_modal_window()
        product_page.add_product_to_cart()
        product_page.check_product_info_from_cart(cart_title, cart_item, cart_total_sum)

        # Очищаем корзину для следующего теста
        product_page.clean_cart()

        driver.quit()

    @allure.description("Test add product to cart by filters")
    def test_add_product_to_cart_by_filters(self, set_up):
        driver = set_up(url=url)

        main_page = MainPage(driver)
        main_page.close_modal_window()
        main_page.add_product_1_to_cart()

        # Очищаем корзину для следующего теста
        main_page.clean_cart()

        driver.quit()


    @allure.description("Test add multiple product to cart")
    def test_add_multiple_product_to_cart(self, set_up):
        driver = set_up(url=url_product_1)

        cart_title = 'Моя корзина (2)'
        cart_item = """Дека Для Скейта СКВОТ Knight
5 900 ₽
Удалить
Размер: 8.64
Футболка C1RCA VICTORY TEE GREEN BOTTLE
3 610 ₽
1 950 ₽
Удалить
Размер: M"""
        cart_total_sum = '7 850₽'

        product_page = ProductPage(driver)
        product_page.close_modal_window()
        product_page.add_multiple_product_to_cart(url=url_product_2)
        product_page.check_product_info_from_cart(cart_title, cart_item, cart_total_sum)

        # Очищаем корзину для следующего теста
        product_page.clean_cart()

        driver.quit()

