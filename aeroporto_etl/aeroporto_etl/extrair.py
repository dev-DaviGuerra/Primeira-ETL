import os

import requests

from constantes import BASE_URL


def get_endpoint(endpoint, endpoint_id=None, params=None):
    headers = {
        "Accept": "application/json",
        "app_id": os.getenv('APP_ID'),
        "app_key": os.getenv('APP_KEY'),
        "ResourceVersion": "v4"
    }

    url = BASE_URL + endpoint

    if endpoint_id:
        url = url + "/" + endpoint_id
    resultado_get = requests.get(url=url, headers=headers, params=None)

    import ipdb; ipdb.set_trace()

if __name__ == "__main__":
    get_endpoint('flights')