import time

import allure
import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage

url_product_1 = 'https://www.skvot.com/catalog/skateboarding/skate-deck-skvot-knight-CB-00020952'
url_cart = 'https://www.skvot.com/cart'

@pytest.mark.run(order=6)
class TestFillShippingInfo:
    @allure.description("Test fill shipping info")
    def test_fill_shipping_info(self, set_up):
        email = 'cope80449@cancer-treatment.xyz'
        password = 'test_create_user1'
        city = 'спб'
        address_zip = '453129'
        address_street = 'Petrogradskaya'
        address_street_number = '17'
        address_building = '2'
        address_apartment = '24'

        driver = set_up(url=url_product_1)
        product_page = ProductPage(driver)

        time.sleep(3)

        product_page.close_modal_window()
        product_page.add_product_to_cart()

        cart_page = CartPage(driver)
        driver.get(url=url_cart)
        cart_page.login(email, password)
        cart_page.fill_shipping_info(city, address_zip, address_street, address_street_number, address_building, address_apartment)

        # Очищаем корзину для будущих тестов
        cart_page.clean_cart()

        driver.quit()