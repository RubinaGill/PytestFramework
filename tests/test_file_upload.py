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

    upload_input = browser.find_element(*UploadPage.FILE_INPUT)
    upload_input.send_keys(filepath)

    browser.find_element(*UploadPage.SUBMIT_BUTTON).click()

@then("the file should be successfully uploaded")
def verify_upload_success(browser):
    header = browser.find_element(*UploadPage.HEADER).text
    assert "File Uploaded!" in header

    uploaded_file = browser.find_element(*UploadPage.RESULT_FILENAME).text
    assert uploaded_file.strip() != ""
