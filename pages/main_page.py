import time
from time import sleep

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from base.base_class import Base
from utils.logger import Logger

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.base = Base(driver)

    #Locators
    modal_window_close_button = '//span[@class="close-modal-btn"]'

    login_button = '//a[@data-modal="login"]'
    email_input = '//input[@type="email"]'
    password_input = '//input[@type="password"]'
    submit_button = '//button[@type="submit"]'

    search_button = '//div[@class="search-btn"]'
    search_field = '//input[@placeholder="Введите слово для поиска"]'
    search_head_title = '//div[@class="page-head__title"]'

    catalog_button = '//div[@class="catalog-btn"]'
    category_skateboarding = '//a[@href="/catalog/skateboarding"]'
    category_clothing = '//a[@href="/catalog/clothing"]'

    subcategory_skate_deck = '//a[@href="/catalog/skateboarding/skate-deck"]'
    subcategory_shirts = '//a[@href="/catalog/clothing/shirts"]'

    filter_checkbox_brand_C1RCA = '//div[contains(text(), "C1Rca") and @class="checkbox__name"]'
    filter_checkbox_brand_Skvot = '//div[contains(text(), "Сквот") and @class="checkbox__name"]'
    filter_checkbox_sex_male = '//div[contains(text(), "Мужской") and @class="checkbox__name"]'
    filter_highest_price = '//input[@id="filter-price-input-2"]'
    filter_submit = '//div[@class="filter-aside__number visible"]'

    shirt_c1rca = '//div[@class="top-item__image" and contains(@title, "Футболка C1RCA VICTORY TEE GREEN BOTTLE")]'
    deck_skvot = '//div[@class="top-item__image" and contains(@title, "Дека для скейта СКВОТ Knight")]'

    size_button_deck = '//label[contains(text(), "8.64") and @class="product-size__label"]'
    size_button_shirt = '//label[contains(text(), "M") and @class="product-size__label"]'
    in_cart_button = '//a[@class="button button--icon product-buttons__button goods_buy"]'
    cart_button = '//div[@class="cart-btn"]'
    place_order = '//a[@class="button-more"]'
    cart_clean_button = '//a[@class="cart-popup__clean"]'

    #Getters
    def get_modal_window_close_button(self):
        return WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, self.modal_window_close_button)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_email_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_input)))
    def get_password_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_input)))
    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))
    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))
    def get_search_head_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_head_title)))

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    def get_category_skateboarding(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_skateboarding)))
    def get_category_clothing(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_clothing)))

    def get_subcategory_shirts(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subcategory_shirts)))
    def get_subcategory_skate_deck(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.subcategory_skate_deck)))

    def get_filter_checkbox_brand_C1RCA(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_checkbox_brand_C1RCA)))
    def get_filter_checkbox_brand_Skvot(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_checkbox_brand_Skvot)))
    def get_filer_checkbox_sex_male(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_checkbox_sex_male)))
    def get_filter_highest_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_highest_price)))
    def get_filter_submit(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.filter_submit)))

    def get_shirt_c1rca(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.shirt_c1rca)))
    def get_deck_skvot(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.deck_skvot)))

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
    def get_cart_clean_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_clean_button)))

    #Actions
    def click_modal_window_close_button(self):
        self.get_modal_window_close_button().click()
        print("Close modal window")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def add_email(self, email):
        self.get_email_input().send_keys(email)
        print("Added email")

    def add_password(self, password):
        self.get_password_input().send_keys(password)
        print("Added password")

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Submitted button was clicked")

    def click_search_button(self):
        self.get_search_button().click()
        print("Search button was clicked")


    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Catalog button is clicked")
    def move_to_category_skateboarding(self):
        self.action.move_to_element(self.get_category_skateboarding())
        self.action.perform()
        print("Move to category skateboarding button")
    def move_to_category_clothing(self):
        self.action.move_to_element(self.get_category_clothing())
        self.action.perform()
        print("Move to category clothing button")

    def click_subcategory_skate_deck(self):
        self.get_subcategory_skate_deck().click()
        print("Subcategory skate deck button is clicked")
    def click_subcategory_shirts(self):
        self.get_subcategory_shirts().click()
        print("Subcategory shirts button is clicked")

    def click_filter_checkbox_brand_C1RCA(self):
        self.get_filter_checkbox_brand_C1RCA().click()
        print("Filter checkbox brand C1Rca button is clicked")
    def click_filter_checkbox_brand_Skvot(self):
        self.get_filter_checkbox_brand_Skvot().click()
        print("Filter checkbox brand Skvot button is clicked")
    def click_filter_checkbox_sex_male(self):
        self.get_filer_checkbox_sex_male().click()
        print("Filter checkbox sex male button is clicked")
    def add_value_to_filter_highest_price(self, price):
        self.get_filter_highest_price().send_keys(price)
        print(f"Filter Highest Price is {price}")
    def click_filter_submit(self):
        self.get_filter_submit().click()
        print("Filter submit button is clicked")

    def click_shirt_c1rca(self):
        self.get_shirt_c1rca().click()
        print("Shirt c1rca button is clicked")
    def click_deck_skvot(self):
        self.get_deck_skvot().click()
        print("Deck skvot button is clicked")

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

    def login(self, email, password):
        with allure.step("Login"):
            Logger.add_start_step(method="login")
            self.click_login_button()
            time.sleep(1)
            self.add_email(email)
            time.sleep(1)
            self.add_password(password)
            time.sleep(1)
            self.click_submit_button()
            time.sleep(2)
            self.base.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="login")

    def search_item(self, item_name):
        with allure.step("Search item"):
            Logger.add_start_step(method="search item")
            self.click_modal_window_close_button()
            time.sleep(1)
            self.click_search_button()
            time.sleep(1)
            self.get_search_field().send_keys(item_name + Keys.ENTER)
            time.sleep(1)
            self.base.check_element_text_value(item_name.upper(), self.get_search_head_title())
            self.base.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="search item")

    def add_product_1_to_cart(self):
        with allure.step("Add product 1 to cart"):
            Logger.add_start_step(method='add_product_1_to_cart')
            print("==Добавляем товар в корзину==")
            set_time = 1 # задаем время сна для подстановки
            self.click_catalog_button()
            time.sleep(set_time)
            self.move_to_category_skateboarding()
            time.sleep(set_time)
            self.click_subcategory_skate_deck()
            time.sleep(set_time)
            self.base.approve_valid_url("https://www.skvot.com/catalog/skateboarding/skate-deck")
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});"  
                "window.scrollBy(0, -100);",  # Поднимаем на 100px вверх
                self.get_filter_checkbox_brand_Skvot()
            )
            self.click_filter_checkbox_brand_Skvot()
            time.sleep(set_time)
            self.click_filter_submit()
            time.sleep(set_time)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});"  
                "window.scrollBy(0, -150);",  # Поднимаем на 150px вверх
                self.get_deck_skvot()
            )
            time.sleep(set_time)
            self.click_deck_skvot()
            time.sleep(set_time)
            self.click_size_button_deck()
            time.sleep(set_time)
            self.click_in_cart_button()
            time.sleep(set_time)
            self.move_to_cart_button()
            time.sleep(set_time)
            self.click_place_order_button()
            self.base.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='add_product_1_to_cart')


    def add_product_2_to_cart(self):
        with allure.step("Add product 2 to cart"):
            Logger.add_start_step(method='add_product_2_to_cart')
            print("==Добавляем товар в корзину==")
            set_time = 1  # задаем время сна для подстановки
            self.click_modal_window_close_button()
            time.sleep(set_time)
            self.click_catalog_button()
            time.sleep(set_time)
            self.move_to_category_clothing()
            time.sleep(set_time)
            self.click_subcategory_shirts()
            time.sleep(set_time)
            self.base.approve_valid_url("https://www.skvot.com/catalog/clothing/shirts")
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});"  
                "window.scrollBy(0, -100);",  # Поднимаем на 100px вверх
                self.get_filter_checkbox_brand_C1RCA()
            )
            self.click_filter_checkbox_brand_C1RCA()
            time.sleep(set_time)
            self.click_filter_submit()
            time.sleep(set_time)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});"
                "window.scrollBy(0, -150);",  # Поднимаем на 150px вверх
                self.get_shirt_c1rca()
            )
            time.sleep(set_time)
            self.click_shirt_c1rca()
            time.sleep(set_time)
            self.click_size_button_shirt()
            time.sleep(set_time)
            self.click_in_cart_button()
            time.sleep(set_time)
            self.move_to_cart_button()
            time.sleep(set_time)
            self.click_place_order_button()
            self.base.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='add_product_2_to_cart')

    def clean_cart(self):
        with allure.step("Clean cart"):
            Logger.add_start_step(method='clean_cart')
            print("==Очищаем корзину==")
            self.move_to_cart_button()
            self.click_cart_clean_button()
            Logger.add_end_step(url=self.driver.current_url, method='clean_cart')
