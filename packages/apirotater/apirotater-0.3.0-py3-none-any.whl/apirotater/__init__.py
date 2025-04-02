from .manager import APIKeyManager, RateLimitExceeded
import os
from dotenv import load_dotenv

# Try to load environment variables
def _load_environment():
    # Try to find .env file in current directory, 
    # parent directory, or user's home directory
    possible_locations = [
        os.path.join(os.getcwd(), '.env'),  # Current dir
        os.path.join(os.path.dirname(os.getcwd()), '.env'),  # Parent dir
        os.path.join(os.path.expanduser('~'), '.env'),  # Home dir
        os.path.join(os.path.expanduser('~'), '.apirotater.env'),  # Config in home
    ]
    
    for env_path in possible_locations:
        if os.path.exists(env_path):
            print(f"APIRotater: Loading environment from {env_path}")
            load_dotenv(env_path)
            return True
            
    # No .env file found, but we'll still try to load from environment variables
    return False

# Auto-load environment on import
_load_environment()

# Create a global API key manager instance
_manager = APIKeyManager()

# Expose key manager functions at module level
add_api_key = _manager.add_api_key
add_multiple_api_keys = _manager.add_multiple_api_keys
get_api_key = _manager.get_api_key
key = lambda usage_count=1, time_window=None, max_uses=None: _manager.get_api_key(usage_count, time_window, max_uses)  # Updated key alias
hit = _manager.hit
get_usage_stats = _manager.get_usage_stats
get_available_keys = _manager.get_available_keys
reset_usage_counts = _manager.reset_usage_counts
remove_api_key = _manager.remove_api_key
set_rate_limit = _manager.set_rate_limit
limit = _manager.set_rate_limit  # Alias for set_rate_limit
get_all_keys = _manager.get_all_keys

# Export exceptions
__all__ = [
    'APIKeyManager', 'RateLimitExceeded',
    'add_api_key', 'add_multiple_api_keys', 'get_api_key', 'key', 'hit',
    'get_usage_stats', 'get_available_keys', 'reset_usage_counts',
    'remove_api_key', 'set_rate_limit', 'limit', 'get_all_keys'
]

__version__ = "0.3.0" 