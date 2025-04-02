from typing import List, Dict, Optional, Tuple
import time
import random
import os
from dotenv import load_dotenv


class APIKeyManager:
    def __init__(self):
        """Initialize the API key manager."""
        load_dotenv()
        self.api_keys = []
        self.usage_counts = {}
        self.reserved_usages = {}
        self.time_limits = {}  # Stores {api_key: [(time_window, max_uses, current_uses_in_window, window_start_time), ...]}
        self.current_index = 0
        self._load_api_keys()

    def _load_api_keys(self):
        i = 1
        while True:
            api_key = os.getenv(f'API_KEY_{i}')
            if not api_key:
                break
                
            # Skip default/placeholder values
            if api_key.startswith("your_") or api_key == "your_api_key_here":
                i += 1
                continue
                
            self.add_api_key(api_key)
            i += 1

    def add_api_key(self, api_key: str) -> None:
        """
        Add a new API key.
        
        Args:
            api_key: The API key to add.
        """
        if api_key not in self.api_keys:
            self.api_keys.append(api_key)
            self.usage_counts[api_key] = 0
            self.reserved_usages[api_key] = 0
            self.time_limits[api_key] = []

    def add_multiple_api_keys(self, api_keys: List[str]) -> None:
        """
        Add multiple API keys.
        
        Args:
            api_keys: The list of API keys to add.
        """
        for key in api_keys:
            self.add_api_key(key)

    def set_rate_limit(self, api_key: str, time_window: int, max_uses: int) -> bool:
        """
        Set rate limits for an API key.
        
        Args:
            api_key: The API key to limit.
            time_window: Time window in seconds.
            max_uses: Maximum number of uses allowed in the time window.
            
        Returns:
            True if successful, False if the API key doesn't exist.
        """
        if api_key not in self.api_keys:
            return False
            
        # Check if this time window already exists
        for i, (tw, _, _, _) in enumerate(self.time_limits[api_key]):
            if tw == time_window:
                # Update existing time window
                self.time_limits[api_key][i] = (time_window, max_uses, 0, time.time())
                return True
                
        # Add new time window
        self.time_limits[api_key].append((time_window, max_uses, 0, time.time()))
        return True
        
    def _check_time_limits(self, api_key: str) -> bool:
        """
        Check if an API key has exceeded any of its time limits.
        
        Args:
            api_key: The API key to check.
            
        Returns:
            True if the key is available, False if it has exceeded any limits.
        """
        if not self.time_limits.get(api_key, []):
            return True
            
        current_time = time.time()
        
        for i, (time_window, max_uses, current_uses, window_start_time) in enumerate(self.time_limits[api_key]):
            # Check if the time window has expired
            if current_time - window_start_time > time_window:
                # Reset the window
                self.time_limits[api_key][i] = (time_window, max_uses, 0, current_time)
            elif current_uses >= max_uses:
                # The key has reached its limit for this time window
                return False
                
        return True

    def _get_rate_limit_status(self, api_key: str) -> Tuple[bool, Optional[float]]:
        """
        Get rate limit status and time until reset.
        
        Args:
            api_key: The API key to check.
            
        Returns:
            A tuple of (is_rate_limited, seconds_until_reset)
            - is_rate_limited: True if rate limited, False otherwise
            - seconds_until_reset: Seconds until the rate limit resets, or None if not limited
        """
        if not self.time_limits.get(api_key, []):
            return False, None
            
        current_time = time.time()
        is_limited = False
        earliest_reset = float('inf')
        
        for time_window, max_uses, current_uses, window_start_time in self.time_limits[api_key]:
            # Skip if window has expired
            if current_time - window_start_time > time_window:
                continue
                
            # Check if rate limited
            if current_uses >= max_uses:
                is_limited = True
                time_until_reset = window_start_time + time_window - current_time
                earliest_reset = min(earliest_reset, time_until_reset)
                
        if is_limited and earliest_reset != float('inf'):
            return True, earliest_reset
            
        return False, None

    def get_api_key(self, usage_count: int = 1) -> Optional[str]:
        """
        Get the next API key in the rotation.
        
        Args:
            usage_count: The number of times the key will be used.
            
        Returns:
            The API key to use, or None if all keys are reserved.
        """
        if not self.api_keys:
            return None
            
        # First try: find an available key with no reservation or time limits
        start_index = self.current_index
        for _ in range(len(self.api_keys)):
            api_key = self.api_keys[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.api_keys)
            
            if api_key in self.reserved_usages:
                # If the key is not reserved and not rate limited
                is_limited, _ = self._get_rate_limit_status(api_key)
                if self.reserved_usages[api_key] == 0 and not is_limited:
                    self.reserved_usages[api_key] = usage_count
                    return api_key
        
        # Second try: find the least used key, ignoring reservations and rate limits
        least_used_key = None
        least_usage = float('inf')
        
        # First try keys that aren't rate limited
        for key in self.api_keys:
            is_limited, _ = self._get_rate_limit_status(key)
            if not is_limited and self.usage_counts[key] < least_usage:
                least_usage = self.usage_counts[key]
                least_used_key = key
                
        if least_used_key:
            # Reset the reservation for this key
            self.reserved_usages[least_used_key] = usage_count
            return least_used_key
            
        # If all keys are rate limited, use the absolute least used key
        least_used_key = None
        least_usage = float('inf')
        for key in self.api_keys:
            if self.usage_counts[key] < least_usage:
                least_usage = self.usage_counts[key]
                least_used_key = key
                
        if least_used_key:
            # Reset the reservation for the least used key
            self.reserved_usages[least_used_key] = usage_count
            return least_used_key
        
        # This should not happen unless there are no keys at all
        return None

    def get_all_keys(self) -> List[str]:
        """
        Get all API keys that have been loaded.
        
        Returns:
            A list of all API keys.
        """
        return self.api_keys.copy()

    def hit(self, api_key: str) -> None:
        """
        Report usage of an API key.
        
        Args:
            api_key: The API key that was used.
        """
        if api_key not in self.api_keys:
            return
            
        self.usage_counts[api_key] += 1
        
        if api_key in self.reserved_usages and self.reserved_usages[api_key] > 0:
            self.reserved_usages[api_key] -= 1
            
        # Update time limits
        for i, (time_window, max_uses, current_uses, window_start_time) in enumerate(self.time_limits.get(api_key, [])):
            current_time = time.time()
            
            # If the window has expired, reset it
            if current_time - window_start_time > time_window:
                self.time_limits[api_key][i] = (time_window, max_uses, 1, current_time)
            else:
                # Increment the current uses in this window
                self.time_limits[api_key][i] = (time_window, max_uses, current_uses + 1, window_start_time)

    def get_usage_stats(self) -> Dict[str, int]:
        """
        Get usage statistics for all API keys.
        
        Returns:
            A dictionary mapping API keys to their usage counts.
        """
        return self.usage_counts

    def get_available_keys(self) -> List[str]:
        """
        Get a list of available (non-reserved) API keys.
        
        Returns:
            A list of available API keys.
        """
        return [key for key in self.api_keys if self.reserved_usages.get(key, 0) == 0]

    def reset_usage_counts(self) -> None:
        """Reset the usage counters for all API keys."""
        for key in self.usage_counts:
            self.usage_counts[key] = 0

    def remove_api_key(self, api_key: str) -> bool:
        """
        Remove an API key.
        
        Args:
            api_key: The API key to remove.
            
        Returns:
            True if the operation was successful, False otherwise.
        """
        if api_key in self.api_keys:
            self.api_keys.remove(api_key)
            del self.usage_counts[api_key]
            del self.reserved_usages[api_key]
            
            # Adjust the current index
            if self.current_index >= len(self.api_keys) and len(self.api_keys) > 0:
                self.current_index = 0
                
            return True
        return False 