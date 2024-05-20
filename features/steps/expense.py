from behave import when, then

from features.pages.ExpensesPage import ExpensesPage
from features.pages.ProductsPage import ProductsPage
from features.pages.DashboardPage import DashboardPage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the expense tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_expenses_tab()


@when(u'I click Add new expense button')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    expense_page.click_add_new_expense_button()


@when(u'I Fill the expense name field')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    unique_expense_name = data_generator.generate_unique_expense_name()
    expense_page.fill_expense_name_field(unique_expense_name)


@when(u'I Select the expense category field')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    expense_page.select_expense_category_field()


@when(u'I Fill the expense Price field')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    unique_product_price = data_generator.generate_unique_product_price()
    expense_page.fill_expense_price_field(unique_product_price)


@when(u'I Fill the expense Description field')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    unique_expense_desc = data_generator.generate_unique_expense_description()
    expense_page.fill_expense_description_field(unique_expense_desc)


@when(u'I Fill the expense Ref field')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    unique_expense_ref = data_generator.generate_unique_product_reference()
    expense_page.fill_expense_ref_field(unique_expense_ref)


@when(u'I click expense submit button')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    expense_page.click_submit_new_expense_button()


@then(u'I Should see a success alert for the expense created')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    assert expense_page.is_expense_submitted_popup_displayed()


@when(u'I Select the expense currency field')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    expense_page.select_expense_currency_field()


@then(u'I should see alerts over the Expense Name, Expense category and Expense Price fields for expense section')
def step_impl(context):
    expense_page = ExpensesPage(context.driver)
    context.expenses_page = expense_page
    assert expense_page.is_expenses_alerts_displayed()


