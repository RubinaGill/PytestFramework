@regression
Feature: Login Functionality

@smoke
Scenario: Successful login with valid credentials
  Given the user is on the login page
  When the user logs in with username "tomsmith" and password "SuperSecretPassword!"
  Then the user should be redirected to the secure area
  And a success message should be displayed

Scenario Outline: Login with invalid credentials
  Given the user is on the login page
  When the user logs in with username "<username>" and password "<password>"
  Then an error message should be displayed

  Examples:
    | username     | password         |
    | wrong        | wrongpass        |
    | tomsmith     | invalidpass      |