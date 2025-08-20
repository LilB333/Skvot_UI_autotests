import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    "Метод для получения url"
    def get_url(self):
        get_url = self.driver.current_url
        print("====Текущий url====", get_url)

    "Метод для сверки url"
    def approve_valid_url(self, url):
        assert url == self.driver.current_url
        print("====Url верный====")

    "Метод для проверки текстового значения элемента"
    def check_element_text_value(self, text, element_xpath):
        print(f"Значение текста элемента: \n{element_xpath.text}")
        assert text in element_xpath.text
        print("====Текст элемента верный====")

    "Метод для проверки есть ли текст на странице"
    def check_text_on_page(self, text):
        assert text in self.driver.page_source
        print("====Текст есть на странице====")

    "Метод для проверки что текста нет на странице"
    def check_text_not_on_page(self, text):
        assert text not in self.driver.page_source
        print("====Текста нет на странице====")

    "Метод для проверки значения CSS-свойства элемента"
    def check_value_css_property(self, element, css_property, value):
        print(f"Значение CSS-свойства: {element.value_of_css_property(css_property)}")
        assert value == element.value_of_css_property(css_property)
        print("====Значение CSS-свойства верное====")

    """Метод для получения скриншота"""
    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshoot' + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\Selenium_Skvot_UI_Autotests\\screen\\' + name_screenshot)
