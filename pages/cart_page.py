import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utils.logger import Logger

class CartPage:
    def __init__(self, driver):
        self.base = Base(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    #Mock-data
    email = 'cope80449@cancer-treatment.xyz'
    password = 'test_create_user1'

    #Locators
    modal_window_close_button = '//span[@class="close-modal-btn"]'

    cart_item = '//div[@class="cart-item"]'

    cart_total_sum = '//div[contains(text(), "Итого:")]'

    email_input = '(//input[@type="email"])[1]'
    password_input = '(//input[@type="password"])[1]'
    submit_button = '(//button[@type="submit"])[1]'
    place_order_button = '//a[@href="/cart/ordering" and contains(text(), "Оформить заказ")]'
    city_input = '//input[@placeholder="Введите ваш город"]'
    first_city_in_dropdown_list = '(//a[@class="ui-menu-item-wrapper"])[1]'
    delivery_service_button = '//button[@data-title="СДЭК"]'
    continue_payment_button = '//a[@data-step="pay"]'
    address_zip_input = '//input[@name="address_zip"]'
    address_street_input = '//input[@placeholder="улица"]'
    address_street_number_input = '//input[@placeholder="дом"]'
    address_building_input = '//input[@placeholder="корп."]'
    address_apartment_input = '//input[@placeholder="кв."]'
    cart_button = '//div[@class="cart-btn"]'
    cart_clean_button = '//a[@class="cart-popup__clean"]'

    #Getters
    def get_modal_window_close_button(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.modal_window_close_button)))

    def get_cart_item(self, n):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f'({self.cart_item})[{n}]')))

    def get_cart_total_sum(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_total_sum)))

    def get_email_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_input)))
    def get_password_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_input)))
    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_button)))
    def get_place_order_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.place_order_button)))
    def get_city_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.city_input)))
    def get_first_city_in_dropdown_list(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_city_in_dropdown_list)))
    def get_delivery_service_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delivery_service_button)))
    def get_continue_payment_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_payment_button)))
    def get_address_zip_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address_zip_input)))
    def get_address_street_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address_street_input)))
    def get_address_street_number_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address_street_number_input)))
    def get_address_building_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address_building_input)))
    def get_address_apartment_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address_apartment_input)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_button)))
    def get_cart_clean_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_clean_button)))

    #Actions
    def click_modal_window_close_button(self):
        self.get_modal_window_close_button().click()
        print("Close modal window")

    def add_email (self, email):
        self.get_email_input().send_keys(email)
        print("Added email")
    def add_password (self, password):
        self.get_password_input().send_keys(password)
        print("Added password")
    def click_submit_button(self):
        self.get_submit_button().click()
        print("Submitted button was clicked")
    def click_place_order_button(self):
        self.get_place_order_button().click()
        print("Place order button was clicked")
    def add_city (self, city):
        self.get_city_input().send_keys(city)
        print("Added city")
    def click_first_city_in_dropdown_list(self):
        self.get_first_city_in_dropdown_list().click()
        print("Selected first city in dropdown list")
    def click_delivery_service_button(self):
        self.get_delivery_service_button().click()
        print("Selected delivery service")
    def click_continue_payment_button(self):
        self.get_continue_payment_button().click()
        print("Continue payment button was clicked")
    def add_address_zip (self, address_zip):
        self.get_address_zip_input().send_keys(address_zip)
        print("Added address zip")
    def add_address_street (self, address_street):
        self.get_address_street_input().send_keys(address_street)
        print("Added address street")
    def add_address_street_number (self, address_street_number):
        self.get_address_street_number_input().send_keys(address_street_number)
        print("Added address street number")
    def add_address_building (self, address_building):
        self.get_address_building_input().send_keys(address_building)
        print("Added address building")
    def add_address_apartment (self, address_apartment):
        self.get_address_apartment_input().send_keys(address_apartment)
        print("Added address apartment")
    def move_to_cart_button(self):
        self.action.move_to_element(self.get_cart_button())
        self.action.perform()
        print("Move to cart button")
    def click_cart_clean_button(self):
        self.get_cart_clean_button().click()
        print("Cart clean button was clicked")

    #Methods
    def close_modal_window(self):
        with allure.step("Click modal window close button"):
            Logger.add_start_step(method="click modal window close button")
            self.click_modal_window_close_button()
            Logger.add_end_step(url=self.driver.current_url, method="click modal window close button")

    def check_product_info(self, text, n):
        with allure.step("Check product info"):
            Logger.add_start_step(method='check_product_info')
            print("==Проверяем добавленный товар==")
            self.base.check_element_text_value(text, self.get_cart_item(n))
            Logger.add_end_step(url=self.driver.current_url, method="check_product_info")

    def check_total_cart_sum(self, total_sum):
        with allure.step("Check total cart sum"):
            Logger.add_start_step(method="check_total_cart_sum")
            print("==Проверяем итоговую сумму==")
            self.base.check_element_text_value(total_sum, self.get_cart_total_sum())
            Logger.add_end_step(url=self.driver.current_url, method="check_total_cart_sum")

    def clean_cart(self):
        with allure.step("Clean cart"):
            Logger.add_start_step(method="clean_cart")
            print("==Очищаем корзину==")
            self.move_to_cart_button()
            self.click_cart_clean_button()
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="clean_cart")

    def login(self, email, password):
        with allure.step("Login"):
            Logger.add_start_step(method='login')
            print("==Заходим в аккаунт==")
            self.add_email(email)
            time.sleep(1)
            self.add_password(password)
            time.sleep(1)
            self.click_submit_button()
            Logger.add_end_step(url=self.driver.current_url, method='login')

    def fill_shipping_info(self, city, address_zip, address_street, address_street_number, address_building, address_apartment):
        with allure.step("Fill shipping info"):
            Logger.add_start_step(method='fill_shipping_info')
            print("==Оформляем добавленный товар==")
            set_time = 1

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});"
                "window.scrollBy(0, 300);",  # Опускаем на 300px вниз
                self.get_cart_button()
            )
            time.sleep(1)
            self.click_place_order_button()
            time.sleep(set_time)
            self.add_city(city)
            time.sleep(set_time)
            self.click_first_city_in_dropdown_list()
            time.sleep(set_time)
            self.click_delivery_service_button()
            time.sleep(set_time)
            self.click_continue_payment_button()
            time.sleep(set_time)
            self.add_address_zip(address_zip)
            self.add_address_street(address_street)
            self.add_address_street_number(address_street_number)
            self.add_address_building(address_building)
            self.add_address_apartment(address_apartment)
            self.base.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='fill_shipping_info')

