import unittest

import gamedatacrunch


class TestLoadMethods(unittest.TestCase):
    def test_load(self):
        data = gamedatacrunch.load()
        self.assertGreater(len(data), 0)

    def test_load_app_ids(self):
        app_ids = gamedatacrunch.load_app_ids()
        self.assertGreater(len(app_ids), 0)


if __name__ == "__main__":
    unittest.main()
