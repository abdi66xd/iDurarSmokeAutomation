from behave import when, then
from features.pages.CompanyPage import CompanyPage
from features.pages.DashboardPage import DashboardPage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the companies tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_companies_tab()


@when(u'I click Add new Company button')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    company_page.click_add_new_company_button()


@when(u'I Fill the Company Name field')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    unique_company_name = data_generator.generate_unique_company_name()
    company_page.fill_company_name_field(unique_company_name)


@when(u'I Fill the Company Email field')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    unique_company_email = data_generator.generate_unique_email()
    company_page.fill_company_email_field(unique_company_email)


@when(u'I Click Company Submit button')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    company_page.click_submit_new_company_button()


@when(u'I select a Company Contact from Contact field')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    company_page.select_company_contact_field()


@when(u'I select a Company Country from Country field')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    company_page.select_company_country_field()


@when(u'I Fill the Company Phone field')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    unique_company_phone = data_generator.generate_unique_phone_number()
    company_page.fill_company_phone_field(unique_company_phone)


@when(u'I Fill the Company Website field')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    unique_company_website = data_generator.generate_unique_website()
    company_page.fill_company_website_field(unique_company_website)


@then(u'I should see a success confirmation pop up for the new company')
def step_impl(context):
    company_page = CompanyPage(context.driver)
    context.company_page = company_page
    assert company_page.is_company_submitted_popup_displayed()
