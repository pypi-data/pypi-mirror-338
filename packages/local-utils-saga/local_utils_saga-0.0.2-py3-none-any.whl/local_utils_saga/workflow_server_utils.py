import json
import os

# Add this after the existing initializations
ASSET_IDS_FILE = "asset_ids.json"

# Initialize asset IDs storage
def load_asset_ids():
    if os.path.exists(ASSET_IDS_FILE):
        try:
            with open(ASSET_IDS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_asset_id(user_id: str, asset_name: str, asset_id: str):
    asset_ids = load_asset_ids()
    key = f"{user_id}_{asset_name}"
    asset_ids[key] = asset_id
    with open(ASSET_IDS_FILE, 'w') as f:
        json.dump(asset_ids, f)

def get_asset_id(user_id: str, asset_name: str) -> str:
    asset_ids = load_asset_ids()
    key = f"{user_id}_{asset_name}"
    return asset_ids.get(key)
