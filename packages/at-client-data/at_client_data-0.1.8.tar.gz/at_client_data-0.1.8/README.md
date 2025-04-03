# AT Client Data

A Python client library for accessing AT Data API services.

## Installation

```bash
pip install at-client-data
```

## Usage

```python
import asyncio
from at_client_data import CoreClient

async def main():
    # Initialize client
    async with CoreClient() as client:
        # Make API calls
        data = await client.get_data()
        print(data)

if __name__ == "__main__":
    asyncio.run(main())
```

## Features

- Async API client with automatic retries
- Support for both core and external AT data endpoints
- Context manager support
- Singleton pattern to avoid multiple connections 
