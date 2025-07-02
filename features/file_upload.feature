Feature: File Upload Functionality

  @FileUpload
  Scenario: Upload a valid file
    Given the user is on the file upload page
    When the user uploads the file "testData/user_data.json"
    Then the file should be successfully uploaded
