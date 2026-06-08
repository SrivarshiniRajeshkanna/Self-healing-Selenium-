from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:

    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=options)
        return driver  # No implicit wait — we use explicit waits instead