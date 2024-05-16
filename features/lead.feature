Feature:  Lead management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button


@NewLeadAll
Scenario: Add a new Lead tabs
  Given I am located on the dashboard
  When I click the Leads tab
  And I click Add new Leads button
  And I tab the Lead type field
  And I tab Lead Status field
  And I tab Lead Source field
  And I tab Lead People field
  And I fill Lead Notes field
  And I Click Lead Submit button
  Then I should see a success confirmation pop up for the new lead
