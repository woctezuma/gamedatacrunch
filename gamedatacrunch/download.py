import requests


def get_api_url():
    return "https://www.gamedatacrunch.com"


def get_api_endpoint():
    return "/api/steam/catalog"


def download(url=None):
    if url is None:
        url = get_api_url() + get_api_endpoint()

    response = requests.get(url=url)

    return response.json() if response.ok else None


if __name__ == "__main__":
    data = download()
