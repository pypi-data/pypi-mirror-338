import unittest
from apirotater import APIKeyManager


class TestAPIKeyManager(unittest.TestCase):
    def setUp(self):
        self.manager = APIKeyManager()
        self.test_keys = ["key1", "key2", "key3"]
        
    def test_add_api_key(self):
        self.manager.add_api_key("test_key")
        self.assertIn("test_key", self.manager.api_keys)
        self.assertEqual(self.manager.usage_counts["test_key"], 0)
        
    def test_add_multiple_api_keys(self):
        self.manager.add_multiple_api_keys(self.test_keys)
        for key in self.test_keys:
            self.assertIn(key, self.manager.api_keys)
            
    def test_get_api_key(self):
        self.manager.add_multiple_api_keys(self.test_keys)
        
        # Get the first key
        key1 = self.manager.get_api_key()
        self.assertEqual(key1, "key1")
        
        # Get the second key
        key2 = self.manager.get_api_key()
        self.assertEqual(key2, "key2")
        
        # Get the third key
        key3 = self.manager.get_api_key()
        self.assertEqual(key3, "key3")
        
        # Should loop back to the first key
        key4 = self.manager.get_api_key()
        self.assertEqual(key4, "key1")
        
    def test_hit(self):
        self.manager.add_api_key("test_key")
        
        # Report usage
        self.manager.hit("test_key")
        self.assertEqual(self.manager.usage_counts["test_key"], 1)
        
        # Report usage again
        self.manager.hit("test_key")
        self.assertEqual(self.manager.usage_counts["test_key"], 2)
        
    def test_get_usage_stats(self):
        self.manager.add_multiple_api_keys(self.test_keys)
        
        # Report some usages
        self.manager.hit("key1")
        self.manager.hit("key1")
        self.manager.hit("key2")
        
        stats = self.manager.get_usage_stats()
        self.assertEqual(stats["key1"], 2)
        self.assertEqual(stats["key2"], 1)
        self.assertEqual(stats["key3"], 0)
        
    def test_reset_usage_counts(self):
        self.manager.add_multiple_api_keys(self.test_keys)
        
        # Report some usages
        self.manager.hit("key1")
        self.manager.hit("key2")
        
        # Reset the counters
        self.manager.reset_usage_counts()
        
        for key in self.test_keys:
            self.assertEqual(self.manager.usage_counts[key], 0)
            
    def test_remove_api_key(self):
        self.manager.add_multiple_api_keys(self.test_keys)
        
        # Remove a key
        self.assertTrue(self.manager.remove_api_key("key2"))
        self.assertNotIn("key2", self.manager.api_keys)
        self.assertNotIn("key2", self.manager.usage_counts)
        
        # Try to remove a non-existent key
        self.assertFalse(self.manager.remove_api_key("nonexistent_key"))
        
    def test_usage_reservation(self):
        self.manager.add_multiple_api_keys(self.test_keys)
        
        # Reserve the first key for 2 usages
        key = self.manager.get_api_key(usage_count=2)
        self.assertEqual(key, "key1")
        self.assertEqual(self.manager.reserved_usages[key], 2)
        
        # Report one usage
        self.manager.hit(key)
        self.assertEqual(self.manager.reserved_usages[key], 1)
        
        # Report another usage
        self.manager.hit(key)
        self.assertEqual(self.manager.reserved_usages[key], 0)
        
        # The key should now be available again
        available_keys = self.manager.get_available_keys()
        self.assertIn(key, available_keys)


if __name__ == "__main__":
    unittest.main() 