import time
from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from base.base_class import Base
from utils.logger import Logger


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.base = Base(driver)



    #Locators
    modal_window_close_button = '//span[@class="close-modal-btn"]'

    product_head_title = '//h1[@class="page-head__title"]'
    product_price = '//div[@class="product-price"]'
    product_size = '//div[@class="product-size"]'
    product_description = '//div[@class="product__description"]'

    size_button_deck = '//label[contains(text(), "8.64") and @class="product-size__label"]'
    size_button_shirt = '//label[contains(text(), "M") and @class="product-size__label"]'

    in_cart_button = '//a[@class="button button--icon product-buttons__button goods_buy"]'
    cart_button = '//div[@class="cart-btn"]'
    place_order = '//a[@class="button-more"]'

    cart_title = '//div[@class="cart-popup__title"]'
    cart_item = '//div[@class="cart-popup-item"]'
    cart_main = '//div[@class="cart-popup__main"]'
    cart_total_sum = '//div[@class="cart-popup__total"]'
    cart_clean_button = '//a[@class="cart-popup__clean"]'

    #Getters
    def get_modal_window_close_button(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.modal_window_close_button)))

    def get_product_head_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_head_title)))
    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))
    def get_product_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_size)))
    def get_product_description(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_description)))

    def get_size_button_deck(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.size_button_deck)))
    def get_size_button_shirt(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.size_button_shirt)))

    def get_in_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.in_cart_button)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_button)))
    def get_place_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.place_order)))

    def get_cart_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_title)))
    def get_cart_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_item)))
    def get_cart_main(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_main)))
    def get_cart_total_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_total_sum)))
    def get_cart_clean_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_clean_button)))

    #Actions
    def click_modal_window_close_button(self):
        self.get_modal_window_close_button().click()
        print("Close modal window")

    def click_size_button_deck(self):
        self.get_size_button_deck().click()
        print("Deck size button is clicked")
    def click_size_button_shirt(self):
        self.get_size_button_shirt().click()
        print("Shirt size button is clicked")

    def click_in_cart_button(self):
        self.get_in_cart_button().click()
        print("In cart button is clicked")
    def move_to_cart_button(self):
        self.action.move_to_element(self.get_cart_button())
        self.action.perform()
        print("Move to cart button")
    def click_place_order_button(self):
        self.get_place_order().click()
        print("Place order button is clicked")
    def click_cart_clean_button(self):
        self.get_cart_clean_button().click()
        print("Cart clean button was clicked")

    #Methods
    def close_modal_window(self):
        with allure.step("Click modal window close button"):
            Logger.add_start_step(method="click modal window close button")
            self.click_modal_window_close_button()
            Logger.add_end_step(url=self.driver.current_url, method="click modal window close button")

    def check_product_page(self, product_head_title, product_price, product_size, product_description):
        with allure.step("Check product page"):
            Logger.add_start_step(method="check product page")
            self.base.check_element_text_value(product_head_title, self.get_product_head_title())
            self.base.check_element_text_value(product_price, self.get_product_price())
            self.base.check_element_text_value(product_size, self.get_product_size())
            self.base.check_element_text_value(product_description, self.get_product_description())
            time.sleep(2)
            self.base.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="check product page")

    def add_product_to_cart(self):
        with allure.step("Add product to cart"):
            Logger.add_start_step(method="add product to cart")
            self.click_size_button_deck()
            self.click_in_cart_button()
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="add product to cart")

    def add_multiple_product_to_cart(self, url):
        with allure.step("Add multiple product to cart"):
            Logger.add_start_step(method="add multiple product to cart")
            # Добавляем первый товар в корзину
            self.click_size_button_deck()
            self.click_in_cart_button()
            time.sleep(1)
            # Добавляем второй товар в корзину
            self.driver.get(url)
            self.click_size_button_shirt()
            self.click_in_cart_button()
            time.sleep(1)
            Logger.add_end_step(url=self.driver.current_url, method="add multiple product to cart")


    def check_product_info_from_cart(self, cart_title, cart_item, cart_total_sum):
        with allure.step("Check product info from cart"):
            Logger.add_start_step(method="check product info from cart")
            self.action.move_to_element(self.get_cart_button()).perform()
            self.base.check_element_text_value(cart_title, self.get_cart_title())
            self.base.check_element_text_value(cart_item, self.get_cart_main())
            self.base.check_element_text_value(cart_total_sum, self.get_cart_total_sum())
            self.base.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="check product info from cart")

    def clean_cart(self):
        with allure.step("Clean cart"):
            Logger.add_start_step(method="clean cart")
            print("==Очищаем корзину==")
            self.move_to_cart_button()
            self.click_cart_clean_button()
            Logger.add_end_step(url=self.driver.current_url, method='clean_cart')