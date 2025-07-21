import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from base.base_class import Base

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.base = Base(driver)



        #Locators
    modal_window_yes_button = '//a[@class="button button--modal yes"]'

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

    #Getters
    def get_modal_window_yes_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.modal_window_yes_button)))

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
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_submit)))

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

    #Actions
    def click_modal_window_yes_button(self):
        self.get_modal_window_yes_button().click()
        print("Click yes in modal window")

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

    #Methods
    def add_product_1_to_cart(self):
        print("==Добавляем товар в корзину==")
        set_time = 1 # задаем время сна для подстановки
        self.click_modal_window_yes_button()
        time.sleep(set_time)
        self.click_catalog_button()
        time.sleep(set_time)
        self.move_to_category_skateboarding()
        time.sleep(set_time)
        self.click_subcategory_skate_deck()
        time.sleep(set_time)
        self.base.approve_valid_url("https://www.skvot.com/catalog/skateboarding/skate-deck")
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});"  # или 'block: 'nearest''
            "window.scrollBy(0, -100);",  # Поднимаем на 150px (шапка ~100px? Подберите значение)
            self.get_filter_checkbox_brand_Skvot()
        )
        self.click_filter_checkbox_brand_Skvot()
        time.sleep(set_time)
        self.click_filter_submit()
        time.sleep(set_time)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});"  # или 'block: 'nearest''
            "window.scrollBy(0, -150);",  # Поднимаем на 150px (шапка ~100px? Подберите значение)
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


    def add_product_2_to_cart(self):
        print("==Добавляем товар в корзину==")
        set_time = 1  # задаем время сна для подстановки
        self.click_modal_window_yes_button()
        time.sleep(set_time)
        self.click_catalog_button()
        time.sleep(set_time)
        self.move_to_category_clothing()
        time.sleep(set_time)
        self.click_subcategory_shirts()
        time.sleep(set_time)
        self.base.approve_valid_url("https://www.skvot.com/catalog/clothing/shirts")
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});"  # или 'block: 'nearest''
            "window.scrollBy(0, -100);",  # Поднимаем на 150px (шапка ~100px? Подберите значение)
            self.get_filter_checkbox_brand_C1RCA()
        )
        self.click_filter_checkbox_brand_C1RCA()
        time.sleep(set_time)
        self.click_filter_submit()
        time.sleep(set_time)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});"  # или 'block: 'nearest''
            "window.scrollBy(0, -150);",  # Поднимаем на 150px (шапка ~100px? Подберите значение)
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


