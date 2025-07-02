import json
import logging
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome or firefox"
    )

def pytest_configure(config):
   os.makedirs("reports", exist_ok=True)

   logging.basicConfig(
         level=logging.INFO,
         format='%(asctime)s - %(levelname)s - %(message)s',
         handlers=[
             logging.FileHandler('reports/suite.log'),
             logging.StreamHandler()
         ]
    )
   logging.info("======== Test Session Started ========")

def pytest_unconfigure(config):
    logging.info("======== Test Session Finished ========")  


@pytest.fixture(scope='session')
def config_data():
       with open('user_data.json', 'r') as file:
            return json.load(file)    

def is_running_in_docker():
     return os.environ.get('IN_DOCKER','false').lower() == 'true'   

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = Options()

        if is_running_in_docker():
            logging.info("Running in Docker, using headless mode")
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if is_running_in_docker():
            logging.info("Running in Docker, using headless mode")
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    logging.info(f"Launching Browser: {browser_name}")
    yield driver
    logging.info("Closing browser")
    driver.quit()



def pytest_bdd_before_scenario(request, feature, scenario):
    logging.info(f"🚀 START Scenario: {scenario.name} in Feature: {feature.name}")

def pytest_bdd_after_scenario(request, feature, scenario):
    logging.info(f"✅ END Scenario: {scenario.name}")

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    logging.info(f"➡️  STEP: {step.keyword} {step.name}")

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    logging.info(f"✅ Completed: {step.name}")

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    logging.error(f"❌ Step failed: {step.name} - {exception}")