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


4. **Set up chrome driver**:
   ```bash
   brew install --cask chromedriver
   ```
   This command will install chrome driver needed to execute chrome instances of selenium

5. **Set up gecko driver**:
   ```bash
   brew install geckodriver
   ```
   This command will install gecko driver needed to execute firefox instances of selenium

## Running the Tests

To run the tests, execute the following command:
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ features
```
This command runs the tests using Behave framework and generates Allure reports in the `allure_reports/` directory.

To run a single test case by introducing a tag run the following command:
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure_reports/ -t example_tag features
```


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

## Cleaning the previous runs

To clean the past runs, execute the following command:
```bash
allure generate --clean -o allure_reports/ allure_results/
```
This command will flush the results got on the `allure_reports/` directory.
