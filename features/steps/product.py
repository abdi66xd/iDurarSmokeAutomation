from behave import when, then

from features.pages.ProductsPage import ProductsPage
from features.pages.DashboardPage import DashboardPage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the product tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_products_tab()


@when(u'I click Add new Product button')
def step_impl(context):
    product_page = ProductsPage(context.driver)
    context.product_page = product_page
    product_page.click_add_new_product_button()


@when(u'I Fill the Product name field')
def step_impl(context):
    product_page = ProductsPage(context.driver)
    context.product_page = product_page
    unique_product_name = data_generator.generate_unique_product_name()
    product_page.fill_product_name_field(unique_product_name)


@when(u'I Select the Product category field')
def step_impl(context):
    product_page = ProductsPage(context.driver)
    context.product_page = product_page
    product_page.select_product_category_field()


@when(u'I Select the Product EUR currency field')
def step_impl(context):
    product_page = ProductsPage(context.driver)
    context.product_page = product_page
    product_page.select_product_currency_field()


@when(u'I Fill the Product Price field')
def step_impl(context):
    product_price = ProductsPage(context.driver)
    context.product_page = product_price
    unique_product_price = data_generator.generate_unique_product_price()
    product_price.fill_product_price_field(unique_product_price)


@when(u'I Fill the Product Description field')
def step_impl(context):
    product_description = ProductsPage(context.driver)
    context.product_page = product_description
    unique_product_description = data_generator.generate_unique_product_description()
    product_description.fill_product_description_field(unique_product_description)


@when(u'I Fill the Product Ref field')
def step_impl(context):
    product_ref = ProductsPage(context.driver)
    context.product_page = product_ref
    unique_product_ref = data_generator.generate_unique_product_reference()
    product_ref.fill_product_ref_field(unique_product_ref)


@then(u'I Should see a success alert for the product created')
def step_impl(context):
    products_page = ProductsPage(context.driver)
    context.product_page = products_page
    assert products_page.is_product_submitted_popup_displayed()


@then(u'I should see alerts over the Product Name, Product category and Product Price fields for Product category '
      u'section')
def step_impl(context):
    products_page = ProductsPage(context.driver)
    context.product_page = products_page
    assert products_page.is_expenses_category_alerts_displayed()


@when(u'I click product submit button')
def step_impl(context):
    products_page = ProductsPage(context.driver)
    context.product_page = products_page
    products_page.click_submit_new_product_button()
