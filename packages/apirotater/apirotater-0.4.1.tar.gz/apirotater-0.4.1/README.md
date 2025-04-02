# APIRotater

APIRotater is a Python library that helps you manage your API keys and control rate limits. By managing multiple API keys, it automatically performs key rotation in case of rate limit exceedance.

## Key Features

- **Automatic API Key Rotation:** Uses multiple API keys in rotation.
- **Rate Limit Control:** You can set a maximum number of uses for each API key within a specific time window.
- **Automatic .env File Loading:** Automatically loads API keys from .env files located in the current working directory or parent directory.
- **Usage Statistics:** Tracks usage counts of API keys.
- **RateLimitExceeded Exception:** Throws an error when all keys have exceeded their rate limit.

## Installation

```bash
pip install apirotater
```

## Usage

Define your API keys in a `.env` file as follows:

```
API_KEY_1=your_api_key_1
API_KEY_2=your_api_key_2
API_KEY_3=your_api_key_3
```

### Basic Usage

```python
import apirotater

# Get an API key
api_key = apirotater.key()

# Make API request
# ...

# Report API key usage
apirotater.hit(api_key)
```

### Usage With Rate Limit

```python
import apirotater

# Get a key with maximum 2 uses in 60 seconds
api_key = apirotater.key(time_window=60, max_uses=2)

# Make API request
# ...

# Report API key usage
apirotater.hit(api_key)
```

### Handling Rate Limit Exceedance

```python
import apirotater
import time

try:
    # Get a key with rate limit
    api_key = apirotater.key(time_window=60, max_uses=2)
    
    # Make API request
    # ...
    
    # Report API key usage
    apirotater.hit(api_key)
    
except apirotater.RateLimitExceeded as e:
    print(f"Rate limit exceeded: {e}")
    # Wait for a while and try again
    time.sleep(60)
```

## API

- `key(time_window=60, max_uses=100)`: Gets an API key (with rate limit)
- `hit(api_key)`: Reports API key usage
- `usage()`: Returns usage statistics for all keys
- `get_all_keys()`: Lists all loaded API keys

## License

MIT 