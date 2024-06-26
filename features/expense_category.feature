# Created by abdias.alpire at 22/4/24
Feature: Expenses Categories management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewExpensesCategories
  Scenario: Add a expense category
    Given I am located on the dashboard
    When I click the expenses category tab
    And I click Add new expense Category button
    And I fill expense category name field
    And I fill expense category description field
    And I select a color for expense category field
    And I click enable expense category combobox
    And I Click expense category Submit button
    Then I should see a success confirmation pop up for the new expense category



  @AlertsDisplayedForExpensesCategory
Scenario: Alerts displayed when add a expense category without filling mandatory fields
  Given I am located on the dashboard
  When I click the expenses category tab
  And I click Add new expense Category button
  And I Click expense category Submit button without filling in required fields
  Then I should see alerts over the Name, Description, Color, and Enabled fields for Expenses category section