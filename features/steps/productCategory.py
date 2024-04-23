from behave import given, when, then
from features.pages.DashboardPage import DashboardPage
from features.pages.PeoplePage import PeoplePage
from features.pages.ProductsCategoryPage import ProductsCategoryPage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the Products category tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_products_category_tab()


@when(u'I click Add new Product Category button')
def step_impl(context):
    product_category_page = ProductsCategoryPage(context.driver)
    context.product_category_page = product_category_page
    product_category_page.click_add_new_product_category_button()


@when(u'I fill product category name field')
def step_impl(context):
    product_category_page = ProductsCategoryPage(context.driver)
    context.product_category_page = product_category_page
    unique_product_name = data_generator.generate_unique_product_name()
    product_category_page.fill_product_category_name_field(unique_product_name)


@when(u'I fill product category description field')
def step_impl(context):
    product_category_page = ProductsCategoryPage(context.driver)
    context.product_category_page = product_category_page
    unique_product_description = data_generator.generate_unique_product_description()
    product_category_page.fill_product_category_description_field(unique_product_description)


@when(u'I click enable product category combobox')
def step_impl(context):
    product_category_page = ProductsCategoryPage(context.driver)
    context.product_category_page = product_category_page
    product_category_page.click_enabled_product_category()


@when(u'I Click Product category Submit button')
def step_impl(context):
    product_category_page = ProductsCategoryPage(context.driver)
    context.product_category_page = product_category_page
    product_category_page.click_product_category_submit_button()


@when(u'I select a color for product category field')
def step_impl(context):
    product_category_page = ProductsCategoryPage(context.driver)
    context.product_category_page = product_category_page
    product_category_page.select_color_product_category()


@then(u'I should see a success confirmation pop up for the new product category')
def step_impl(context):
    product_category_page = ProductsCategoryPage(context.driver)
    assert product_category_page.is_product_category_submitted_popup_displayed()
