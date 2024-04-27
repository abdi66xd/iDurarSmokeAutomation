# Installation Guide

## Setting up Selenium with Python (python 3.12 needed)

1. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```
   This command will create a virtual environment named `venv` in your project directory.

2. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```
   Activating the virtual environment will ensure that all subsequent Python and pip commands are executed within this isolated environment.

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```
   This command will install all the required packages listed in the `requirements.txt` file.

## Running the Tests

To run the tests, execute the following command:
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ features
```
This command runs the tests using Behave framework and generates Allure reports in the `allure_reports/` directory.

## Viewing the Allure Report

1. **Install Allure**:
   If Allure is not already installed, you can install it using Homebrew:
   ```bash
   brew install allure
   ```

2. **Run the Report**:
   After installing Allure, run the following command to view the Allure report:
   ```bash
   allure serve allure_reports/
   ```
   This command serves the Allure report, allowing you to view it in your web browser.
