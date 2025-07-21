import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage
from pages.cart_page import CartPage


def test_buy_product_1():

    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option('detach', True)
    service = Service(executable_path='C:\\Users\\user\\Downloads\\data for work\\pycharm_projects\\ProjectsPy\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()


    print("### start test // buy deck ###")
    url = 'https://www.skvot.com/'
    driver.get(url)

    main = MainPage(driver)
    main.add_product_1_to_cart()

    cart = CartPage(driver)
    cart.buy_product()

    driver.quit()
    print("Не оформляем товар до конца, чтобы не спамить Сквот фейковыми заказами. Один такой сделал ради проверки :)")
    print("### finish test ###")

def test_buy_product_2():
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option('detach', True)
    service = Service(
        executable_path='C:\\Users\\user\\Downloads\\data for work\\pycharm_projects\\ProjectsPy\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    print("### start test // buy shirt ###")
    url = 'https://www.skvot.com/'
    driver.get(url)

    main = MainPage(driver)
    main.add_product_2_to_cart()

    cart = CartPage(driver)
    cart.buy_product()

    driver.quit()
    print("Не оформляем товар до конца, чтобы не спамить Сквот фейковыми заказами. Один такой сделал ради проверки :)")
    print("### finish test ###")

