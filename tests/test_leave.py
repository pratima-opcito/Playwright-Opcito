import pytest

from config.config import USERNAME, PASSWORD
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage
from pages.login_page import LoginPage

@pytest.mark.flaky(retries=2)
def test_leave(page):
    login = LoginPage(page)

    login.navigate()
    login.login(USERNAME, PASSWORD)
    dashboard = DashboardPage(page)

    dashboard.click_on_menu("Leave")
    leave=LeavePage(page)
    leave.click_on_assign_leave()
    leave.assign_leave()
