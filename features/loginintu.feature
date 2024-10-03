Feature: Login Feature Intu
  Scenario: Successful login with valid credentials
    Given the user is on the login page of the application
    When the user logs in with valid credentials (username and password)
    Then the user should be redirected to the dashboard page of the application