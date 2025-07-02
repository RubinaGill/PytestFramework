@regression
Feature: Dropdown Selection

  @Dropdown
  Scenario: Select an option from dropdown
    Given the user is on the dropdown page
    When the user selects "Option 2"
    Then "Option 2" should be selected
