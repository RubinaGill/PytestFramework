import json
import logging
import pytest
import allure
import os
import shutil
from datetime import datetime

from src.utils import config_loader, driver_factory,logger

feature_tags = set()

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
    feature_tags.update(feature.tags)
    allure.dynamic.parent_suite(next(iter(feature_tags), feature.name))
    allure.dynamic.title(f"{feature.name} - {scenario.name}")
    allure.dynamic.feature(feature.name)  
    allure.dynamic.story(scenario.name) 

    logging.info(f"🚀 START Scenario: {scenario.name} in Feature: {feature.name}")

def pytest_bdd_after_scenario(request, feature, scenario):
    logging.info(f"✅ END Scenario: {scenario.name}")

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    logging.info(f"➡️  STEP: {step.keyword} {step.name}")

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    logging.info(f"✅ Completed: {step.name}")

def capture_screenshot(driver, step_name):
    screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{step_name}_{timestamp}.png"
    file_path = os.path.join(screenshot_dir, file_name)

    driver.save_screenshot(file_path)


    with open(file_path, "rb") as image_file:
        allure.attach(
            image_file.read(),
            name=file_name,
            attachment_type=allure.attachment_type.PNG
        )   

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    logging.error(f"❌ Step failed: {step.name} - {exception}")
    driver = request.getfixturevalue("browser")
    if driver:
        capture_screenshot(driver, step.name)

def detect_executor():
    # Jenkins detection
    if os.getenv('JENKINS_URL') or os.getenv('BUILD_URL'):
        return "Jenkins"

    # Docker detection (several common ways)
    if os.path.exists('/.dockerenv'):
        return "Docker"

    # cgroup-based Docker detection (for newer Docker versions)
    try:
        with open('/proc/1/cgroup', 'rt') as f:
            if 'docker' in f.read() or 'kubepods' in f.read():
                return "Docker"
    except FileNotFoundError:
        pass

    # Default to local
    return "Local Terminal"

def copy_previous_history():
    if os.path.exists('allure-report/history'):
        shutil.copytree('allure-report/history', 'allure-results/history', dirs_exist_ok=True)

def pytest_sessionstart(session):
    copy_previous_history()
    executor_type = detect_executor()

    # Example: write executor.json for Allure
    executor_info = {
        "name": executor_type,
        "type": executor_type,
        "url": os.getenv('BUILD_URL', 'N/A'),
        "buildOrder": 1,
        "buildName": os.getenv('BUILD_NAME', 'manual-run'),
        "reportUrl": os.getenv('ALLURE_REPORT_URL', 'N/A')
    }

    os.makedirs('reports/allure-results', exist_ok=True)

    with open('reports/allure-results/executor.json', 'w') as f:
        json.dump(executor_info, f, indent=2)

    print(f"✔️ Detected Executor: {executor_type}")

def pytest_sessionfinish(session, exitstatus):
    config = session.config
    browser_name = getattr(config, "option", None)
    browser_name = None
    try:
        browser_name = config.getoption("--browser")
    except Exception:
        browser_name = "chrome" 

    env_dir = os.path.join(os.getcwd(), "reports", "allure-results")
    os.makedirs(env_dir, exist_ok=True)
    env_file = os.path.join(env_dir, "environment.properties")

    with open(env_file, "w") as f:
        f.write(f"Browser={browser_name}\n")
        f.write(f"Marker={feature_tags}\n")
        f.write("By=Rubina Gill\n")