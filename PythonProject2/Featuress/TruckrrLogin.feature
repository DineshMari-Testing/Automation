Feature: Login Truckrr web
  Background: Common Steps

  Scenario: Login and verifying logo
    Given launch browser
    When launch truckrr one browser
    When Enter "demotruckrr@gmail.com" and "Demo@123"
    When skip two step verification page

 Scenario: Adding Customer
    When Need to add customer
    And click add customer to add
    When Entering customer details
    Then Close Browser