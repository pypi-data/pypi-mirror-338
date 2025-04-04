# PowerMap

A Python client for PowerMap geospatial API services.

## Installation

```bash
pip install powermap
```

## Usage

```python
from powermap import PowerMapClient

# Initialize client with your API token
client = PowerMapClient(token="your_api_token")

# Get grid of plus codes for a geographical zone
codes = client.grid(geozone="ercot_rto", resolution=0.02)
print(f"Found {len(codes)} locations in the zone")
```

## Authentication

To use this client, you need a valid API token. Contact PowerMap to obtain your token.

## Features

- Generate grids of plus codes for geographical zones
- Configurable resolution for grid generation
- Professional error handling
- Simple, intuitive API

## License

MIT
