# in features/steps/login_steps.py
from time import sleep

from behave import given, when, then

from features.pages.DashboardPage import DashboardPage
from features.pages.LoginPage import LoginPage
from utilities import ConfigReader


@given(u'I got navigated to the Login page')
def step_impl(context):
    login_page = LoginPage(context.driver)
    context.login_page = login_page


@when(u'I enter a valid Email')
def step_impl(context):
    context.login_page.fill_email_field(ConfigReader.read_configuration("Admin Account", "email"))


@when(u'I enter a valid Password')
def step_impl(context):
    context.login_page.fill_password_field(ConfigReader.read_configuration("Admin Account", "password"))


@when(u'I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then(u'I should see email on the avatar section')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_avatar_icon()
    dashboard_mail = dashboard_page.catch_mail_name()
    assert dashboard_mail, ConfigReader.read_configuration("Admin Account", "email")


@when(u'I enter an invalid Email')
def step_impl(context):
    context.login_page.fill_email_field("invalid_email@example.com")


@when(u'I enter an invalid Password')
def step_impl(context):
    context.login_page.fill_password_field("invalid_password")


@then(u'I should see an alert')
def step_impl(context):
    # Add verification steps to check if an alert is displayed
    pass
