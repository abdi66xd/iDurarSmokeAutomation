# Created by abdias.alpire at 22/4/24
Feature: Customer management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewCustomerPeople
  Scenario: Add a new people customer people
    Given I am located on the dashboard
    When I click the customers tab
    And I click Add new client button
    And I select a people client type
    And I select people linked to the client
    And I Click client Submit button
    Then I should see a 403 error

  @NewCustomerCompany
  Scenario: Add a new people customer company
    Given I am located on the dashboard
    When I click the customers tab
    And I click Add new client button
    And I select a company client type
    And I select a company linked to the client
    And I Click client Submit button
    Then I should see a 403 error

