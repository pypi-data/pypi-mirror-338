from .manager import APIKeyManager

# Create a global API key manager instance
_manager = APIKeyManager()

# Expose key manager functions at module level
add_api_key = _manager.add_api_key
add_multiple_api_keys = _manager.add_multiple_api_keys
get_api_key = _manager.get_api_key
key = _manager.get_api_key  # Alias for get_api_key
hit = _manager.hit
get_usage_stats = _manager.get_usage_stats
get_available_keys = _manager.get_available_keys
reset_usage_counts = _manager.reset_usage_counts
remove_api_key = _manager.remove_api_key
set_rate_limit = _manager.set_rate_limit
limit = _manager.set_rate_limit  # Alias for set_rate_limit
get_all_keys = _manager.get_all_keys

__version__ = "0.2.0" 