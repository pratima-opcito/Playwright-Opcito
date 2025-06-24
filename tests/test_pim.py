import pytest

from config.config import USERNAME, PASSWORD
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.pim_page import PimPage

@pytest.mark.smoke
def test_pim(page):
    login = LoginPage(page)

    login.navigate()
    login.login(USERNAME, PASSWORD)
    dashboard= DashboardPage(page)
    dashboard.verify_dashboard_navigation()
    dashboard.click_on_menu("PIM")
    pim=PimPage(page)
    pim.employee_information()
