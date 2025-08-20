import allure
import pytest
from pages.main_page import MainPage
from base.base_class import Base

url = 'https://www.skvot.com/'

@pytest.mark.run(order=2)
class TestSearchProduct:
    @allure.description("Test search valid product")
    def test_search_valid_product(self, set_up):
        driver = set_up(url=url)

        main = MainPage(driver)
        main.search_item('бушинг')

        base = Base(driver)
        base.check_text_not_on_page('Поиск не принес результата')

        driver.quit()

    @allure.description("Test search invalid product")
    def test_search_invalid_product(self, set_up):
        driver = set_up(url=url)

        main = MainPage(driver)
        main.search_item('дуршлаг')

        base = Base(driver)
        base.check_text_on_page('Поиск не принес результата')

        driver.quit()