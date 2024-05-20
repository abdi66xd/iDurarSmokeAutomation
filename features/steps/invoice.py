from behave import when, then
from features.pages.CompanyPage import CompanyPage
from features.pages.DashboardPage import DashboardPage
from features.pages.InvoicePage import InvoicePage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the invoice tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_invoices_tab()


@when(u'I click Add new invoice button')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    invoice_page.click_add_new_invoice_button()


@when(u'I Select client invoice dropdown')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    invoice_page.select_client_invoice_field()


@when(u'I fill the item name field')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    unique_item_name = data_generator.generate_unique_product_name()
    invoice_page.fill_item_name_field(unique_item_name)


@when(u'I fill the item quantity field')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    unique_item_quantity = data_generator.generate_unique_product_price()
    invoice_page.fill_item_name_field(unique_item_quantity)


@when(u'I fill the item price field')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    unique_item_price = data_generator.generate_unique_product_price()
    invoice_page.fill_item_price_field(unique_item_price)


@when(u'I Select tax invoice dropdown')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    invoice_page.select_client_tax_field()


@when(u'I click invoice submit button')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    invoice_page.click_submit_new_invoice_button()


@then(u'I Should see a success alert for the invoice created')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    assert invoice_page.is_invoice_submitted_popup_displayed()


@when(u'I click add new item button ')
def step_impl(context):
    invoice_page = InvoicePage(context.driver)
    context.invoice_page = invoice_page
    invoice_page.click_new_item_button()
