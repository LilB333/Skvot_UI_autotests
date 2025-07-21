import time
from argparse import Action

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    #Mock-data
    email = 'cope80449@cancer-treatment.xyz'
    password = 'test_create_user1'
    city = 'спб'
    address_zip = '453129'
    address_street = 'Petrogradskaya'
    address_street_number = '17'
    address_building = '2'
    address_apartment = '24'

    #Locators
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
    def buy_product(self):
        print("==Оформляем добавленный товар==")
        set_time = 1
        self.add_email(email=self.email)
        time.sleep(set_time)
        self.add_password(password=self.password)
        time.sleep(set_time)
        self.click_submit_button()
        time.sleep(set_time)
        self.click_place_order_button()
        time.sleep(set_time)
        self.add_city(city=self.city)
        time.sleep(set_time)
        self.click_first_city_in_dropdown_list()
        time.sleep(set_time)
        self.click_delivery_service_button()
        time.sleep(set_time)
        self.click_continue_payment_button()
        time.sleep(set_time)
        self.add_address_zip(address_zip=self.address_zip)
        time.sleep(set_time)
        self.add_address_street(address_street=self.address_street)
        time.sleep(set_time)
        self.add_address_street_number(address_street_number=self.address_street_number)
        time.sleep(set_time)
        self.add_address_building(address_building=self.address_building)
        time.sleep(set_time)
        self.add_address_apartment(address_apartment=self.address_apartment)
        time.sleep(set_time)
        self.move_to_cart_button()
        time.sleep(set_time)
        self.click_cart_clean_button()
        time.sleep(3)
