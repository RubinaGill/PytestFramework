# Selenium Automation Project

This project is a Python-based automation framework using Selenium WebDriver. It is designed for automating web application testing and generating test reports.

## Features

- Automated browser testing with Selenium
- Modular Page Object Model (POM)
- Centralized locators in JSON files
- Pytest-BDD for Gherkin-style scenarios
- Test report and log generation
- Support for multiple environments
- Docker-ready for isolated test execution
- Jenkins pipeline integration
- Easy configuration and extensibility
## Project Structure

```
SeleniumAutomationProject/
├── reports/               # Test reports
├── tests/                 # Test cases (BDD step definitions)
├── features/              # Gherkin .feature files
├── src/
│   ├── pages/             # Page Object classes
│   ├── utils/             # Utilities like locator loaders
│   └── testData/locators/ # JSON locator files
├── seleniumenv/           # Virtual environment (ignored)
├── conftest.py            # Pytest configurations & fixtures
├── pytest.ini             # Pytest settings
├── Dockerfile             # Docker build instructions
├── Jenkinsfile            # Jenkins CI/CD pipeline
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
└── README.md              # Project description
```

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd SeleniumAutomationProject
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv seleniumenv
   source seleniumenv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run tests:**
   ```sh
   pytest --browser=chrome --alluredir=reports/allure-results
   ```

## Locator Management
   - All page locators are stored in JSON files under `src/testData/locators/`.

   - Example locator file (`login_page_locators.json`):

   ```json
   {
   "username": { "by": "id", "value": "username" },
   "password": { "by": "id", "value": "password" },
   "login_button": { "by": "css selector", "value": "button.radius" }
   }
   ```

   - Locators are loaded in page classes through a shared BasePage class.

## Running with Docker

You can also build and run the project using Docker:

1. **Build the Docker image:**
   ```sh
   docker build -t bdd-tests .
   ```

2. **Run the tests in a Docker container:**
   ```sh
   docker run --rm -v "$PWD:/app" -e PYTEST_MARK=smoke bdd-tests
   ```

## CI/CD

- Jenkins pipeline (Jenkinsfile) to automate builds and test execution.

- Easily integrates into most CI/CD environments.

## Requirements

- Python 3.7+
- Selenium
- pytest

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.
