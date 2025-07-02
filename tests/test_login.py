from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import LoginPage

scenarios('login.feature')

@given("the user is on the login page")
def open_login_page(browser, config_data):
    browser.get(config_data["url"]+LoginPage.URL_KEY)

@when(parsers.parse('the user logs in with username "{username}" and password "{password}"'))
def login_with_credentials(browser, username, password):
    username_elem = browser.find_element(*LoginPage.USERNAME)
    username_elem.clear()
    username_elem.send_keys(username)
    password_elem = browser.find_element(*LoginPage.PASSWORD)
    password_elem.clear()
    password_elem.send_keys(password)
    browser.find_element(*LoginPage.LOGIN_BUTTON).click()
    
@then("the user should be redirected to the secure area")
def verify_secure_area(browser):
    assert "/secure" in browser.current_url, f"Expected '/secure' in URL, got {browser.current_url}"

@then("a success message should be displayed")
def verify_success_message(browser):
    flash = browser.find_element(*LoginPage.FLASH_MESSAGE).text
    assert "You logged into a secure area!" in flash, f"Expected success message not found in: {flash}"

@then("an error message should be displayed")
def verify_error_message(browser):
    flash = browser.find_element(*LoginPage.FLASH_MESSAGE).text
    assert "Your username is invalid!" in flash or "Your password is invalid!" in flash, f"Expected error message not found in: {flash}"
