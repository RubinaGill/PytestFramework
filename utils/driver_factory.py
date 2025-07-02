import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.environment import is_running_in_docker

def create_browser(browser_name):
    if browser_name == "chrome":
        options = Options()
        if is_running_in_docker():
            logging.info("Running in Docker, using headless Chrome")
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if is_running_in_docker():
            logging.info("Running in Docker, using headless Firefox")
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    logging.info(f"Launching Browser: {browser_name}")
    return driver
