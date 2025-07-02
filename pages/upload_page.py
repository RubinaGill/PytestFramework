from selenium.webdriver.common.by import By

class UploadPage:
    URL_KEY = "/upload"
    FILE_INPUT = (By.ID, "file-upload")
    SUBMIT_BUTTON = (By.ID, "file-submit")
    HEADER = (By.TAG_NAME, "h3")
    RESULT_FILENAME = (By.ID, "uploaded-files")
