import unittest
from base_test import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RedditTest(BaseTest):

    def test_reddit_search(self):
        driver = self.driver

        # Otwórz stronę Reddit
        driver.get("https://www.reddit.com/")

        # Asercja 1: Sprawdzenie tytułu strony
        assert "Reddit" in driver.title, "Tytuł strony nie zawiera 'Reddit'"
        time.sleep(1)

        # Asercja 2: Sprawdzenie pola wyszukiwania
        search_box = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
        assert search_box.is_displayed(), "Pole wyszukiwania nie jest widoczne"

        # Asercja 3: Wpisanie frazy do wyszukiwania
        search_box.send_keys("Python" + Keys.RETURN)
        time.sleep(2)  # Czekaj na załadowanie wyników

        # Asercja 4: Sprawdzenie, czy są wyniki wyszukiwania
        search_results = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div[data-testid='post-container']"))
        )
        assert len(search_results) > 0, "Brak wyników wyszukiwania dla 'Python'"

        # Asercja 5: Kliknięcie w pierwszy wynik wyszukiwania
        first_result_link = search_results[0].find_element(By.CSS_SELECTOR, "a[data-click-id='comments']")
        first_result_link.click()
        time.sleep(2)

        # Asercja 6: Sprawdzenie, czy otworzył się post
        assert "Python" in driver.title, "Nie udało się przejść do postu na temat 'Python'"

        # Asercja 7: Sprawdzenie, czy sekcja komentarzy jest widoczna
        comments_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='comments-section']"))
        )
        assert comments_section.is_displayed(), "Sekcja komentarzy nie jest widoczna"

        # Asercja 8: Sprawdzenie widoczności przycisku logowania (dla niezalogowanego użytkownika)
        login_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']")
        assert login_button.is_displayed(), "Przycisk logowania nie jest widoczny"

        # Asercja 9: Sprawdzenie widoczności linku do rejestracji
        register_link = driver.find_element(By.LINK_TEXT, "sign up")
        assert register_link.is_displayed(), "Link do rejestracji nie jest widoczny"

        # Asercja 10: Sprawdzenie widoczności sekcji 'Popular posts'
        popular_posts_section = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='feed-ads']"))
        )
        assert popular_posts_section.is_displayed(), "Sekcja popularnych postów nie jest widoczna"


if __name__ == "__main__":
    unittest.main()
