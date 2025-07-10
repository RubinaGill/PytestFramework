import os
import json
def load_locators(page_name):
    locators_path=os.path.join("testData", "locators", f"{page_name}_locators.json")
    with open(locators_path,'r') as file:
        return json.load(file)