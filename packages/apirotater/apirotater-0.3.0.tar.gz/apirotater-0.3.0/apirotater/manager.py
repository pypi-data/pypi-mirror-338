from typing import List, Dict, Optional, Tuple
import time
import random
import os
from dotenv import load_dotenv


class RateLimitExceeded(Exception):
    """Exception raised when all API keys have reached their rate limits."""
    pass


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
        """Load API keys from environment variables"""
        try:
            i = 1
            # First look for API_KEY_* pattern
            while True:
                env_var = f'API_KEY_{i}'
                api_key = os.getenv(env_var)
                if not api_key:
                    break
                    
                # Skip default/placeholder values
                if api_key.startswith("your_") or api_key == "your_api_key_here":
                    i += 1
                    continue
                    
                self.add_api_key(api_key)
                print(f"Loaded API key from {env_var}")
                i += 1
                
            # If no keys were found with API_KEY_* pattern, look for OPENAI_API_KEY, etc.
            if len(self.api_keys) == 0:
                common_api_keys = [
                    "OPENAI_API_KEY", 
                    "GOOGLE_API_KEY", 
                    "GEMINI_API_KEY",
                    "API_KEY"
                ]
                
                for key_name in common_api_keys:
                    api_key = os.getenv(key_name)
                    if api_key:
                        self.add_api_key(api_key)
                        print(f"Loaded API key from {key_name}")
                        
            # Log the number of keys loaded
            if len(self.api_keys) > 0:
                print(f"Successfully loaded {len(self.api_keys)} API key(s)")
            else:
                print("Warning: No API keys were loaded from environment variables")
                
        except Exception as e:
            print(f"Error loading API keys from environment: {e}")
            # Continue without failing completely

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
        current_time = time.time()
        
        for i, (tw, max_u, current_uses, window_start_time) in enumerate(self.time_limits[api_key]):
            if tw == time_window:
                # Eğer mevcut bir time window varsa ve süresi dolmamışsa, verileri koru
                # Sadece zaman penceresinin süresi dolmuşsa sıfırla
                if current_time - window_start_time > time_window:
                    # Pencere süresi dolmuş, yeni bir pencere başlat
                    self.time_limits[api_key][i] = (time_window, max_uses, 0, current_time)
                else:
                    # Pencere hala aktif, sadece max_uses güncelle, diğer değerleri koru
                    self.time_limits[api_key][i] = (time_window, max_uses, current_uses, window_start_time)
                return True
                
        # Bu time window daha önce ayarlanmamış, yeni ekle
        self.time_limits[api_key].append((time_window, max_uses, 0, current_time))
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

    def get_api_key(self, usage_count: int = 1, time_window: Optional[int] = None, max_uses: Optional[int] = None) -> Optional[str]:
        """
        Get the next API key in the rotation.
        
        Args:
            usage_count: The number of times the key will be used.
            time_window: Time window in seconds for rate limiting.
            max_uses: Maximum number of uses in the time window.
            
        Returns:
            The API key to use, or None if all keys are reserved.
            
        Raises:
            RateLimitExceeded: If all keys are rate limited.
        """
        if not self.api_keys:
            return None
            
        # If time_window and max_uses are provided, we check if any key is available
        # with these limits, and if not, raise RateLimitExceeded
        all_keys_rate_limited = True
        earliest_reset_time = float('inf')
        reset_key = None
            
        # First try: find an available key with no reservation or time limits
        start_index = self.current_index
        for _ in range(len(self.api_keys)):
            api_key = self.api_keys[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.api_keys)
            
            if api_key in self.reserved_usages:
                # If the key is reserved, skip it
                if self.reserved_usages[api_key] > 0:
                    continue
                    
                # Check rate limits
                is_limited, reset_seconds = self._get_rate_limit_status(api_key)
                if is_limited:
                    # Track the earliest reset time
                    if reset_seconds is not None and reset_seconds < earliest_reset_time:
                        earliest_reset_time = reset_seconds
                        reset_key = api_key
                    continue
                    
                # This key is available!
                all_keys_rate_limited = False
                
                # If time_window and max_uses are provided, check if we need to set a rate limit
                if time_window is not None and max_uses is not None:
                    # Kontrol et - bu anahtar için verilen time_window ile mevcut bir rate limit var mı?
                    has_matching_limit = False
                    
                    for tw, _, _, win_start_time in self.time_limits.get(api_key, []):
                        if tw == time_window:
                            # Zaten bu time_window için bir limit var, 
                            # ve set_rate_limit fonksiyonu gerekirse güncelleme yapacak
                            has_matching_limit = True
                            break
                    
                    # Eğer bu time_window için bir limit yoksa veya hiç limit yoksa, yeni bir tane ekle
                    if not has_matching_limit:
                        self.set_rate_limit(api_key, time_window, max_uses)
                
                # Reserve the key for usage
                self.reserved_usages[api_key] = usage_count
                return api_key
        
        # If we get here, all keys are either reserved or rate limited
        if all_keys_rate_limited and earliest_reset_time < float('inf'):
            # All keys are rate limited, raise an exception
            reset_msg = f"Next key will be available in {earliest_reset_time:.1f} seconds"
            raise RateLimitExceeded(f"All API keys have reached their rate limits. {reset_msg}")
        
        # Second try: if all keys are reserved or limited, use the least used key
        # that isn't rate limited
        least_used_key = None
        least_usage = float('inf')
        
        for key in self.api_keys:
            is_limited, _ = self._get_rate_limit_status(key)
            if not is_limited and self.usage_counts[key] < least_usage:
                least_usage = self.usage_counts[key]
                least_used_key = key
                
        if least_used_key:
            # If time_window and max_uses are provided, check if we need to set a rate limit
            if time_window is not None and max_uses is not None:
                # Kontrol et - bu anahtar için verilen time_window ile mevcut bir rate limit var mı?
                has_matching_limit = False
                
                for tw, _, _, win_start_time in self.time_limits.get(least_used_key, []):
                    if tw == time_window:
                        # Zaten bu time_window için bir limit var, 
                        # ve set_rate_limit fonksiyonu gerekirse güncelleme yapacak
                        has_matching_limit = True
                        break
                
                # Eğer bu time_window için bir limit yoksa veya hiç limit yoksa, yeni bir tane ekle
                if not has_matching_limit:
                    self.set_rate_limit(least_used_key, time_window, max_uses)
                
            # Reset the reservation for this key
            self.reserved_usages[least_used_key] = usage_count
            return least_used_key
        
        # All keys are rate limited
        if earliest_reset_time < float('inf'):
            reset_msg = f"Next key will be available in {earliest_reset_time:.1f} seconds"
            raise RateLimitExceeded(f"All API keys have reached their rate limits. {reset_msg}")
            
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
            
        # Increment the global usage counter
        self.usage_counts[api_key] += 1
        
        # Decrement the reservation counter if it's > 0
        if api_key in self.reserved_usages and self.reserved_usages[api_key] > 0:
            self.reserved_usages[api_key] -= 1
            
        # Update time limits
        current_time = time.time()
        
        # Store updated limits here
        updated_limits = []
        
        for time_window, max_uses, current_uses, window_start_time in self.time_limits.get(api_key, []):
            # If the window has expired, reset it
            if current_time - window_start_time > time_window:
                # Reset the window with 1 use
                updated_limits.append((time_window, max_uses, 1, current_time))
            else:
                # Increment the current uses in this window
                updated_limits.append((time_window, max_uses, current_uses + 1, window_start_time))
        
        # Update the time limits
        if api_key in self.time_limits:
            self.time_limits[api_key] = updated_limits

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