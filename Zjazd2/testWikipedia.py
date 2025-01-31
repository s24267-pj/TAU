import unittest
from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class WikipediaTest(BaseTest):

    def test_wikipedia_search(self):
        driver = self.driver

        # Otwórz stronę Wikipedii
        driver.get('https://pl.wikipedia.org/')
        assert "Wikipedia" in driver.title, "Tytuł strony nie zawiera 'Wikipedia'"

        # 1. Sprawdzenie, czy logo Wikipedii jest widoczne
        logo = driver.find_element(By.CSS_SELECTOR, "img.mw-logo-icon")
        assert logo.is_displayed(), "Logo Wikipedii nie jest widoczne na stronie"

        # 2. Sprawdzenie pola wyszukiwania
        search_box = driver.find_element(By.NAME, "search")
        assert search_box.is_displayed(), "Pole wyszukiwania nie jest widoczne"

        # 3. Sprawdzenie przycisku wyszukiwania (kliknięcie)
        search_button = driver.find_element(By.CSS_SELECTOR, "button.cdx-search-input__end-button")
        assert search_button.is_displayed(), "Przycisk wyszukiwania nie jest widoczny"

        # 4. Testowanie wyszukiwania
        search_box.send_keys("Python" + Keys.RETURN)
        time.sleep(2)
        assert "Python" in driver.title, "Strona wyników nie zawiera 'Python'"

        # 5. Sprawdzenie obecności stopki
        footer = driver.find_element(By.ID, "footer")
        assert footer.is_displayed(), "Stopka strony nie jest widoczna"

        # 6. Testowanie linku do strony 'O Wikipedii' w stopce
        about_link = driver.find_element(By.XPATH, '//li[@id="footer-places-about"]/a')
        about_link.click()
        time.sleep(2)
        assert "Wikipedia:O Wikipedii" in driver.title, "Nie udało się przejść do strony 'O Wikipedii'"

        # 7. Losowanie artykułu
        initial_title = driver.title

        # Kliknięcie w przycisk menu głównego
        menu_button = driver.find_element(By.ID, "vector-main-menu-dropdown-checkbox")
        menu_button.click()
        time.sleep(1)

        # Kliknięcie w link "Losuj artykuł" w menu
        random_article_link = driver.find_element(By.ID, "n-randompage").find_element(By.TAG_NAME, "a")
        random_article_link.click()

        time.sleep(2)

        new_title = driver.title
        assert initial_title != new_title, "Tytuł okna nie zmienił się po kliknięciu w 'Losuj artykuł'"


if __name__ == "__main__":
    unittest.main()
