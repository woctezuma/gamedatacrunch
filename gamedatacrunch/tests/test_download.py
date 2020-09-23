import unittest

import gamedatacrunch


class TestDownloadMethods(unittest.TestCase):
    def test_get_api_url(self):
        api_url = gamedatacrunch.get_api_url()
        self.assertEqual(api_url, "https://www.gamedatacrunch.com")

    def test_get_api_endpoint(self):
        api_endpoint = gamedatacrunch.get_api_endpoint()
        self.assertEqual(api_endpoint, "/api/steam/catalog")

    def test_download(self):
        data = gamedatacrunch.download()
        self.assertGreater(len(data), 0)


if __name__ == "__main__":
    unittest.main()
