from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import scenarios, given, when, then, parsers
import os

from pages.upload_page import UploadPage

scenarios('file_upload.feature')

@given("the user is on the file upload page")
def go_to_upload_page(browser, config_data):
    browser.get(config_data["url"]+UploadPage.URL_KEY)

@when(parsers.parse('the user uploads the file "{filename}"'))
def upload_file(browser, filename):
    filepath = os.path.abspath(filename)
    assert os.path.exists(filepath), f"File not found: {filepath}"

    wait = WebDriverWait(browser, 10)
    upload_input = wait.until(EC.presence_of_element_located(UploadPage.FILE_INPUT))
    upload_input.send_keys(filepath)

    submit_btn = wait.until(EC.element_to_be_clickable(UploadPage.SUBMIT_BUTTON))
    submit_btn.click()

@then("the file should be successfully uploaded")
def verify_upload_success(browser):
    wait = WebDriverWait(browser, 10)
    header = wait.until(EC.presence_of_element_located(UploadPage.HEADER)).text
    assert "File Uploaded!" in header

    uploaded_file = wait.until(EC.presence_of_element_located(UploadPage.RESULT_FILENAME)).text
    assert uploaded_file.strip() != ""