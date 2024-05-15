# Created by abdias.alpire at 22/4/24
Feature: Products Categories management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewProductCategories
  Scenario: Add a simple product category
    Given I am located on the dashboard
    When I click the Products category tab
    And I click Add new Product Category button
    And I fill product category name field
    And I fill product category description field
    And I select a color for product category field
    And I click enable product category combobox
    And I Click Product category Submit button
    Then I should see a success confirmation pop up for the new product category

  @AlertsDisplayedForProductsCategory
Scenario: Alerts displayed when add a product category without filling mandatory fields
  Given I am located on the dashboard
  When I click the products category tab
  And I click Add new Product Category button
  And I Click product category Submit button without filling in required fields
  Then I should see alerts over the Name, Description, Color, and Enabled fields for the Product section