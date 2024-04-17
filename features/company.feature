# Created by abdias.alpire at 7/4/24
Feature:  Company management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button


@NewCompanyMandatoryFields
Scenario: Add a new Company using only mandatory fields
  Given I am located on the dashboard
  When I click the companies tab
  And I click Add new Company button
  And I Fill the Company Name field
  And I Fill the Company Email field
  And I Click Company Submit button
  Then I should see a success confirmation pop up for the new company

@NewCompanyAllFields
Scenario: Add a new Company using all fields
  Given I am located on the dashboard
  When I click the companies tab
  And I click Add new Company button
  And I Fill the Company Name field
  And I Fill the Company Phone field
  And I Fill the Company Email field
  And I Fill the Company Website field
  And I Click Company Submit button
  Then I should see a success confirmation pop up for the new company
