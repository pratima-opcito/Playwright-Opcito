from playwright.sync_api import Page, expect, TimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, selector: str, *, timeout: int = 10000):
        """Click an element located by selector."""
        self.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).click(timeout=timeout)

    def fill(self, selector: str, text: str, *, timeout: int = 10000):
        """Fill input field located by selector with text."""
        self.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).fill(text, timeout=timeout)

    def get_text(self, selector: str, *, timeout: int = 5000) -> str:
        """Get inner text of an element."""
        self.wait_for_element(selector, timeout=timeout)
        return self.page.locator(selector).inner_text(timeout=timeout)

    def is_visible(self, selector: str, *, timeout: int = 5000) -> bool:
        """Check if element is visible on the page."""
        try:
            expect(self.page.locator(selector)).to_be_visible(timeout=timeout)
            return True
        except TimeoutError:
            return False

    def wait_for_element(self, selector: str, *, timeout: int = 10000):
        """Wait until element is visible."""
        expect(self.page.locator(selector)).to_be_visible(timeout=timeout)

    def select_dropdown_option(self, dropdown_selector: str, option_text: str):
        """
        For custom dropdowns (non-<select>): click dropdown and select option by visible text.
        """
        self.click(dropdown_selector)
        option_locator = f"//div[contains(text(), '{option_text}')]"
        self.click(option_locator)

    def upload_file(self, input_selector: str, file_path: str):
        """
        Upload file via input[type='file'] element.
        Works even if the input is hidden.
        """
        self.page.locator(input_selector).set_input_files(file_path)

    def wait_for_navigation(self, url_part: str = None, timeout: int = 10000):
        """Wait for page navigation to complete optionally checking URL contains url_part."""
        self.page.wait_for_load_state("load", timeout=timeout)
        if url_part:
            self.page.wait_for_url(f"**{url_part}**", timeout=timeout)

    def press_key(self, selector: str, key: str, *, timeout: int = 10000):
        """Press a key on an element."""
        self.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).press(key, timeout=timeout)

    def get_attribute(self, selector: str, attribute: str, *, timeout: int = 5000):
        """Get attribute value of an element."""
        self.wait_for_element(selector, timeout=timeout)
        return self.page.locator(selector).get_attribute(attribute)

    def clear_field(self, selector: str, *, timeout: int = 5000):
        """Clear the text of an input field."""
        self.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).fill("", timeout=timeout)

    def scroll_into_view(self, selector: str, *, timeout: int = 5000):
        """Scroll element into view."""
        self.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).scroll_into_view_if_needed(timeout=timeout)
