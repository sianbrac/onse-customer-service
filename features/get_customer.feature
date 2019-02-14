Feature: Get the customer based on id
  As a service I want to get the customer details so that I can check whether they exist.

  Scenario: Fetching existing customer
    Given customer "Nicole Forsgren" with ID "12345" exists
    When I fetch customer "12345"
    Then I should see customer "Nicole Forsgren"

  Scenario: Fetching customer which doesn't exist
    Given there is no customer with ID "99999"
    When I fetch customer "99999"
    Then I should get a not found response

  Scenario: Update Customer
    Given customer "Nicole Forsgren" with ID "12345" exists
    When customer "12345" surname is updated to "Brown"
    Then customer "12345" surname is changed to "Brown"
