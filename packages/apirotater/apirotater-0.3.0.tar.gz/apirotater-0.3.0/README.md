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
- Direct module-level API access
- Short syntax aliases for common operations

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


### Usage
```python

import time
import apirotater #import apirotater

#Get a available API key and set rate limit as 15 requests per 60 seconds
api_key = apirotater.key(time_window=60, max_uses=15)

try:

    #your code here

    apirotater.hit(api_key) #report usage to apirotater

    """
    apirotater will automatically rotate to a new API key 
    until there are no more available API keys 
    according to the rate limit set by apirotater.key().
    When a key is available again apirotater will pass the key to app automatically.
    """

except apirotater.RateLimitExceeded as e: #catch if there are no more available API keys
    print(e)
    time.sleep(10) #or do anything else you want

```