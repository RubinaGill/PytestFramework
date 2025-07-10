import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import shutil
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from src.utils.environment import is_running_in_docker

def create_browser(browser_name):
    if browser_name == "chrome":
        options = Options()
        if is_running_in_docker():
            logging.info("Running in Docker, using headless Chromium")
            options.binary_location = "/usr/bin/chromium"
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            driver_path = "/usr/bin/chromedriver"
        else:
            logging.info("Running outside Docker, using regular Chrome")
            options.add_argument('--start-maximized')
            driver_path = shutil.which("chromedriver")
            if not driver_path:
                raise FileNotFoundError("ChromeDriver not found in PATH. Please install it or add to PATH.")

        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)

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
