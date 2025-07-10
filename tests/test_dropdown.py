from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support.ui import Select

from pages.dropdown_page import DropdownPage

scenarios('dropdown.feature')

@given("the user is on the dropdown page")
def go_to_dropdown_page(browser, config_data):
    browser.get(config_data["url"]+DropdownPage.URL_KEY)

@then("the step should fail")
def step_should_fail():
    assert False, "This step is expected to fail"

@then("this step must be skipped")
def step_should_be_skipped():
    pass   

@when(parsers.parse('the user selects "{option_text}"'))
def select_option(browser, option_text):
    try:
        select_element = browser.find_element(*DropdownPage.SELECT_BOX)
        select = Select(select_element)
        select.select_by_visible_text(option_text)
    except (NoSuchElementException, UnexpectedTagNameException) as e:
        assert False, f"Dropdown interaction failed: {e}"

@then(parsers.parse('"{option_text}" should be selected'))
def verify_option_selected(browser, option_text):
    try:
        select_element = browser.find_element(*DropdownPage.SELECT_BOX)
        select = Select(select_element)
        assert select.first_selected_option.text == option_text
    except (NoSuchElementException, UnexpectedTagNameException) as e:
        assert False, f"Dropdown interaction failed: {e}"