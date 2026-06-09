from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:

    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--headless")              # No display needed
        options.add_argument("--no-sandbox")            # Required for Render
        options.add_argument("--disable-dev-shm-usage") # Prevents crashes
        options.add_argument("--disable-gpu")           # Headless stability
        options.add_argument("--window-size=1920,1080") # Replaces maximized

        driver = webdriver.Chrome(options=options)
        return driver  # No implicit wait — we use explicit waits instead