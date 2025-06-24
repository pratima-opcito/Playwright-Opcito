# pages/dashboard_page.py

class DashboardPage:
    def __init__(self, page):
        self.page = page

    def click_menu_item(self, item_text):
        """Click on a menu item by visible text."""
        self.page.get_by_role("link", name=item_text).click()

    def verify_dashboard_navigation(self):
        """Click through each top-level menu item."""
        menu_items = [
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",

            "Claim",
            "Buzz"
        ]

        for item in menu_items:
            self.click_menu_item(item)

    # Optional: individual method for specific menu if needed
    def click_on_admin(self):
        self.click_menu_item("PIM")
