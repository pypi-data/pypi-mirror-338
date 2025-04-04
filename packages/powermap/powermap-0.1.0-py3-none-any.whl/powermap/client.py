"""PowerMap API client."""
from typing import List, Dict, Any, Optional, Union
from openlocationcode import openlocationcode as olc
from shapely.geometry import shape, Point
from shapely.validation import make_valid
import requests
import math

from .exceptions import PowerMapError, InvalidGeozoneError, AuthenticationError


class PowerMapClient:
    """Client for accessing PowerMap API services.

    This client provides access to PowerMap's geospatial services, allowing
    users to retrieve grid codes for specific geographic zones.

    Attributes:
        token (str): API token for authentication.
        base_url (str): Base URL for API endpoints.
    """

    def __init__(self, token: str, base_url: str = "https://iso.powermap.workers.dev/"):
        """Initialize PowerMapClient.

        Args:
            token (str): API token for authentication.
            base_url (str, optional): Base URL for API endpoints.
                Defaults to "https://iso.powermap.workers.dev/".
        """
        self.token = token
        self.base_url = base_url

    def grid(self, geozone: str, resolution: float = 0.02) -> List[str]:
        """Generate a grid of plus codes for a geographical zone.

        Args:
            geozone (str): Name of the geographical zone.
            resolution (float, optional): Resolution of the grid in degrees.
                Defaults to 0.02.

        Returns:
            List[str]: List of plus codes within the geographical zone.

        Raises:
            InvalidGeozoneError: If the geozone is invalid or not found.
            AuthenticationError: If authentication fails.
            PowerMapError: For other API-related errors.
        """
        # Fetch geographical data
        data = self._fetch(geozone)

        if data is None:
            raise InvalidGeozoneError(f"Invalid or unknown geozone: {geozone}")

        # Extract geometry
        if "features" in data:
            geometry = data["features"][0]["geometry"]
        elif "geometry" in data:
            geometry = data["geometry"]
        else:
            geometry = data

        # Create and validate shape
        polygon = shape(geometry)
        if not polygon.is_valid:
            polygon = make_valid(polygon)

        # Get bounding box
        minx, miny, maxx, maxy = polygon.bounds

        # Calculate starting points
        start_lat_unstable = math.ceil(miny / resolution) * resolution
        start_lon_unstable = math.ceil(minx / resolution) * resolution

        start_lat = float("{:.4f}".format(start_lat_unstable))
        start_lon = float("{:.4f}".format(start_lon_unstable))

        # Generate points inside polygon
        points_inside = []

        lat = round(start_lat, 4)
        while lat <= maxy:
            lon = round(start_lon, 4)
            while lon <= maxx:
                point = Point(lon, lat)
                if polygon.contains(point):
                    points_inside.append(olc.encode(lat, lon))
                lon += resolution
                lon = round(lon, 4)
            lat += resolution
            lat = round(lat, 4)

        return points_inside

    def _fetch(self, geozone: str) -> Optional[Dict[str, Any]]:
        """Fetch geographical data for a zone.

        This is an internal method not intended for direct use.

        Args:
            geozone (str): Name of the geographical zone.

        Returns:
            Optional[Dict[str, Any]]: JSON response data or None if request failed.

        Raises:
            AuthenticationError: If authentication fails.
            PowerMapError: For other API-related errors.
        """
        params = {"filename": geozone, "token": self.token}

        try:
            response = requests.get(self.base_url, params=params)

            if response.status_code == 401:
                raise AuthenticationError("Invalid API token")
            elif response.status_code == 404:
                return None
            elif response.status_code != 200:
                raise PowerMapError(
                    f"API error: {response.status_code} - {response.text}")

            return response.json()
        except requests.RequestException as e:
            raise PowerMapError(f"Request failed: {str(e)}")
