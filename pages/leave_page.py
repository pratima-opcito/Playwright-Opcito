from playwright.sync_api import expect


class LeavePage:

    def __init__(self, page):
        self.page = page


    def click_on_assign_leave(self):
        self.page.locator("a",has_text="Assign Leave").click()

    def assign_leave(self):
        expect(self.page.get_by_placeholder("Type for hints...")).to_be_visible()

