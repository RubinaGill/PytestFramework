from pytest_bdd import scenarios, given, when, then, parsers
import os

from src.pages.upload_page import UploadPage

scenarios('file_upload.feature')

@given("the user is on the file upload page")
def go_to_upload_page(browser, config_data):
    browser.get(config_data["url"]+UploadPage.URL_KEY)

@when(parsers.parse('the user uploads the file "{filename}"'))
def upload_file(browser, filename):
    filepath = os.path.abspath(filename)
    assert os.path.exists(filepath), f"File not found: {filepath}"

    upload_page = UploadPage()
    upload_input = upload_page.get_file_input_element(browser)
    upload_input.send_keys(filepath)

    submit_btn = upload_page.get_upload_button_element(browser)
    submit_btn.click()

@then("the file should be successfully uploaded")
def verify_upload_success(browser):
    upload_page = UploadPage()
    header = upload_page.get_success_message_element(browser).text
    assert "File Uploaded!" in header

    uploaded_file = upload_page.get_result_filename_element(browser).text
    assert uploaded_file.strip() != ""