import os

def get_endpoint(endpoint, endpoint_id=None, params=None):
    headers = {
        "Accept": "application/json",
        "app_id": os.getenv('APP_ID'),
        "app_key": os.getenv('APP_KEY'),
        "ResourceVersion": "v4"
    }


if __name__ == "__main__":
    get_endpoint('flights')