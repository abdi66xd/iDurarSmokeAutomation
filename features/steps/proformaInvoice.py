from behave import when, then
from features.pages.CompanyPage import CompanyPage
from features.pages.DashboardPage import DashboardPage
from features.pages.InvoicePage import InvoicePage
from features.pages.ProformaInvoicePage import ProformaInvoicePage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the proforma invoice tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_proforma_invoices_tab()


@when(u'I click Add new proforma invoice button')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    proforma_invoice_page.click_add_new_proforma_invoice_button()


@when(u'I Select client proforma invoice dropdown')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    proforma_invoice_page.select_client_proforma_invoice_field()


@when(u'I fill the proforma item name field')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    unique_item_name = data_generator.generate_unique_product_name()
    proforma_invoice_page.fill_proforma_item_name_field(unique_item_name)


@when(u'I fill the proforma item quantity field')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    unique_item_quantity = data_generator.generate_unique_product_price()
    proforma_invoice_page.fill_proforma_item_quantity_field(unique_item_quantity)


@when(u'I fill the proforma item price field')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    unique_item_price = data_generator.generate_unique_product_price()
    proforma_invoice_page.fill_proforma_item_price_field(unique_item_price)


@when(u'I Select tax proforma invoice dropdown')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    proforma_invoice_page.select_proforma_client_tax_field()


@when(u'I click proforma invoice submit button')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    proforma_invoice_page.click_submit_new_proforma_invoice_button()


@then(u'I Should see a success alert for the proforma invoice created')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    assert proforma_invoice_page.is_proforma_invoice_submitted_popup_displayed()


@when(u'I click add new proforma item button')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    proforma_invoice_page.click_new_proforma_item_button()


@then(u'I should see alerts over the Client,Item, Quantity, Price and Tax fields for proforma invoice section')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    assert proforma_invoice_page.are__proforma_invoice_alerts_displayed()


@when(u'I click the options of the first row for proforma invoice list')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    proforma_invoice_page.click_options_proforma_list()


@when(u'I click download button for proforma invoice list')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    proforma_invoice_page.click_options_proforma_list()


@then(u'I should download the PDF for proforma invoice list')
def step_impl(context):
    proforma_invoice_page = ProformaInvoicePage(context.driver)
    context.proforma_invoice_page = proforma_invoice_page
    proforma_invoice_page.is_proforma_pdf_downloaded()
