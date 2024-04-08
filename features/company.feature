# Created by abdias.alpire at 7/4/24
Feature:  Company management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button


@NewPersonMandatoryFields
Scenario: Add a new person
  Given I am located on the dashboard
  When I click the companies tab
  And I click Add new Company button
  And I Fill the Name field
  And I select a Contact from Contact field
  And I select a Country from Country field
  And I Fill the Phone field
  And I Fill the Email field
  And I Fill the Website field
  And I Click Submit button
  Then I should see the submitted information on a new row of People list table


