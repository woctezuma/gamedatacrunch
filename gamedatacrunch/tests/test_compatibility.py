import unittest

import gamedatacrunch


class TestCompatibilityMethods(unittest.TestCase):
    def get_dummy_app_id(self):
        dummy_app_id = 730
        return dummy_app_id

    def get_dummy_app_name(self):
        dummy_app_name = "Counter-Strike: Global Offensive"
        return dummy_app_name

    def get_dummy_app_slug(self):
        dummy_app_slug = "counter_strike_global_offensive"
        return dummy_app_slug

    def test_load_as_steam_api(self):
        data = gamedatacrunch.load_as_steam_api()
        self.assertIn("applist", data.keys())
        self.assertIn("apps", data["applist"])
        self.assertGreater(len(data["applist"]["apps"]), 0)

    def test_load_as_steamspy_api(self):
        data = gamedatacrunch.load_as_steamspy_api()
        self.assertGreater(len(data), 0)

    def test_check_app_as_steam_api(self):
        data = gamedatacrunch.load_as_steam_api(include_slug=True)

        # Reference: https://stackoverflow.com/a/9542768
        app_index = next(
            i
            for (i, app) in enumerate(data["applist"]["apps"])
            if app["appid"] == self.get_dummy_app_id()
        )

        app = data["applist"]["apps"][app_index]
        self.assertEqual(app["appid"], self.get_dummy_app_id())
        self.assertEqual(app["name"], self.get_dummy_app_name())
        self.assertEqual(app["slug"], self.get_dummy_app_slug())

    def test_check_app_as_steamsy_api(self):
        data = gamedatacrunch.load_as_steamspy_api(include_slug=True)

        app = data[str(self.get_dummy_app_id())]
        self.assertEqual(app["appid"], self.get_dummy_app_id())
        self.assertEqual(app["name"], self.get_dummy_app_name())
        self.assertEqual(app["slug"], self.get_dummy_app_slug())


if __name__ == "__main__":
    unittest.main()
