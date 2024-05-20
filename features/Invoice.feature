Feature: Invoice management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewInvoice
  Scenario: Add a new invoice
  Given I am located on the dashboard
  When I click the invoice tab
  And I click Add new invoice button
  And I Select client invoice dropdown
  And I fill the item name field
  And I fill the item quantity field
  And I fill the item price field
  And I click add new item button
  And I Select tax invoice dropdown
  And I click invoice submit button
  Then I Should see a success alert for the invoice created
