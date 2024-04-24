from behave import when, then
from features.pages.CompanyPage import CompanyPage
from features.pages.DashboardPage import DashboardPage
from features.pages.ExpensesCategoryPage import ExpensesCategoryPage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the expenses category tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_expenses_category_tab()


@when(u'I click Add new expense Category button')
def step_impl(context):
    expenses_category_page = ExpensesCategoryPage(context.driver)
    context.product_category_page = expenses_category_page
    expenses_category_page.click_add_new_expenses_category_button()


@when(u'I fill expense category name field')
def step_impl(context):
    expenses_category_page = ExpensesCategoryPage(context.driver)
    context.product_category_page = expenses_category_page
    unique_expense_name = data_generator.generate_unique_expense_name()
    expenses_category_page.fill_expenses_category_name_field(unique_expense_name)


@when(u'I fill expense category description field')
def step_impl(context):
    expenses_category_page = ExpensesCategoryPage(context.driver)
    context.product_category_page = expenses_category_page
    unique_expense_description = data_generator.generate_unique_expense_description()
    expenses_category_page.fill_expenses_category_description_field(unique_expense_description)


@when(u'I select a color for expense category field')
def step_impl(context):
    expenses_category_page = ExpensesCategoryPage(context.driver)
    context.product_category_page = expenses_category_page
    expenses_category_page.select_color_expenses_category()


@when(u'I click enable expense category combobox')
def step_impl(context):
    expenses_category_page = ExpensesCategoryPage(context.driver)
    context.product_category_page = expenses_category_page
    expenses_category_page.click_enabled_expenses_category()


@when(u'I Click expense category Submit button')
def step_impl(context):
    expenses_category_page = ExpensesCategoryPage(context.driver)
    context.product_category_page = expenses_category_page
    expenses_category_page.click_expenses_category_submit_button()


@then(u'I should see a success confirmation pop up for the new expense category')
def step_impl(context):
    expenses_category_page = ExpensesCategoryPage(context.driver)
    assert expenses_category_page.is_expenses_category_submitted_popup_displayed()
