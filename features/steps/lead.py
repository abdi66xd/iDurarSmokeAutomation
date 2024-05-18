from behave import when, then

from features.pages.DashboardPage import DashboardPage
from features.pages.LeadsPage import LeadPage
from utilities.UniqueDataGenerator import UniqueDataGenerator

data_generator = UniqueDataGenerator()


@when(u'I click the Leads tab')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    context.dashboard_page = dashboard_page
    dashboard_page.click_leads_tab()


@when(u'I click Add new Leads button')
def step_impl(context):
    lead_page = LeadPage(context.driver)
    context.lead_page = lead_page
    context.lead_page.click_add_new_leads_button()


@when(u'I tab the Lead type field')
def step_impl(context):
    lead_page = LeadPage(context.driver)
    context.lead_page = lead_page
    context.lead_page.select_lead_type_field()


@when(u'I tab Lead Status field')
def step_impl(context):
    lead_page = LeadPage(context.driver)
    context.lead_page = lead_page
    context.lead_page.select_lead_status_field()


@when(u'I tab Lead Source field')
def step_impl(context):
    lead_page = LeadPage(context.driver)
    context.lead_page = lead_page
    context.lead_page.select_lead_source_field()


@when(u'I tab Lead People field')
def step_impl(context):
    lead_page = LeadPage(context.driver)
    context.lead_page = lead_page
    context.lead_page.select_lead_people_field()


@when(u'I fill Lead Notes field')
def step_impl(context):
    lead_page = LeadPage(context.driver)
    context.lead_page = lead_page
    unique_note = data_generator.generate_unique_company_name()
    lead_page.fill_notes_field(unique_note)


@when(u'I Click Lead Submit button')
def step_impl(context):
    lead_page = LeadPage(context.driver)
    context.lead_page = lead_page
    context.lead_page.click_submit_new_lead_button()


@then(u'I should see a success confirmation pop up for the new lead')
def step_impl(context):
    lead_page = LeadPage(context.driver)
    context.company_page = lead_page
    assert lead_page.is_lead_submitted_popup_displayed()
