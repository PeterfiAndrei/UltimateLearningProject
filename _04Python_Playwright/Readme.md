# 1. Create Virtual env
Windows:
- python -m venv venv
- venv\Scripts\activate

MAC: 
- python -m venv venv
- source venv/bin/activate

Check if installed:
- python --version
- pip --version

# 2. Install Playwright for python
1. pip install playwright pytest pytest-playwright
2. playwright install
3. playwright install-deps (not really required)
4. pip install -r requirements.txt (install dependencies)
5. pip freeze > requirements.txt (save dependencies, don't use this unless you do changes to the project)

# 3. Setup playwright.config.py and pytest.ini (add them if they not exist)
1. playwright.config.py:
    ```python
    from pytest_playwright.pytest_plugin import (
        browser_name,
        browser_channel,
    )
    import pytest
    
    def pytest_addoption(parser):
        """Adaugă opțiuni custom pentru rularea testelor."""
        parser.addoption("--browser", action="store", default="chromium", help="Browser implicit")
        parser.addoption("--headed", action="store_true", help="Rulează în mod vizibil")
        parser.addoption("--workers", action="store", default="4", type=int, help="Număr de workeri")
        parser.addoption("--timeout", action="store", default="30000", type=int, help="Timeout global")
    
    @pytest.fixture(scope="session")
    def browser_config(pytestconfig):
        """Configurarea implicită a browserului."""
        return {
            "browser": pytestconfig.getoption("--browser"),
            "headed": pytestconfig.getoption("--headed"),
            "workers":4,
            "timeout": 30000,
            "testIdAttribute": "id",  # Selectează testId implicit
        }
    
    @pytest.fixture(scope="session")
    def browser_context_args(browser_config):
        """Setează timeout-ul implicit și alte configurații globale."""
        return {
            "acceptDownloads": True,
            "viewport": {"width": 1280, "height": 720},
            "recordVideo": {"dir": "test-results/videos"},  # Salvează înregistrări video
            "recordHar": {"path": "test-results/network.har", "mode": "full"},
        }
    
    @pytest.fixture(scope="session")
    def launch_options(browser_config):
        """Setează opțiunile de launch pentru Playwright."""
        return {
            "headless": not browser_config["headed"],
            "timeout": browser_config["timeout"],
        }
    ```
2. pytest.ini:
    ```[pytest]
    testpaths = tests
    addopts = --headed --slowmo 500 --browser=chromium
    log_cli = true
    log_cli_level = INFO
    ```
   
# 4. Run tests
1. using the play button
2. using the terminal, you can pass a few arguments too:

    `pytest tests/test_login.py`

    `pytest tests/test_login.py --browser=firefox --headed`

    `BROWSER=firefox pytest tests/test_login.py`

    `pytest tests/test_login.py::test_valid_login --browser=webkit --timeout=20000 --headed -s -v`


✔️ Explicație:

    ::test_valid_login → Rulează doar acel test
    --browser=webkit → Folosește WebKit
    --timeout=20000 → Timeout de 20 secunde
    --headed → Rulează browserul vizibil
    -s → Afișează print() în consolă
    -v → Mod verbose (afișează testele detaliat)

3. In terminal: `pytest` (will run all tests from the path defined in **pytest.ini** -> `testpaths = tests`)

# 5. Extra fisiere care probabil vor trebui configurate(foloseste chtgbt pentru mai multe detalii):
📌 La ce sunt utile fișierele __init__.py, conftest.py și pytest_plugin.py în Pytest?
În funcție de nevoile tale, unele dintre aceste fișiere sunt obligatorii, iar altele sunt opționale. Hai să vedem ce face fiecare și dacă ai nevoie de ele.

**1️⃣ __init__.py (Face un folder să fie un "Package" Python)**
📌 Rol: Marchează un folder ca fiind un package Python.
✅ Când ai nevoie de el?

Dacă ai teste organizate pe mai multe directoare și vrei să le importezi corect.
Dacă vrei să importezi fișiere între module (from tests.helpers.utils import func).
Dacă ai testele într-un subfolder și vrei să eviți erori de import.
❌ Dacă testele sunt simple și toate fișierele sunt în același folder, atunci poți șterge __init__.py.

**2️⃣ conftest.py (Configurare globală pentru Pytest)**
📌 Rol: Conține fixutres, hooks și configurări globale pentru Pytest.

✅ Când ai nevoie de el?

Dacă ai nevoie de fixtures reutilizabile (ex: setup pentru browser, autentificare).
Dacă vrei să configurezi hooks (ex: setup/teardown global).
Dacă vrei să eviți importuri redundante în fiecare fișier de test.
Exemplu de conftest.py:
```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()
```
📌 Acum, orice test poate folosi browser fără să îl declare manual!

🔥 Dacă folosești Pytest pe un proiect mare, ai nevoie de conftest.py!
❌ Dacă proiectul e mic și nu folosești fixtures/hooks, îl poți șterge.

**3️⃣ pytest_plugin.py (Definirea de plugins personalizate)**
📌 Rol: Extinde funcționalitățile Pytest cu fixtures, hooks sau alte configurații.

✅ Când ai nevoie de el?

Dacă faci un plugin personalizat pentru Pytest.
Dacă vrei să ai un fișier separat pentru fixtures reutilizabile.
Dacă ai multe fixtures și vrei să separi fișierele (pytest_plugins = ["pytest_plugin"] în conftest.py).
📌 Exemplu de pytest_plugin.py:

```python
import pytest

@pytest.fixture
def example_fixture():
    return "Hello from pytest plugin!"
```
📌 Acest fixture poate fi folosit automat în orice test Pytest.

❌ Dacă nu ai nevoie de plugin-uri custom, pytest_plugin.py poate fi șters.
