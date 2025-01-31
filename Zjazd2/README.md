# Testowanie strony Google

## Krok 1: Wstępne przygotowanie
1. **Tworzenie instancji przeglądarki**:
   - Wykorzystanie sterownika `webdriver` z ustawionymi opcjami, które umożliwiają testowanie w różnych przeglądarkach (np. Chrome, Firefox, Opera).
   - Otwórz stronę Google (https://www.google.com).

## Krok 2: Sprawdzenie załadowania strony
1. **Sprawdzenie tytułu strony**:
   - Upewnij się, że tytuł strony zawiera słowo "Google".
   - **Asercja**:
    ```python
    assert "Google" in driver.title
    ```
   - Strona Google powinna być poprawnie załadowana.

## Krok 3: Sprawdzenie komunikatu o cookie
1. **Sprawdzenie, czy przycisk akceptacji plików cookie jest widoczny**:
   - Zidentyfikuj przycisk związany z plikami cookie.
   - **Asercja**:
    ```python
    assert cookie_button.is_displayed()
    ```
   - Przycisk powinien być widoczny.
   
2. **Kliknięcie w przycisk akceptacji plików cookie**:
   - Kliknij przycisk akceptacji plików cookie.

## Krok 4: Interakcja z polem wyszukiwania
1. **Sprawdzenie, czy pole wyszukiwania jest widoczne**:
   - Zidentyfikuj pole wyszukiwania (element z nazwą `q`).
   - **Asercja**:
    ```python
    assert search_box.is_displayed()
    ```
   - Pole wyszukiwania powinno być widoczne.

2. **Sprawdzenie, czy pole wyszukiwania jest puste**:
   - Sprawdź, czy pole wyszukiwania jest początkowo puste.
   - **Asercja**:
    ```python
    assert search_box.get_attribute("value") == ""
    ```
   - Pole wyszukiwania nie powinno zawierać żadnych danych początkowych.

3. **Wpisanie tekstu w pole wyszukiwania**:
   - Wpisz w pole wyszukiwania frazę "Selenium".
   - **Asercja**:
    ```python
    assert search_box.get_attribute("value") == "Selenium"
    ```
   - Po wpisaniu tekstu w polu, powinien się on pojawić.

## Krok 5: Wykonanie wyszukiwania
1. **Sprawdzenie, czy przycisk wyszukiwania jest dostępny**:
   - Zidentyfikuj przycisk wyszukiwania (z nazwą `btnK`).
   - **Asercja**:
    ```python
    assert search_button.is_enabled()
    ```
   - Przycisk powinien być aktywny.
   
2. **Naciśnięcie przycisku Enter w polu wyszukiwania**:
   - Naciśnij klawisz Enter, aby wykonać wyszukiwanie.

## Krok 6: Weryfikacja wyników wyszukiwania
1. **Sprawdzenie, czy wyniki wyszukiwania są widoczne**:
   - Zidentyfikuj elementy wyników wyszukiwania (nagłówki wyników z tagiem `h3`).
   - **Asercja**:
    ```python
    assert len(results) > 0
    ```
   - Musi być przynajmniej jeden wynik wyszukiwania.

2. **Kliknięcie w pierwszy wynik wyszukiwania**:
   - Kliknij w pierwszy wynik wyszukiwania, aby przejść do strony.

## Krok 7: Sprawdzenie załadowania strony wyników
1. **Sprawdzenie, czy strona wyników wyszukiwania się załadowała**:
   - Poczekaj, aż tytuł strony zmieni się (bo na początku będzie to "Google").
   - **Asercja**:
    ```python
    assert driver.title != "Google"
    ```
   - Tytuł strony powinien się zmienić, co oznacza, że nowa strona została załadowana.

## Krok 8: Zakończenie testu
1. **Zamknięcie przeglądarki**:
   - Po zakończeniu testu zamknij przeglądarkę.



# Testowanie strony Wikipedii

## Krok 1: Wstępne przygotowanie
1. **Tworzenie instancji przeglądarki**:
   - Wykorzystanie sterownika `webdriver` z ustawionymi opcjami, które umożliwiają testowanie w różnych przeglądarkach (np. Chrome, Firefox, Opera).
   - Uruchomienie przeglądarki i przejście na stronę Wikipedii (https://pl.wikipedia.org/).

## Krok 2: Sprawdzenie załadowania strony
1. **Sprawdzenie tytułu strony**:
   - Upewnij się, że tytuł strony zawiera słowo "Wikipedia".
   - **Asercja**: 
     ```python
     assert "Wikipedia" in driver.title
     ```
     - Tytuł strony powinien zawierać nazwę "Wikipedia".

## Krok 3: Sprawdzenie elementów na stronie
1. **Sprawdzenie, czy logo Wikipedii jest widoczne**:
   - Zidentyfikuj element logo Wikipedii przy pomocy selektora CSS (`img.mw-logo-icon`).
   - **Asercja**: 
     ```python
     assert logo.is_displayed()
     ```
     - Logo powinno być widoczne na stronie.

2. **Sprawdzenie pola wyszukiwania**:
   - Zidentyfikuj pole wyszukiwania po nazwie `search`.
   - **Asercja**: 
     ```python
     assert search_box.is_displayed()
     ```
     - Pole wyszukiwania powinno być widoczne.

3. **Sprawdzenie przycisku wyszukiwania**:
   - Zidentyfikuj przycisk wyszukiwania (z klasą `cdx-search-input__end-button`).
   - **Asercja**: 
     ```python
     assert search_button.is_displayed()
     ```
     - Przycisk wyszukiwania powinien być widoczny.

## Krok 4: Testowanie funkcji wyszukiwania
1. **Wykonanie wyszukiwania**:
   - Wpisz frazę "Python" w pole wyszukiwania i naciśnij klawisz Enter.
   - **Asercja**: 
     ```python
     assert "Python" in driver.title
     ```
     - Tytuł strony wyników powinien zawierać frazę "Python".

## Krok 5: Sprawdzenie obecności stopki
1. **Sprawdzenie, czy stopka jest widoczna**:
   - Zidentyfikuj stopkę po ID `footer`.
   - **Asercja**: 
     ```python
     assert footer.is_displayed()
     ```
     - Stopka powinna być widoczna na stronie.

## Krok 6: Testowanie linku w stopce
1. **Kliknięcie w link 'O Wikipedii' w stopce**:
   - Zidentyfikuj link do strony "O Wikipedii" w stopce i kliknij go.
   - **Asercja**: 
     ```python
     assert "Wikipedia:O Wikipedii" in driver.title
     ```
     - Tytuł strony po kliknięciu w link powinien zawierać "Wikipedia:O Wikipedii".

## Krok 7: Losowanie artykułu
1. **Sprawdzenie, czy link do losowania artykułu działa**:
   - Kliknij w przycisk menu głównego i wybierz opcję "Losuj artykuł".
   - **Asercja**: 
     ```python
     assert initial_title != new_title
     ```
     - Po kliknięciu w link, tytuł strony powinien się zmienić, co oznacza, że artykuł został wylosowany.

## Krok 8: Zakończenie testu
1. **Zamknięcie przeglądarki**:
   - Po zakończeniu testu zamknij przeglądarkę, aby zakończyć sesję testową.



# Testowanie strony Reddit

## Krok 1: Wstępne przygotowanie
1. **Tworzenie instancji przeglądarki**:
   - Wykorzystanie sterownika `webdriver` z ustawionymi opcjami, które umożliwiają testowanie w różnych przeglądarkach (np. Chrome, Firefox, Opera).
   - Uruchomienie przeglądarki i przejście na stronę Reddit (https://www.reddit.com/).

## Krok 2: Sprawdzenie załadowania strony
1. **Sprawdzenie tytułu strony**:
   - Upewnij się, że tytuł strony zawiera słowo "Reddit".
   - **Asercja**: 
     ```python
     assert "Reddit" in driver.title
     ```
     - Tytuł strony powinien zawierać nazwę "Reddit".

## Krok 3: Sprawdzenie elementów na stronie
1. **Sprawdzenie, czy pole wyszukiwania jest widoczne**:
   - Zidentyfikuj pole wyszukiwania przy pomocy selektora CSS (`input[name='q']`).
   - **Asercja**: 
     ```python
     assert search_box.is_displayed()
     ```
     - Pole wyszukiwania powinno być widoczne na stronie.

2. **Wpisanie frazy do wyszukiwania**:
   - Wpisz frazę "Python" w pole wyszukiwania i naciśnij klawisz Enter.
   - **Asercja**: 
     ```python
     search_box.send_keys("Python" + Keys.RETURN)
     ```
     - Po wprowadzeniu frazy, przejdź do wyników wyszukiwania.

## Krok 4: Sprawdzenie wyników wyszukiwania
1. **Sprawdzenie, czy są wyniki wyszukiwania**:
   - Poczekaj na załadowanie wyników wyszukiwania (np. postów).
   - **Asercja**: 
     ```python
     assert len(search_results) > 0
     ```
     - Musi być przynajmniej jeden wynik wyszukiwania.

2. **Kliknięcie w pierwszy wynik wyszukiwania**:
   - Kliknij w pierwszy wynik wyszukiwania, aby otworzyć post.
   - **Asercja**: 
     ```python
     first_result_link.click()
     ```

3. **Sprawdzenie, czy otworzył się post**:
   - Upewnij się, że tytuł strony zawiera słowo "Python", co oznacza, że otworzono post o tematyce związanej z "Python".
   - **Asercja**: 
     ```python
     assert "Python" in driver.title
     ```
     - Strona powinna zawierać temat "Python".

## Krok 5: Sprawdzenie sekcji komentarzy
1. **Sprawdzenie, czy sekcja komentarzy jest widoczna**:
   - Zidentyfikuj sekcję komentarzy na stronie.
   - **Asercja**: 
     ```python
     assert comments_section.is_displayed()
     ```
     - Sekcja komentarzy powinna być widoczna.

## Krok 6: Sprawdzenie przycisków logowania i rejestracji
1. **Sprawdzenie widoczności przycisku logowania**:
   - Zidentyfikuj przycisk logowania (dla niezalogowanego użytkownika).
   - **Asercja**: 
     ```python
     assert login_button.is_displayed()
     ```
     - Przycisk logowania powinien być widoczny na stronie.

2. **Sprawdzenie widoczności linku do rejestracji**:
   - Zidentyfikuj link do rejestracji na stronie.
   - **Asercja**: 
     ```python
     assert register_link.is_displayed()
     ```
     - Link do rejestracji powinien być widoczny.

## Krok 7: Sprawdzenie sekcji "Popular posts"
1. **Sprawdzenie widoczności sekcji 'Popular posts'**:
   - Zidentyfikuj sekcję "Popular posts" na stronie.
   - **Asercja**: 
     ```python
     assert popular_posts_section.is_displayed()
     ```
     - Sekcja popularnych postów powinna być widoczna na stronie.

## Krok 8: Zakończenie testu
1. **Zamknięcie przeglądarki**:
   - Po zakończeniu testu zamknij przeglądarkę, aby zakończyć sesję testową.



# Testowanie strony Amazon

## Krok 1: Wstępne przygotowanie
1. **Tworzenie instancji przeglądarki**:
   - Wykorzystanie sterownika `webdriver` z ustawionymi opcjami, które umożliwiają testowanie w różnych przeglądarkach (np. Chrome, Firefox, Opera).
   - Uruchomienie przeglądarki i przejście na stronę Amazon (https://www.amazon.com/).

## Krok 2: Sprawdzenie załadowania strony
1. **Sprawdzenie tytułu strony**:
   - Upewnij się, że tytuł strony zawiera słowo "Amazon".
   - **Asercja**: 
     ```python
     assert "Amazon" in driver.title
     ```
     - Tytuł strony powinien zawierać nazwę "Amazon".

## Krok 3: Sprawdzenie elementów na stronie
1. **Sprawdzenie, czy pole wyszukiwania jest widoczne**:
   - Zidentyfikuj pole wyszukiwania przy pomocy selektora ID (`twotabsearchtextbox`).
   - **Asercja**: 
     ```python
     assert search_box.is_displayed()
     ```
     - Pole wyszukiwania powinno być widoczne na stronie.

2. **Testowanie wyszukiwania produktu (np. "Laptop")**:
   - Wpisz frazę "Laptop" w pole wyszukiwania i naciśnij klawisz Enter.
   - **Asercja**: 
     ```python
     search_box.send_keys("Laptop" + Keys.RETURN)
     ```
     - Po wprowadzeniu frazy, przejdź do wyników wyszukiwania.

## Krok 4: Sprawdzenie wyników wyszukiwania
1. **Sprawdzenie, czy pojawiły się wyniki wyszukiwania**:
   - Zidentyfikuj sekcję wyników wyszukiwania za pomocą selektora CSS (`.s-main-slot`).
   - **Asercja**: 
     ```python
     assert search_results.is_displayed()
     ```
     - Wyniki wyszukiwania muszą być widoczne na stronie.

## Krok 5: Sprawdzenie przycisku wyszukiwania
1. **Sprawdzenie, czy przycisk wyszukiwania jest widoczny**:
   - Zidentyfikuj przycisk wyszukiwania (z selektorem CSS `input.nav-input[type='submit']`).
   - **Asercja**: 
     ```python
     assert search_button.is_displayed()
     ```
     - Przycisk wyszukiwania musi być widoczny na stronie.

## Krok 6: Sprawdzenie menu nawigacyjnego
1. **Sprawdzenie, czy menu nawigacyjne działa**:
   - Kliknij na menu kategorii (z identyfikatorem `nav-hamburger-menu`).
   - **Asercja**: 
     ```python
     assert driver.find_element(By.ID, "hmenu-content").is_displayed()
     ```
     - Menu nawigacyjne powinno się otworzyć.

## Krok 7: Sprawdzenie linku do "Your Account"
1. **Testowanie linku do "Your Account"**:
   - Zidentyfikuj link do sekcji "Your Account" (z tekstem `Your Account`) i kliknij w niego.
   - **Asercja**: 
     ```python
     assert "Your Account" in driver.title
     ```
     - Powinno otworzyć się nowe okno z tytułem "Your Account".

## Krok 8: Sprawdzenie obecności logo Amazon
1. **Sprawdzenie widoczności logo Amazon**:
   - Zidentyfikuj logo Amazon (z ID `nav-logo`).
   - **Asercja**: 
     ```python
     assert logo.is_displayed()
     ```
     - Logo Amazon musi być widoczne na stronie.

## Krok 9: Zakończenie testu
1. **Zamknięcie przeglądarki**:
   - Po zakończeniu testu zamknij przeglądarkę, aby zakończyć sesję testową.
