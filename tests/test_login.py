# tests/test_login.py

from pages.login_page import LoginPage
from config.config import USERNAME, PASSWORD

def test_login_valid_credentials(page):
    login = LoginPage(page)
    login.navigate()
    login.login(USERNAME, PASSWORD)


    assert page.url != "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", "Login failed"
