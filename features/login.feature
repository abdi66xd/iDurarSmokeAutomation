# Created by abdias.alpire at 4/4/24
Feature: Login functionality
  @login
  Scenario: Login using valid credentials
    Given I got navigated to the Login page
    When I enter a valid Email
    And I enter a valid Password
    And I click the login button
    Then I should see email on the avatar section

  @negative_login
  Scenario: Login using invalid credentials
    Given I got navigated to the Login page
    When I enter an invalid Email
    Then I should see an email alert

