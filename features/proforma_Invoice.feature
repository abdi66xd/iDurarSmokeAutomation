Feature: Proforma Invoice management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewProformaInvoice
  Scenario: Add a proforma invoice
  Given I am located on the dashboard
  When I click the proforma invoice tab
  And I click Add new proforma invoice button
  And I Select client proforma invoice dropdown
  And I fill the proforma item name field
  And I fill the proforma item quantity field
  And I fill the proforma item price field
  And I Select tax proforma invoice dropdown
  And I click proforma invoice submit button
  Then I Should see a success alert for the proforma invoice created


  @ProformaInvoiceAlerts
  Scenario: Alerts displayed when add a invoice without filling mandatory fields
  Given I am located on the dashboard
  When I click the proforma invoice tab
  And I click Add new proforma invoice button
  And I click proforma invoice submit button
  Then I should see alerts over the Client,Item, Quantity, Price and Tax fields for proforma invoice section