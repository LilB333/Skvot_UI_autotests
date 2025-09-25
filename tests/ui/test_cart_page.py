import allure
import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage

url_product_1 = 'https://www.skvot.com/catalog/skateboarding/skate-deck-skvot-knight-CB-00020952'
url_product_2 = 'https://www.skvot.com/catalog/clothing/shirts-c1rca-victory-tee-green-bottle-CB-00013927'
url_cart = 'https://www.skvot.com/cart'

@pytest.mark.run(order=5)
class TestCartPage:
    @allure.description("Test product cart page")
    def test_product_cart_page(self, set_up):
        # n - порядковый номер товара в корзине
        n = 1
        text = """Дека для скейта СКВОТ Knight
Размер: 8.64"""
        total_sum = '5 900'

        driver = set_up(url=url_product_1)
        product_page = ProductPage(driver)

        product_page.add_product_to_cart()

        driver.get(url_cart)
        cart_page = CartPage(driver)
        cart_page.check_product_info(text, n)
        cart_page.check_total_cart_sum(total_sum)

        # Очищаем корзину для следующего теста
        cart_page.clean_cart()

        driver.quit()

    @allure.description("Test multiple product cart page")
    def test_multiple_product_cart_page(self, set_up):
        # product_index - порядковый номер товара в корзине
        product_index = {
            'first': 1,
            'second': 2,
        }
        product_description = {'first_product_description': """Дека для скейта СКВОТ Knight
Размер: 8.64""",
        'second_product_description': """Футболка C1RCA VICTORY TEE GREEN BOTTLE
Размер: M
Наличие:
- СПб. Петроградская, ст. м. «Петроградская», ул. Ленина, д. 16
- Тюмень, ул. Дзержинского, д. 15
- Екатеринбург, ст.м. «Площадь 1905 года», ул. Малышева, д. 42
- Красноярск, пр. Мира, д. 19, к. 1
- Интернет магазин
1 950 ₽
1
1 950 ₽
Удалить"""}
        total_sum = '7 850'

        driver = set_up(url=url_product_1)
        product_page = ProductPage(driver)

        product_page.add_multiple_product_to_cart(url=url_product_2)

        driver.get(url_cart)
        cart_page = CartPage(driver)
        # Проверяем товар с порядковым номером 1
        cart_page.check_product_info(product_description['first_product_description'], product_index['first'])
        # Проверяем товар с порядковым номером 2
        cart_page.check_product_info(product_description['second_product_description'], product_index['second'])

        cart_page.check_total_cart_sum(total_sum)

        # Очищаем корзину для следующего теста
        cart_page.clean_cart()

        driver.quit()
