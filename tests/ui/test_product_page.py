import allure
import pytest
from pages.product_page import ProductPage

url_product_1 = 'https://www.skvot.com/catalog/skateboarding/skate-deck-skvot-knight-CB-00020952'
url_product_2 = 'https://www.skvot.com/catalog/clothing/shirts-c1rca-victory-tee-green-bottle-CB-00013927'

@pytest.mark.run(order=3)
class TestProductPage:
    @allure.description("Test product page 1")
    def test_product_page_1(self, set_up):
        product_head_title = 'Дека для скейта СКВОТ Knight'
        product_price = '5 900 ₽'
        product_size = '8.64 10'
        product_description = """Встречайте новую коллекцию дек СКВОТ 2025 — мы реально постарались, чтобы порадовать вас мощными обновлениями. Огромный выбор размеров: в коллекции представлены как всеми любимые «рыбы», так и скейтборды для самых маленьких райдеров. Деки с High конкейвом и есть деки с Twin формой! А вишенка на торте — данные деки с технологией Impact Light!
Сделаны на DSM — это одна из топовых фабрик мира по производству скейтбордов. Материалы на высоком уровне: используется прочный, жёсткий американский клён, с отличным щелчком и выносливостью. То, что нужно для серьёзного катания!
Размеры:

8.125" x 31.7"; WB: 14.125" IMPACT LIGHT
8.25" x 31.7"; WB: 14.125" IMPACT LIGHT
8.375" x 31.875"; WB: 14.25" IMPACT LIGHT
Конкейв: HIGH

8.636" х 30.4"; WB: 14.25" HIGH concave
10.0" х 31.61"; WB: 14.5" или 15" MEDIUM Concave
IMPACT LIGHT — деки с продольной вставкой карбона сверху доски, что делает её очень крепкой! Имеет жёсткую конструкцию; может долго сохранять хороший щелчок, а также, имеет изначально более мощный щелчок! """

        driver = set_up(url=url_product_1)
        product_page = ProductPage(driver)
        product_page.close_modal_window()
        # Проверка описания товара
        product_page.check_product_page(product_head_title, product_price, product_size, product_description)

        driver.quit()


    @allure.description("Test product page 2")
    def test_product_page_2(self, set_up):

        product_head_title = 'Футболка C1RCA VICTORY TEE GREEN BOTTLE'
        product_price = '1 950 ₽'
        product_size = 'S M'
        product_description = """Стильная футболка премиум-класса от одного из самых легендарных скейт-брендов! Отлично сочетается с брюками, джинсами и шортами. Изготовлена из мягкой и прочной веганской ткани, имеет классический крой, который не стесняет движений во время катания на скейте. Крутой принт с логотипом C1RCA создаёт лаконичный вид, такой же классический, как и скейт-наследие бренда.
 Сертификация «PETA-Approved Vegan» - одежда без компонентов животного происхождения. 
Состав: 100% органический чесаный хлопок, стиранный. 180 гр."""

        driver = set_up(url=url_product_2)
        product_page = ProductPage(driver)
        product_page.close_modal_window()
        # Проверка описания товара
        product_page.check_product_page(product_head_title, product_price, product_size, product_description)

        driver.quit()