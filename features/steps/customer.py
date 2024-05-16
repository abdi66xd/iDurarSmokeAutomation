from behave import when, then

from features.pages.CustomerPage import CustomerPage
from features.pages.DashboardPage import DashboardPage


@when(u'I click the customers tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_customers_tab()


@when(u'I click Add new client button')
def step_impl(context):
    customer_page = CustomerPage(context.driver)
    context.company_page = customer_page
    customer_page.click_add_new_client_button()


@when(u'I select a people client type')
def step_impl(context):
    customer_page = CustomerPage(context.driver)
    context.company_page = customer_page
    customer_page.select_people_client_type_field()


@when(u'I select a company client type')
def step_impl(context):
    customer_page = CustomerPage(context.driver)
    context.company_page = customer_page
    customer_page.select_company_client_type_field()


@when(u'I select people linked to the client')
def step_impl(context):
    customer_page = CustomerPage(context.driver)
    context.company_page = customer_page
    customer_page.select_people_field()


@when(u'I select a company linked to the client')
def step_impl(context):
    customer_page = CustomerPage(context.driver)
    context.company_page = customer_page
    customer_page.select_company_field()


@when(u'I Click client Submit button')
def step_impl(context):
    customer_page = CustomerPage(context.driver)
    context.company_page = customer_page
    customer_page.click_submit_new_client_button()


@then(u'I should see a 403 error')
def step_impl(context):
    customer_page = CustomerPage(context.driver)
    context.company_page = customer_page
    assert context.company_page.is_client_submitted_popup_displayed()
