from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class DriverFactory:

    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.binary_location = "/usr/bin/chromium"  # Render's Chrome path

        service = Service("/usr/bin/chromedriver")  # Render's ChromeDriver path
        driver = webdriver.Chrome(service=service, options=options)
        return driver