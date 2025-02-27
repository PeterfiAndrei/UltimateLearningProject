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