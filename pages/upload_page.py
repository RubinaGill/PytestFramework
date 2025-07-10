from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UploadPage(BasePage):
    URL_KEY = "/upload"
    def __init__(self):
        super().__init__("upload_page")

    def get_file_input_element(self, browser):
        wait = WebDriverWait(browser, 10)
        return wait.until(EC.presence_of_element_located(self.get_locator("file_input")))

    def get_upload_button_element(self, browser):
        wait = WebDriverWait(browser, 10)
        return wait.until(EC.element_to_be_clickable(self.get_locator("submit_button")))

    def get_success_message_element(self, browser):
        wait = WebDriverWait(browser, 10)
        return wait.until(EC.presence_of_element_located(self.get_locator("header")))

    def get_error_message_element(self, browser):
        wait = WebDriverWait(browser, 10)
        return wait.until(EC.presence_of_element_located(self.get_locator("error_message")))

    def get_result_filename_element(self, browser):
        wait = WebDriverWait(browser, 10)
        return wait.until(EC.presence_of_element_located(self.get_locator("result_filename")))
