from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import subprocess

class DriverFactory:

    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        # Auto-detect chromium path on Render
        chrome_path = subprocess.check_output(["which", "chromium"]).decode().strip()
        driver_path = subprocess.check_output(["which", "chromedriver"]).decode().strip()

        options.binary_location = chrome_path
        service = Service(driver_path)

        driver = webdriver.Chrome(service=service, options=options)
        return driver