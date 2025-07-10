from pages.base_page import BasePage

class LoginPage(BasePage):
    URL_KEY = "/login"

    def __init__(self):
        super().__init__("login_page")

    def get_username_element(self, browser):
        return browser.find_element(*self.get_locator("username"))
    
    def get_password_element(self, browser):
        return browser.find_element(*self.get_locator("password"))

    def get_login_button_element(self, browser):
        return browser.find_element(*self.get_locator("login_button"))

    def get_flash_message_element(self, browser):
        return browser.find_element(*self.get_locator("flash_message"))