from behave import given, when, then
from features.pages.DashboardPage import DashboardPage
from features.pages.PeoplePage import PeoplePage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@given(u'I am located on the dashboard')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    logo = dashboard_page.is_logo_loaded()
    assert logo


@when(u'I click the people tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_people_tab()


@when(u'I click Add new Person button')
def step_impl(context):
    people_page = PeoplePage(context.driver)
    people_page.click_add_new_person()


@when(u'I Fill the Firstname field')
def step_impl(context):
    people_page = PeoplePage(context.driver)
    unique_first_name = data_generator.generate_unique_name()
    people_page.fill_people_firstname_field(unique_first_name)


@when(u'I Fill the Lastname field')
def step_impl(context):
    people_page = PeoplePage(context.driver)
    unique_last_name = data_generator.generate_unique_lastname()
    people_page.fill_people_lastname_field(unique_last_name)


@when(u'I Fill the Phone field')
def step_impl(context):
    people_page = PeoplePage(context.driver)
    unique_phone_number = data_generator.generate_unique_phone_number()
    people_page.fill_people_phone_field(unique_phone_number)


@when(u'I Fill the Email field')
def step_impl(context):
    people_page = PeoplePage(context.driver)
    unique_email = data_generator.generate_unique_email()
    people_page.fill_people_email_field(unique_email)


@when(u'I Click Submit new person button')
def step_impl(context):
    people_page = PeoplePage(context.driver)
    people_page.click_submit_new_person_button()


@then("I Should see a success alert for the person created")
def step_impl(context):
    people_page = PeoplePage(context.driver)
    assert people_page.is_people_submitted_popup_displayed()