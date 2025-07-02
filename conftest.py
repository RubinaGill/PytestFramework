import logging
import pytest

from utils import config_loader, driver_factory,logger

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome or firefox"
    )

def pytest_configure(config):
   logger.setup_logging()

def pytest_unconfigure(config):
    logger.finish_logging()


@pytest.fixture(scope='session')
def config_data():
    return config_loader.load_config() 

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    driver = driver_factory.create_browser(browser_name)
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