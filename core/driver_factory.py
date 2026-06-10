import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class DriverFactory:

    @staticmethod
    def get_driver():
        options = Options()

        # ── Check if running on cloud server ──────────────────────
        is_cloud = os.environ.get("RENDER") or os.environ.get("STREAMLIT_SHARING_MODE")

        if is_cloud:
            # Cloud — must be headless (no screen available)
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            print("☁️  Running in cloud mode (headless)")
        else:
            # Local PC — open visible browser so you can see it!
            options.add_argument("--start-maximized")
            print("🖥️  Running in local mode (visible browser)")

        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(options=options)
        return driver