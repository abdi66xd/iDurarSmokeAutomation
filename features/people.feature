Feature: People management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button


@NewPersonCreated
Scenario: Add a new person with all fields
  Given I am located on the dashboard
  When I click the people tab
  And I click Add new Person button
  And I Fill the Firstname field
  And I Fill the Lastname field
  And I Fill the Phone field
  And I Fill the Email field
  And I Click Submit new person button
  Then I Should see a success alert for the person created



@NewPersonOnlyMandatoryFields
Scenario: Add Only Mandatory Fields
  Given I am located on the dashboard
  When I click the people tab
  And I click Add new Person button
  And I Fill the Firstname field
  And I Fill the Lastname field
  And I Click Submit new person button
  Then I Should see a success alert for the person created