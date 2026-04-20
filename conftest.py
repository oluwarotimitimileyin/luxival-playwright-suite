"""
Playwright + pytest configuration for luxival.vercel.app.
pytest-playwright provides the browser/context/page fixtures automatically.
--browser chromium|firefox|webkit  (default: chromium)
--headed                            (default: headless)
--slowmo <ms>                       (default: 0)
"""
import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage


@pytest.fixture(scope="session")
def base_url():
    return "https://luxival.vercel.app"


@pytest.fixture
def home_page(page, base_url):
    return HomePage(page, base_url).load()


@pytest.fixture
def contact_page(page, base_url):
    return ContactPage(page, base_url).load()
