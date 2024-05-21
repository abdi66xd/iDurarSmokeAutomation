from behave import when, then
from features.pages.DashboardPage import DashboardPage
from features.pages.OffersPage import OffersPage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the offer tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_offers_tab()


@when(u'I click Add new offer button')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.click_add_new_offer_button()


@when(u'I Select lead offer dropdown')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.select_lead_offer_field()


@when(u'I fill the offer item name field')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    unique_offer_name = data_generator.generate_unique_product_name()
    offer_page.fill_offer_item_name_field(unique_offer_name)


@when(u'I fill the offer item quantity field')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.fill_offer_item_quantity_field()


@when(u'I fill the offer item price field')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.fill_offer_item_price_field()


@when(u'I Select offer tax dropdown')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.select_offer_tax_field()


@when(u'I click offer submit button')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.click_submit_new_offer_button()


@then(u'I Should see a success alert for the offer created')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.is_offer_submitted_popup_displayed()


@then(u'I should see alerts over the Client,Item, Quantity, Price and Tax fields for offer section')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.are_offer_alerts_displayed()


@when(u'I click the options of the first row for offer list')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.click_options_offer_list()


@when(u'I click download button for offer list')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.click_download_offer_option()


@then(u'I should download the PDF for offer list')
def step_impl(context):
    offer_page = OffersPage(context.driver)
    context.offer_page = offer_page
    offer_page.is_offer_pdf_downloaded()
