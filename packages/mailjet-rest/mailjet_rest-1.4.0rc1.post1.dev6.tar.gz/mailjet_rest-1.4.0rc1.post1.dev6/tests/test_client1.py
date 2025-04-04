import unittest
from unittest.mock import patch, Mock

from mailjet_rest.client import Client, api_call


class TestClientAuthentication(unittest.TestCase):
    def setUp(self):
        self.valid_auth = ("valid_api_key", "valid_secret_key")
        self.client = Client(auth=self.valid_auth)

    @patch("requests.get")
    def test_authentication_with_valid_credentials(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = api_call(
            auth=self.valid_auth,
            method="get",
            url="https://api.mailjet.com/v3/",
            headers={"Content-type": "application/json"},
        )

        self.assertEqual(response.status_code, 200)
        mock_get.assert_called_once_with(
            "https://api.mailjet.com/v3/",
            auth=self.valid_auth,
            data=None,
            headers={"Content-type": "application/json"},
            params=None,
            timeout=60,
            verify=True,
            stream=False,
        )


if __name__ == "__main__":
    unittest.main()
