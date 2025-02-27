from pytest_playwright.pytest_plugin import (
    browser_name,
    browser_channel,
)
import pytest


def pytest_addoption(parser):
    """Adaugă opțiuni custom pentru rularea testelor."""
    parser.addoption(
        "--browser", action="store", default="chromium", help="Browser implicit"
    )
    parser.addoption("--headed", action="store_true", help="Rulează în mod vizibil")
    parser.addoption(
        "--workers", action="store", default="4", type=int, help="Număr de workeri"
    )
    parser.addoption(
        "--timeout", action="store", default="30000", type=int, help="Timeout global"
    )


@pytest.fixture(scope="session")
def browser_config(pytestconfig):
    """Configurarea implicită a browserului."""
    return {
        "browser": pytestconfig.getoption("--browser"),
        "headed": pytestconfig.getoption("--headed"),
        "workers": 4,
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
