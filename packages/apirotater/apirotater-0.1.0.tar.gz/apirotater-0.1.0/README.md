# APIRotater

A Python library for rotating API keys to help prevent rate limit issues.

## Features

- Manage multiple API keys
- Sequential rotation
- Track API key usage counts
- Reserve keys for specific number of uses
- Set time-based rate limits for each key
- Automatically load API keys from .env file
- Helper functions and decorators
- Smart fallback mechanism for continuous operation

## Installation

```bash
pip install apirotater
```

## Usage Examples

### Creating a .env File

Create a `.env` file in your root directory and add your API keys in the following format:

```
API_KEY_1=your_first_api_key_here
API_KEY_2=your_second_api_key_here
API_KEY_3=your_third_api_key_here
```

The library will automatically load all API keys defined with the API_KEY_* pattern in your .env file.

### Basic Usage

```python
from apirotater import APIKeyManager

# Create an API key manager
manager = APIKeyManager()

# API keys are automatically loaded from .env file

# Get all API keys
all_keys = manager.get_all_keys()
print(f"All available API keys: {all_keys}")

# Get an API key
api_key = manager.get_api_key()
print(f"API key to use: {api_key}")

# Make your API request (Add your own API call here)
# ...

# Report usage
manager.hit(api_key)

# Get usage statistics
stats = manager.get_usage_stats()
print(f"Usage statistics: {stats}")
```

### Reserving Keys for Multiple Uses

```python
# Get an API key for 5 uses
api_key = manager.get_api_key(usage_count=5)

# Make API requests
for _ in range(5):
    # Make your API request (Add your own API call here)
    # ...
    
    # Report each usage
    manager.hit(api_key)
```

### Using Helper Functions

```python
from apirotater.utils import with_api_key

def make_api_request(param1, param2, api_key=None):
    # Make your API request here
    print(f"Making API request: {param1}, {param2}, API key: {api_key}")
    return "API response"

# API key will be automatically added
result = with_api_key(manager, make_api_request, "param1_value", "param2_value")
print(result)

# Reserve key for 3 uses
result = with_api_key(manager, make_api_request, "param1_value", "param2_value", usage_count=3)
print(result)
```

### Request Throttling

```python
from apirotater.utils import APIThrottler

# Maximum 60 requests per minute
throttler = APIThrottler(rate_limit=60, time_period=60)

for _ in range(100):
    # Will wait if needed
    throttler.wait_if_needed()
    
    # Make your API request
    # ...
```

### Time-Based Rate Limits

```python
from apirotater import APIKeyManager
import time

# Create an API key manager
manager = APIKeyManager()

# Get all API keys
all_keys = manager.get_all_keys()

# Set rate limits: first key can only be used 5 times in 60 seconds
manager.set_rate_limit(all_keys[0], time_window=60, max_uses=5)

# You can set multiple time windows for the same key
manager.set_rate_limit(all_keys[0], time_window=3600, max_uses=100)  # 100 times per hour

# Make API requests
for i in range(10):
    # This will automatically switch to another key after the first key hits its limit
    api_key = manager.get_api_key()
    
    # Make your API request
    # ...
    
    # Report usage
    manager.hit(api_key)
```

### Continuous Operation

The library ensures continuous operation by implementing a smart fallback system:

1. First, it tries to find an available key that isn't reserved or rate-limited
2. If all keys are reserved/limited, it selects the least used key that isn't rate-limited
3. If all keys are rate-limited, it falls back to the overall least used key

This ensures your application keeps running even when rate limits are reached.

```python
# Set strict rate limits
for key in manager.get_all_keys():
    manager.set_rate_limit(key, time_window=60, max_uses=5)

# Even with strict limits, your application keeps running
for i in range(100):
    api_key = manager.get_api_key()
    # Use the API key...
    manager.hit(api_key)
```

## License

MIT 