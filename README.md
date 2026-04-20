# Luxival Playwright Web UI Suite

Playwright + Python + pytest test suite for [luxival.vercel.app](https://luxival.vercel.app).

Complements the [Cypress E2E suite](https://github.com/oluwarotimitimileyin/luxival-qa-cypress-suite) and [Selenium suite](https://github.com/oluwarotimitimileyin/Selenium-web-UI-suite) with cross-browser UI testing via Playwright's native browser engines.

## Test Coverage

| Suite | File | Tests | Focus |
|---|---|---|---|
| Homepage | `test_homepage.py` | 12 | Page load, title, nav, hero, service cards, footer, performance |
| Contact Form | `test_contact_form.py` | 12 | Field presence, input, validation, keyboard interaction |

## Stack

- Python 3.9+
- Playwright 1.43+
- pytest 8.x
- pytest-playwright 0.5+
- Browsers: Chromium (default), Firefox, WebKit

## Setup

```bash
pip install -r requirements.txt
playwright install
```

## Run

```bash
# All tests (headless, chromium)
pytest

# Headed (visible browser)
pytest --headed

# Firefox
pytest --browser firefox

# WebKit (Safari engine)
pytest --browser webkit

# All browsers
pytest --browser chromium --browser firefox --browser webkit

# Slow motion (useful for debugging)
pytest --headed --slowmo 500

# Single suite
pytest tests/test_homepage.py
pytest tests/test_contact_form.py

# With HTML report
pytest --html=report.html --self-contained-html
```

## Project Structure

```
luxival-playwright-suite/
├── conftest.py               # base_url, home_page, contact_page fixtures
├── pytest.ini                # pytest config
├── requirements.txt
├── pages/
│   ├── base_page.py          # Shared Playwright Page helpers
│   ├── home_page.py          # Homepage Page Object
│   └── contact_page.py       # Contact Page Object
└── tests/
    ├── test_homepage.py
    └── test_contact_form.py
```

## Key Playwright Advantages Over Selenium

- **Auto-wait**: Playwright waits for elements to be actionable before interacting — no `WebDriverWait` boilerplate
- **WebKit support**: Tests run against Safari's rendering engine
- **Built-in network interception**: `page.route()` for mocking/stubbing API calls
- **Keyboard API**: `page.keyboard.press()` for realistic user interaction tests
- **`validationMessage`**: Native JS evaluation for HTML5 form validation introspection

## Author

Olakunle Shopeju — [github.com/oluwarotimitimileyin](https://github.com/oluwarotimitimileyin)
