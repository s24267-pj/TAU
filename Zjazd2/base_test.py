from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        # Wybór przeglądarki do testów
        self.driver = self.create_driver('firefox')  # firefox, chrome, opera
        self.driver.get("https://www.google.com")

    def create_driver(self, browser_name):
        if browser_name == 'chrome':
            options = Options()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            driver = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            options.headless = True
            driver = webdriver.Firefox(options=options)
        elif browser_name == 'opera':
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            driver = webdriver.Opera(options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
        return driver

    def tearDown(self):
        if self.driver:
            self.driver.quit()
