from pages.base_page import BasePage

class DropdownPage(BasePage):
    URL_KEY = "/dropdown"

    def __init__(self):
        super().__init__("dropdown_page")

    def get_select_element(self, browser):
        return browser.find_element(*self.get_locator("select_box"))
