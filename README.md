# ROV_client

Zadanie rekrutacyjne do KN Robocik. Klient dla serwera zdefiniowanego [tu](https://gitlab.com/KNRobocik/knrobocik-software-rekrutacja).

## Uruchomienie

Przed pierwszym uruchomieniem należy zainstalować [python3](https://www.python.org/), [pip](https://pypi.org/project/pip/) oraz zależności:

```bash
pip install -r requirements.txt
```

Klienta uruchomić można komendą:

```bash
python main.py
```

Klient wysyła zapytania na adres http://localhost:8000, gdzie powinno się wcześniej uruchomić serwer.

## Sterowanie

... odbywa się przy pomocy klawiszy strzałek.

## Testy

```bash
pip install -r requirements_tests.txt # instalacja zależności dla testów
pytest tests/test.py -vv # uruchomienie testów
coverage run --source=src -m pytest --junitxml=report.xml tests/test.py # generacja raportu (1)
coverage html #generacja raportu (2)
```
