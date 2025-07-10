from selenium.webdriver.common.by import By
from utils.locator_loader import load_locators

class BasePage:
    BY_MAPPING = {
        "id": By.ID,
        "name": By.NAME,
        "css selector": By.CSS_SELECTOR,
        "xpath": By.XPATH,
        "class name": By.CLASS_NAME,
        "tag name": By.TAG_NAME,
        "link text": By.LINK_TEXT,
        "partial link text": By.PARTIAL_LINK_TEXT
    }

    def __init__(self, page_name):
        self.locators = load_locators(page_name)

    def get_locator(self, locator_key):
        locator = self.locators.get(locator_key)
        if not locator:
            raise ValueError(f"Locator '{locator_key}' not found")
        by = self.BY_MAPPING[locator["by"].lower()]
        value = locator["value"]
        return (by, value)
