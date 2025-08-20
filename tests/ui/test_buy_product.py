import allure
import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage

url_product = 'https://www.skvot.com/catalog/skateboarding/skate-deck-skvot-knight-CB-00020952'
url_cart = 'https://www.skvot.com/cart'

@pytest.mark.run(order=7)
class TestBuyProduct:
    @allure.description("Test buy product")
    def test_buy_product(self, set_up):
        driver = set_up(url=url_product)

    # ДАННЫЕ ДЛЯ ПРОВЕРКИ СТРАНИЦЫ ТОВАРА
        product_head_title = 'Дека для скейта СКВОТ Knight'
        product_price = '5 900 ₽'
        product_size = '8.64 10'
        product_description = """Описание товара:
Встречайте новую коллекцию дек СКВОТ 2025 — мы реально постарались, чтобы порадовать вас мощными обновлениями. Огромный выбор размеров: в коллекции представлены как всеми любимые «рыбы», так и скейтборды для самых маленьких райдеров. Деки с High конкейвом и есть деки с Twin формой! А вишенка на торте — данные деки с технологией Impact Light!
Сделаны на DSM — это одна из топовых фабрик мира по производству скейтбордов. Материалы на высоком уровне: используется прочный, жёсткий американский клён, с отличным щелчком и выносливостью. То, что нужно для серьёзного катания!
Размеры:

8.125" x 31.7"; WB: 14.125" IMPACT LIGHT
8.25" x 31.7"; WB: 14.125" IMPACT LIGHT
8.375" x 31.875"; WB: 14.25" IMPACT LIGHT
Конкейв: HIGH

8.636" х 30.4"; WB: 14.25" HIGH concave
10.0" х 31.61"; WB: 14.5" или 15" MEDIUM Concave
IMPACT LIGHT — деки с продольной вставкой карбона сверху доски, что делает её очень крепкой! Имеет жёсткую конструкцию; может долго сохранять хороший щелчок, а также, имеет изначально более мощный щелчок!"""

    # ДАННЫЕ ДЛЯ ПРОВЕРКИ ДОБАВЛЕНИЯ ТОВАРА В КОРЗИНУ
        cart_title = 'Моя корзина (1)'
        cart_item = """Дека Для Скейта СКВОТ Knight
5 900 ₽
Удалить
Размер: 8.64"""
        cart_total_sum = '5 900 ₽'

    # ДАННЫЕ ДЛЯ ПРОВЕРКИ КОРЗИНЫ
        # n - порядковый номер товара в корзине
        n = 1
        product_cart_info = """Дека для скейта СКВОТ Knight
Размер: 8.64
Наличие:
- СПб. Петроградская, ст. м. «Петроградская», ул. Ленина, д. 16
- СПб. Садовая, ст. м. «Садовая», ул. Садовая, д. 28/30
- Пермь, ул. Революции, д. 22
- Нижний Новгород, ст. м. «Горьковская», ул. Белинского, д. 38
- СПб. ТРК «Европолис», ст. м. «Лесная», Полюстровский проспект, д. 80/84, пом. D33, 3 этаж. ТРК «Европолис»
- Мск. Парк Победы, ст. м. «Парк Победы», ул. Генерала Ермолова, д. 6
- Мск. ТРЦ «Хорошо», ст. м. «Полежаевская», Хорошёвское шоссе, д. 27. ТРЦ «Хорошо»
- Мск. Таганская, ст. м. «Таганская», ул. Большие Каменщики, д. 15
- Тюмень, ул. Дзержинского, д. 15
- СПб. Московская, ст. м. «Московская», Московский проспект, д. 183-185, лит A (вход с Московского пр-та)
- Красноярск, пр. Мира, д. 19, к. 1
- Интернет магазин
5 900 ₽
1
5 900 ₽
Удалить"""
        total_sum = '5 900'

    # ДАННЫЕ ДЛЯ ВХОДА В АККАУНТ
        email = 'cope80449@cancer-treatment.xyz'
        password = 'test_create_user1'

    # ДАННЫЕ ДЛЯ ОТПРАВКИ ТОВАРА
        city = 'спб'
        address_zip = '453129'
        address_street = 'Petrogradskaya'
        address_street_number = '17'
        address_building = '2'
        address_apartment = '24'

        product_page = ProductPage(driver)
        product_page.close_modal_window()
        # Проверяем описание товара
        product_page.check_product_page(product_head_title, product_price, product_size, product_description)
        # Добавляем товары в корзину
        product_page.add_product_to_cart()
        # Проверяем информацию о товаре в корзине
        product_page.check_product_info_from_cart(cart_title, cart_item, cart_total_sum)
        # Проверяем информацию о товаре в корзине
        driver.get(url_cart)
        cart_page = CartPage(driver)
        cart_page.check_product_info(product_cart_info, n)
        cart_page.check_total_cart_sum(total_sum)
        # Входим в аккаунт
        cart_page.login(email, password)
        # Заполняем информацию для отправки
        cart_page.fill_shipping_info(city, address_zip, address_street, address_street_number, address_building, address_apartment)
        # Очищаем корзину
        cart_page.clean_cart()

        driver.quit()
