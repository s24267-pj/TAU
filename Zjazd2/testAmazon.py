import unittest
from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class AmazonTest(BaseTest):

    def test_amazon(self):
        driver = self.driver

        # 1. Otwórz stronę Amazon
        driver.get('https://www.amazon.com/')
        assert "Amazon" in driver.title, "Tytuł strony nie zawiera 'Amazon'"

        # 2. Sprawdzenie pola wyszukiwania
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        assert search_box.is_displayed(), "Pole wyszukiwania nie jest widoczne"

        # 3. Testowanie wyszukiwania produktu (np. "Laptop")
        search_box.send_keys("Laptop" + Keys.RETURN)
        time.sleep(2)
        assert "Laptop" in driver.title, "Strona wyników nie zawiera 'Laptop'"

        # 4. Sprawdzenie, czy pojawiły się wyniki wyszukiwania
        search_results = driver.find_element(By.CSS_SELECTOR, ".s-main-slot")
        assert search_results.is_displayed(), "Brak wyników wyszukiwania"

        # 5. Testowanie przycisku "Wyszukaj"
        search_button = driver.find_element(By.CSS_SELECTOR, "input.nav-input[type='submit']")
        assert search_button.is_displayed(), "Przycisk wyszukiwania nie jest widoczny"

        # 6. Sprawdzenie, czy menu nawigacyjne działa (np. kategorie)
        category_menu = driver.find_element(By.ID, "nav-hamburger-menu")
        category_menu.click()
        time.sleep(2)
        assert driver.find_element(By.ID, "hmenu-content").is_displayed(), "Menu nawigacyjne nie jest widoczne"

        # 7. Testowanie linku do "Pomoc"
        help_link = driver.find_element(By.LINK_TEXT, "Your Account")
        help_link.click()
        time.sleep(2)
        assert "Your Account" in driver.title, "Nie udało się przejść do strony 'Your Account'"

        # 8. Sprawdzenie obecności logo Amazon
        logo = driver.find_element(By.ID, "nav-logo")
        assert logo.is_displayed(), "Logo Amazon nie jest widoczne"


if __name__ == "__main__":
    unittest.main()
