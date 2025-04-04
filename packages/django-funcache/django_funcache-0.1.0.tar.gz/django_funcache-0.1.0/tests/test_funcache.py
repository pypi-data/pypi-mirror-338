"""Tests for the funcache package."""
from django.test import TestCase
from funcache.utils import func_cache


class FuncCacheTestCase(TestCase):
    def test_func_cache_decorator(self):
        """Test that func_cache correctly caches function results."""
        call_count = [0]  # Use a list to allow modification in the inner function
        
        @func_cache(key_prefix="test")
        def test_func(value):
            call_count[0] += 1
            return value * 2
        
        # First call should execute the function
        result1 = test_func(5)
        self.assertEqual(result1, 10)
        self.assertEqual(call_count[0], 1)
        
        # Second call with same args should return cached result
        result2 = test_func(5)
        self.assertEqual(result2, 10)
        self.assertEqual(call_count[0], 1)  # Should still be 1
        
        # Call with different args should execute the function
        result3 = test_func(10)
        self.assertEqual(result3, 20)
        self.assertEqual(call_count[0], 2)
