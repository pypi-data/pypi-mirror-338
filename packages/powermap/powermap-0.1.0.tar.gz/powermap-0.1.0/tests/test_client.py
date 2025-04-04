"""Tests for PowerMap client."""
import unittest
from unittest.mock import patch, Mock
from powermap import PowerMapClient, InvalidGeozoneError, PowerMapError


class TestPowerMapClient(unittest.TestCase):
    """Test cases for PowerMapClient."""

    def setUp(self):
        """Set up test fixtures."""
        self.client = PowerMapClient(token="test_token")
        self.sample_geometry = {
            "type": "Polygon",
            "coordinates": [
                [
                    [-95.5, 29.5],
                    [-95.5, 30.0],
                    [-95.0, 30.0],
                    [-95.0, 29.5],
                    [-95.5, 29.5]
                ]
            ]
        }
        self.sample_feature = {
            "features": [
                {
                    "type": "Feature",
                    "geometry": self.sample_geometry
                }
            ]
        }

    @patch("powermap.client.requests.get")
    def test_fetch_success(self, mock_get):
        """Test successful data fetch."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_feature
        mock_get.return_value = mock_response

        result = self.client._fetch("test_zone")
        self.assertEqual(result, self.sample_feature)
        mock_get.assert_called_once()

    @patch("powermap.client.requests.get")
    def test_fetch_invalid_zone(self, mock_get):
        """Test fetch with invalid zone."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = self.client._fetch("invalid_zone")
        self.assertIsNone(result)

    @patch("powermap.client.requests.get")
    def test_grid_success(self, mock_get):
        """Test grid generation."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_feature
        mock_get.return_value = mock_response

        points = self.client.grid("test_zone", resolution=0.1)
        self.assertIsInstance(points, list)
        self.assertGreater(len(points), 0)
        # All points should be plus codes
        for code in points:
            self.assertIsInstance(code, str)
            self.assertGreater(len(code), 6)

    @patch("powermap.client.requests.get")
    def test_grid_invalid_zone(self, mock_get):
        """Test grid with invalid zone."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(InvalidGeozoneError):
            self.client.grid("invalid_zone")


if __name__ == "__main__":
    unittest.main()