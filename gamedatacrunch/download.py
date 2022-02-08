import requests
import pandas as pd
import json
from config.topgames.segmentations import *

class

def get_api_url():
    api_url = api_url_address
    return api_url


def get_api_endpoint():
    api_endpoint = api_top_performing_endpoint_all_fields
    return api_endpoint


def download(url=None):
    if url is None:
        url = get_api_url() + get_api_endpoint()

    response = requests.get(url=url)

    if response.ok:
        data = response.json()
        json_data = json.loads(response.text)
    else:
        data = None

    print(data)
    return data





if __name__ == "__main__":
    data = download()
