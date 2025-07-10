@regression
Feature: Dropdown Selection

  @Dropdown
  Scenario: Select an option from dropdown
    Given the user is on the dropdown page
    When the user selects "Option 2"
    Then "Option 2" should be selected

  @NotImp
  Scenario: Select an option from dropdown1
    Given the user is on the dropdown page
    Then the step should fail
    And this step must be skipped