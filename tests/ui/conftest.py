import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def set_up():

    def setup_browser(url):

        print("\nStart test")

        # Настройки Chrome
        chrome_options = Options()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('detach', True)

        # Путь к драйверу
        service = Service(
            executable_path='C:\\Users\\user\\Downloads\\data for work\\pycharm_projects\\ProjectsPy\\resource\\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Открытие сайта
        driver.get(url)
        driver.maximize_window()

        return driver
    yield setup_browser

    # Завершение теста
    print("\nFinish test")
