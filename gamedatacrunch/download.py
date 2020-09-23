import requests


def get_api_url():
    api_url = "https://www.gamedatacrunch.com"

    return api_url


def get_api_endpoint():
    api_endpoint = "/api/steam/catalog"

    return api_endpoint


def download(url=None):
    if url is None:
        url = get_api_url() + get_api_endpoint()

    response = requests.get(url=url)

    if response.ok:
        data = response.json()
    else:
        data = None

    return data


if __name__ == "__main__":
    data = download()
