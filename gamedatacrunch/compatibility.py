from gamedatacrunch.load import load


def load_as_steam_api(file_name=None, url=None, include_slug=False):
    data_as_gdc = load(file_name=file_name, url=url)

    data = dict()
    data["applist"] = dict()
    data["applist"]["apps"] = list()

    for app_batch in data_as_gdc.values():
        for app in app_batch:
            app_id = int(app["i"])
            app_name = app["n"]
            app_slug = app["s"]

            app_dict = dict()
            app_dict["appid"] = app_id
            app_dict["name"] = app_name
            if include_slug:
                app_dict["slug"] = app_slug

            data["applist"]["apps"].append(app_dict)

    return data


def load_as_steamspy_api(file_name=None, url=None, include_slug=False):
    data_as_gdc = load(file_name=file_name, url=url)

    data = dict()

    for app_batch in data_as_gdc.values():
        for app in app_batch:
            app_id = int(app["i"])
            app_name = app["n"]
            app_slug = app["s"]

            app_dict = dict()
            app_dict["appid"] = app_id
            app_dict["name"] = app_name
            if include_slug:
                app_dict["slug"] = app_slug

            app_id_as_str = str(app_id)
            data[app_id_as_str] = app_dict

    return data


if __name__ == "__main__":
    data_as_steam = load_as_steam_api()
    data_as_steamspy = load_as_steamspy_api()
