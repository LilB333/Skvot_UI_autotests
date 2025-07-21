import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    "Method to get url"
    def get_url(self):
        get_url = self.driver.current_url
        print("Current url", get_url)

    "Method to approve valid url"
    def approve_valid_url(self, url):
        assert url == self.driver.current_url
        print("Url is valid")

    "Method to check element text value"
    def check_element_text_value(self, text, element_xpath):
        assert text == element_xpath.text
        print("Element text is valid")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshoot' + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\Selenium_Skvot_UI_Autotests\\screen\\' + name_screenshot)