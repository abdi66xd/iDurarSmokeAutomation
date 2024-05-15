# Created by abdias.alpire at 22/4/24
Feature: Customer management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewCustomer
  Scenario: Add a new customer
    Given I am located on the dashboard
    When I click the customers tab
    And I click Add new client button
    And I select a client type
    And I select people linked to the client
    And I select a company linked to the client
    And I Click client Submit button
    Then I should see a success confirmation pop up for the new client created



  @AlertsDisplayedForNewCustomer
Scenario: Alerts displayed when add a expense category without filling mandatory fields
  Given I am located on the dashboard
  When I click the expenses category tab
  And I click Add new expense Category button
  And I Click expense category Submit button without filling in required fields
  Then I should see alerts over the Name, Description, Color, and Enabled fields for Expenses category section