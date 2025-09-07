import allure
import pytest

from pages.main_page import MainPage
from base.base_class import Base

url = 'https://www.skvot.com/'

@pytest.mark.run(order=1)
class TestLogin:


    @allure.description("Test login valid")
    def test_login_valid(self, set_up):
        driver = set_up(url=url)

        main = MainPage(driver)
        main.close_modal_window()
        main.login(email = 'cope80449@cancer-treatment.xyz', password = 'test_create_user1')

        driver.quit()

    @allure.description("Test login invalid email")
    def test_login_invalid_email(self, set_up):
        driver = set_up(url=url)

        main = MainPage(driver)
        main.close_modal_window()
        main.login(email = 'cope80449@', password = 'test_create_user1')

        base = Base(driver)
        base.check_text_on_page('Авторизация')

        driver.quit()

    @allure.description("Test login invalid password")
    def test_login_invalid_password(self, set_up):
        driver = set_up(url=url)

        main = MainPage(driver)
        main.close_modal_window()
        main.login(email = 'cope80449@cancer-treatment.xyz', password = 'test_create_')

        base = Base(driver)
        base.check_text_on_page('Авторизация')

        driver.quit()

    @allure.description("Test empty login")
    def test_empty_login(self, set_up):
        driver = set_up(url=url)

        main = MainPage(driver)
        main.close_modal_window()
        main.login(email = '', password = '')

        base = Base(driver)
        base.check_value_css_property(main.get_email_input(), 'border', '1px solid rgb(255, 0, 0)')
        base.check_value_css_property(main.get_password_input(), 'border', '1px solid rgb(255, 0, 0)')

        driver.quit()

