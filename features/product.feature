Feature: Product management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewDollarProduct
  Scenario: Add a dollar cost product
  Given I am located on the dashboard
  When I click the product tab
  And I click Add new Product button
  And I Fill the Product name field
  And I Select the Product category field
  And I Fill the Product Price field
  And I Fill the Product Description field
  And I Fill the Product Ref field
  And I click product submit button
  Then I Should see a success alert for the product created


  @NewEURProduct
  Scenario: Add a EUR cost product
  Given I am located on the dashboard
  When I click the product tab
  And I click Add new Product button
  And I Fill the Product name field
  And I Select the Product category field
  And  I Select the Product EUR currency field
  And I Fill the Product Price field
  And I Fill the Product Description field
  And I Fill the Product Ref field
  And I click product submit button
  Then I Should see a success alert for the product created


  @AlertsDisplayedForProduct
  Scenario: Alerts displayed when add a product without filling mandatory fields
  Given I am located on the dashboard
  When I click the product tab
  And I click Add new Product button
  And I click product submit button
  Then I should see alerts over the Product Name, Product category and Product Price fields for Product category section