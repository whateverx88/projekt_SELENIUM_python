# 1. Opis projektu

Celem projektu jest przetestowanie podstawowych funkcjonalności strony internetowej – rejestracji i logowania użytkownika. W tym celu opracowano 5 podstawowych przypadków testowych dla strony „https://demowebshop.tricentis.com/”:

- TC1: Rejestracja użytkownika bez podania imienia 
- TC2: Poprawna rejestracja nowego użytkownika
- TC3: Rejestracja użytkownika z już istniejącym adresem e-mail
- TC4: Poprawne logowanie istniejącego użytkownika
- TC5: Logowanie z błędnym hasłem

W niniejszej pracy zastosowano wzorzec projektowy Page Object Model (POM).

Projekt został przygotowany na maszynie wirtualnej z wykorzystaniem Oracle VM VirtualBox (wersja 7.2.2), uruchomionej na środowisku macOS Tahoe 26.4 na architekturze ARM (Apple M1). Jako system gościnny wykorzystano Ubuntu 24.04 LTS.

Zastosowanie architektury ARM stanowiło dodatkowe wyzwanie ze względu na ograniczoną kompatybilność niektórych narzędzi testowych oraz sterowników przeglądarek. W celu rozwiązania tych problemów wykorzystano Docker wraz z obrazami Selenium, co umożliwiło uruchamianie testów w izolowanym środowisku kontenerowym, niezależnym od architektury systemu hosta.

Takie podejście pozwoliło na stabilne uruchamianie testów automatycznych oraz zapewniło większą powtarzalność i przenoszalność środowiska testowego.

---

# 2. Wymagania

Projekt wymaga:

- Python 3.12.3+
- Selenium WebDriver

## Instalacja zależności

```bash

pip install -r requirements.txt

```

---

# 3. Uruchamianie testów

Uruchomienie wszystkich testów:

```bash

python test_runner.py

```

Po zakończeniu wykonywania testów generowany jest raport HTML w folderze:

```text

/reports

```

---

# 4. Przypadki testowe

## TC1: Rejestracja użytkownika bez podania imienia

Sprawdzenie, czy system poprawnie waliduje wymagane pole „imię” i wyświetla odpowiedni komunikat błędu w przypadku jego braku.

---

## TC2: Poprawna rejestracja nowego użytkownika

Weryfikacja, czy użytkownik może poprawnie zarejestrować konto przy użyciu prawidłowych danych oraz czy system wyświetla komunikat potwierdzający rejestrację.

---

## TC3: Rejestracja użytkownika z już istniejącym adresem e-mail

Sprawdzenie, czy system blokuje rejestrację przy użyciu wcześniej zarejestrowanego adresu e-mail i wyświetla odpowiedni komunikat błędu.

---

## TC4: Poprawne logowanie istniejącego użytkownika

Weryfikacja, czy użytkownik może zalogować się przy użyciu poprawnych danych logowania oraz czy zostaje poprawnie uwierzytelniony w systemie.

---

## TC5: Logowanie z błędnym hasłem

Sprawdzenie, czy system odrzuca próbę logowania przy użyciu nieprawidłowego hasła i wyświetla odpowiedni komunikat błędu.

# 5. Technologie

W projekcie wykorzystano:

- Python
- Selenium WebDriver
- unittest
- HtmlTestRunner
- Docker
- Oracle VM VirtualBox
- Ubuntu 24.04 LTS