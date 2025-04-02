import time
from typing import Callable, Any, Dict


def with_api_key(manager, func: Callable, *args, usage_count: int = 1, **kwargs) -> Any:
    """
    A decorator-like function to call a function with an API key.
    
    Args:
        manager: The APIKeyManager instance
        func: The function to call
        usage_count: The number of times the API key will be used
        args: Arguments to pass to the function
        kwargs: Keyword arguments to pass to the function
        
    Returns:
        The return value of the function
    """
    api_key = manager.get_api_key(usage_count=usage_count)
    if api_key is None:
        raise ValueError("No available API key found")
    
    # Add or update the API key in kwargs
    kwargs['api_key'] = api_key
    
    try:
        result = func(*args, **kwargs)
        manager.hit(api_key)
        return result
    except Exception as e:
        manager.hit(api_key)
        raise e


class APIThrottler:
    """A class used to limit API requests."""
    
    def __init__(self, rate_limit: int, time_period: int = 60):
        """
        Args:
            rate_limit: The maximum number of requests allowed in the given time period
            time_period: The time period in seconds
        """
        self.rate_limit = rate_limit
        self.time_period = time_period
        self.requests = []
    
    def wait_if_needed(self):
        """Wait if the limit has been exceeded."""
        current_time = time.time()
        
        # Clear old requests
        self.requests = [t for t in self.requests if current_time - t < self.time_period]
        
        # Wait if the limit is reached
        if len(self.requests) >= self.rate_limit:
            sleep_time = self.time_period - (current_time - self.requests[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
            
            # Recalculate time and clear old requests
            current_time = time.time()
            self.requests = [t for t in self.requests if current_time - t < self.time_period]
        
        # Add the new request
        self.requests.append(current_time) 