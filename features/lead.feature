Feature:  Lead management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button


@NewLeadMandatory
Scenario: Add a new lead using only mandatory fields
  Given I am located on the dashboard
  When I click the Leads tab
  And I click Add new Leads button
  And I select the lead type field
  And I Click Lead Submit button
  Then I should see a success confirmation pop up for the new lead

@NewLeadAll
Scenario: Add a new Lead using all fields
  Given I am located on the dashboard
  When I click the Leads tab
  And I click Add new Leads button
  And I select the Lead type field
  And I select Lead Status field
  And I select Lead Source field
  And I click Lead People field
  And I fill Lead Notes field
  And I Click Lead Submit button
  Then I should see a success confirmation pop up for the new lead
