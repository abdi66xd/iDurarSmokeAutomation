Feature: Offer management

Background:
  Given I got navigated to the Login page
  When I enter a valid Email
  And I enter a valid Password
  And I click the login button

  @NewOffer
  Scenario: Add an offer
  Given I am located on the dashboard
  When I click the offer tab
  And I click Add new offer button
  And I Select lead offer dropdown
  And I fill the offer item name field
  And I fill the offer item quantity field
  And I fill the offer item price field
  And I Select offer tax dropdown
  And I click offer submit button
  Then I Should see a success alert for the offer created


  @OfferAlerts
  Scenario: Alerts displayed when add a invoice without filling mandatory fields
  Given I am located on the dashboard
  When I click the offer tab
  And I click Add new offer button
  And I click offer submit button
  Then I should see alerts over the Client,Item, Quantity, Price and Tax fields for offer section

  @DownloadPDFOffer
  Scenario: Download a  Invoice pdf
  Given I am located on the dashboard
  When I click the offer tab
  And I click the options of the first row for offer list
  And I click download button for offer list
  Then I should download the PDF for offer list