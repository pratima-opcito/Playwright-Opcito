import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def browser(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    context=browser.new_context()
    page=context.new_page()
    yield page
    context.close()
