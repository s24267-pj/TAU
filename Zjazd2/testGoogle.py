import unittest
from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BrowserTest(BaseTest):

    def test_google(self):
        driver = self.driver
        driver.get('https://www.google.com/')

        # 1. Sprawdzenie, czy strona Google jest załadowana
        self.assertIn("Google", driver.title)

        # 2. Sprawdzenie, czy przycisk cookie jest widoczny
        cookie_button = driver.find_element(By.ID, "L2AGLb")
        self.assertTrue(cookie_button.is_displayed())

        cookie_button.click()
        time.sleep(1)

        # 3. Sprawdzenie, czy pole wyszukiwania jest widoczne
        search_box = driver.find_element(By.NAME, "q")
        self.assertTrue(search_box.is_displayed())

        # 4. Sprawdzenie, czy pole wyszukiwania jest puste
        self.assertEqual(search_box.get_attribute("value"), "")
        search_box.send_keys("Selenium")

        # 5. Sprawdzenie, czy tekst "Selenium" został wpisany w pole wyszukiwania
        self.assertEqual(search_box.get_attribute("value"), "Selenium")

        # 6. Sprawdzenie, czy przycisk wyszukiwania jest dostępny
        search_button = driver.find_element(By.NAME, "btnK")
        self.assertTrue(search_button.is_enabled())

        search_box.send_keys(Keys.RETURN)
        time.sleep(1)

        # 7. Sprawdzenie, czy wyniki wyszukiwania są widoczne
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        self.assertGreater(len(results), 0)
        results[0].click()

        # 8. Sprawdzenie, czy strona wyników załadowała się poprawnie
        self.assertNotEqual(driver.title, "Google")


if __name__ == "__main__":
    unittest.main()
