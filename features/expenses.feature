Feature: Expenses management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewDollarExpense
  Scenario: Add a dollar cost expense
  Given I am located on the dashboard
  When I click the expense tab
  And I click Add new expense button
  And I Fill the expense name field
  And I Select the expense category field
  And I Fill the expense Price field
  And I Fill the expense Description field
  And I Fill the expense Ref field
  And I click expense submit button
  Then I Should see a success alert for the expense created


  @NewEURExpense
  Scenario: Add a EUR cost expense
  Given I am located on the dashboard
  When I click the expense tab
  And I click Add new expense button
  And I Fill the expense name field
  And I Select the expense category field
  And I Select the expense currency field
  And I Fill the expense Price field
  And I Fill the expense Description field
  And I Fill the expense Ref field
  And I click expense submit button
  Then I Should see a success alert for the expense created


  @AlertsDisplayedForProduct
  Scenario: Alerts displayed when add a expense without filling mandatory fields
  Given I am located on the dashboard
  When I click the expense tab
  And I click Add new expense button
  And I click expense submit button
  Then I should see alerts over the Expense Name, Expense category and Expense Price fields for expense section


  @ExpensesTranslatedSpanish
  Scenario: Expenses labels translated to spanish
  Given I am located on the dashboard
  And I have selected spanish language on language dropdown
  When I click the expense tab
  And I click on the options menu for the first row of expenses list
  And I click show option on the options menu
  Then I should see the labels of the row translated to spanish