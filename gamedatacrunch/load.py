import json

from gamedatacrunch.download import download
from gamedatacrunch.utils import get_cached_database_filename, get_data_folder


def load(file_name=None, url=None):
    if file_name is None:
        file_name = get_data_folder() + get_cached_database_filename()

    try:
        with open(file_name, encoding="utf8") as f:
            data = json.load(f)

    except FileNotFoundError:
        data = download(url=url)

        with open(file_name, "w", encoding="utf8") as f:
            json.dump(data, f)

    del data["cached"]

    return data


def load_app_ids(file_name=None, url=None, verbose=True):
    data = load(file_name=file_name, url=url)

    app_ids = [int(app["i"]) for app_batch in data.values() for app in app_batch]

    app_ids = sorted(app_ids, key=int)

    if verbose:
        print(f"#appIDs = {len(app_ids)}")

    return app_ids


if __name__ == "__main__":
    data = load()
    app_ids = load_app_ids()
