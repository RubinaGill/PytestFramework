import json

def load_config(filepath='src/testData/user_data.json'):
    with open(filepath, 'r') as file:
        return json.load(file)
