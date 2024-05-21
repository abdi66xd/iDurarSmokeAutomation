Feature: Invoice management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewInvoice
  Scenario: Add an invoice
  Given I am located on the dashboard
  When I click the invoice tab
  And I click Add new invoice button
  And I Select client invoice dropdown
  And I fill the item name field
  And I fill the item quantity field
  And I fill the item price field
  And I Select tax invoice dropdown
  And I click invoice submit button
  Then I Should see a success alert for the invoice created


  @InvoiceAlerts
  Scenario: Alerts displayed when add a invoice without filling mandatory fields
  Given I am located on the dashboard
  When I click the invoice tab
  And I click Add new invoice button
  And I click invoice submit button
  Then I should see alerts over the Client,Item, Quantity, Price and Tax fields for invoice section