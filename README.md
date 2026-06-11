# Self-Healing Test Automation Framework

> An AI-powered Selenium framework that auto-heals broken locators and credentials — zero manual fixes required.

**Team:** Think Infinite Agents
**Members:** Sri Varshini R · Arthi K · Karthika Devi S

---

## Overview

UI tests break whenever developers rename element IDs or class names. Traditional test suites require manual updates to every affected locator — a slow, error-prone process.

This framework solves that. It detects broken locators at runtime, scans the live page HTML, picks the best available locator, and rewrites the locator JSON automatically — so the test continues without human intervention. Wrong credentials are handled the same way.

---

## Features

- **Auto-heals broken locators** — detects `NoSuchElement` errors and replaces the broken locator on the fly
- **Smart locator priority** — scans page HTML and picks the best match using `id > name > css > xpath` order
- **Skips false matches** — ignores hidden and CSRF fields to avoid bad substitutions
- **Credential self-healing** — detects "Invalid credentials" errors, resets login data, and retries automatically
- **Persistent healing** — updates `login_locators.json` so fixes survive across test runs
- **HTML reports** — generate full test reports with `pytest --html=report.html`

---

## Tech Stack

| Technology | Version |
|---|---|
| Python | 3.13 |
| Selenium | 4.6+ |
| BeautifulSoup | latest |
| Pytest | latest |

---

## Project Structure

```
self-healing-framework/
│
├── ai/
│   ├── llm_client.py          # LLM integration client
│   └── prompt_builder.py      # Prompt construction for AI healing
│
├── core/
│   ├── config.py              # Global configuration
│   ├── driver_factory.py      # WebDriver setup & teardown
│   ├── element_actions.py     # Wrapped Selenium actions with healing hooks
│   ├── locator_engine.py      # HTML scanning & locator selection logic
│   └── self_healing_engine.py # Core healing orchestration
│
├── locators/
│   └── login_locators.json    # Locator store (auto-updated on heal)
│
├── tests/
│   └── test_login.py          # Test scenarios
│
├── conftest.py                # Pytest fixtures & setup
├── run.py                     # Entry point for running tests
└── requirements.txt           # Python dependencies
```

---

## How Self-Healing Works

```
1. Test Runs
   └─ find_element() called with stored locator

2. Element Not Found
   └─ NoSuchElement or not-interactable error raised

3. Scan Page HTML
   └─ BeautifulSoup parses the current page source

4. Best Locator Found
   └─ Priority: id > name > css > xpath

5. JSON Updated
   └─ login_locators.json auto-rewritten with new locator

6. Test Continues
   └─ Element found, action performed, test passes
```

**Credential Self-Healing:**
If login fails with "Invalid credentials" → `reset_credentials()` rewrites `login_locators.json` → page reloads → retry (attempt 2 of 2).

---

## Test Scenarios

| # | Scenario | Result | Description |
|---|---|---|---|
| 01 | Normal Login | ✅ PASS | All locators correct — logs in and reaches dashboard |
| 02 | Wrong Password | 🔧 HEALED | Invalid credentials detected → auto-reset → retry → pass |
| 03 | Broken Username Locator | 🔧 HEALED | `BROKEN_FIELD` in JSON → HTML scan → correct locator found → JSON updated → pass |
| 04 | Broken Button Locator | 🔧 HEALED | Wrong XPath for login button → healed to working XPath → pass |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/srivarshinirajeshkanna/Self-healing-Selenium-.git
cd self-healing-framework

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
# Run all tests
python run.py

# Run with verbose output
pytest tests/test_login.py -v -s

# Run and generate HTML report
pytest --html=report.html
```

---

## Live Demo

[https://srivarshinirajeshkanna.github.io/Self-healing-Selenium-/](https://srivarshinirajeshkanna.github.io/Self-healing-Selenium-/)

---

## Key Takeaways

- **Zero Manual Fixes** — broken locators and wrong credentials are resolved automatically at runtime
- **Smart Healing Logic** — skips CSRF/hidden fields; uses strict locator priority order
- **Clean Architecture** — fully modular design with config, engine, actions, and tests separated
- **6 Scenarios Tested** — covers normal login, wrong credentials, broken locators, page failures, and report generation

---

*Think Infinite Agents — Built with Python, Selenium, BeautifulSoup & Pytest*
