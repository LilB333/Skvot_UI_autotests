import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def set_up():

    def setup_browser(url):

        print("\nStart test")

        # Настройки Chrome
        chrome_options = Options()

        # Сначала устанавливаем headless режим
        chrome_options.add_argument('--headless=new')

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        # Настройки логирования
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("--disable-logging")

        # Путь к драйверу
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.execute_cdp_cmd(
            "Emulation.setDeviceMetricsOverride",
            {
                "width": 1920,
                "height": 1080,
                "deviceScaleFactor": 1,
                "mobile": False,
                "screenWidth": 1920,
                "screenHeight": 1080,
                "viewport": {
                    "x": 0,
                    "y": 0,
                    "width": 1920,
                    "height": 1080,
                    "scale": 1
                }
            }
        )

        # Открытие сайта
        driver.get(url)
        driver.maximize_window()

        return driver
    yield setup_browser

    # Завершение теста
    print("\nFinish test")
