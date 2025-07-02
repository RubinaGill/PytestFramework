# Selenium Automation Project

This project is a Python-based automation framework using Selenium WebDriver. It is designed for automating web application testing and generating test reports.

## Features

- Automated browser testing with Selenium
- Test report and log generation
- Support for multiple environments
- Easy configuration and extensibility
## Project Structure

```
SeleniumAutomationProject/
├── reports/           # Test reports
├── tests/             # Test cases
├── features/          # BDD feature files
├── src/               # Source code and utilities
├── seleniumenv/       # Virtual environment (ignored)
├── conftest.py        # Pytest configuration and fixtures
├── pytest.ini         # Pytest settings
├── Dockerfile         # Docker build instructions
├── Jenkinsfile        # Jenkins CI/CD pipeline
├── .gitignore         # Git ignore rules
├── requirements.txt   # Python dependencies
└── README.md          #
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
   pytest
   ```

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

## Requirements

- Python 3.7+
- Selenium
- pytest

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.
