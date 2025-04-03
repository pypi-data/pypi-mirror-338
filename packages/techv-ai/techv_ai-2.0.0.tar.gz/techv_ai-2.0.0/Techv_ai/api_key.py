import uuid
import json

API_KEY_FILE = "api_keys.json"

def generate_api_key(user_id):
    api_key = f"{user_id}-{uuid.uuid4()}"
    store_api_key(user_id, api_key)
    return api_key

def store_api_key(user_id, api_key):
    try:
        with open(API_KEY_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    data[user_id] = api_key

    with open(API_KEY_FILE, "w") as f:
        json.dump(data, f)

def validate_api_key(api_key):
    try:
        with open(API_KEY_FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    return api_key in data.values()
