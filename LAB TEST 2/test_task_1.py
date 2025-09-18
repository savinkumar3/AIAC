import unittest
from task_1 import fare


class TestFareFunction(unittest.TestCase):
    """Comprehensive test cases for the fare calculation function."""
    
    def test_basic_fare_calculations(self):
        """Test normal fares before and after surge time."""
        # Normal fares before 18:00
        self.assertEqual(fare([{'time': '08:00', 'km': 3.0}]), [66.0])
        self.assertEqual(fare([{'time': '12:30', 'km': 5.5}]), [121.0])
        self.assertEqual(fare([{'time': '17:59', 'km': 2.0}]), [44.0])
        
        # Surge pricing after 18:00
        self.assertEqual(fare([{'time': '18:01', 'km': 3.0}]), [132.0])
        self.assertEqual(fare([{'time': '20:30', 'km': 5.0}]), [220.0])
        self.assertEqual(fare([{'time': '23:45', 'km': 2.5}]), [110.0])
        
        # Exact 18:00 (no surge)
        self.assertEqual(fare([{'time': '18:00', 'km': 3.0}]), [66.0])
    
    def test_mixed_times(self):
        """Test mixed times with and without surge pricing."""
        rides = [
            {'time': '17:30', 'km': 2.0},  # No surge
            {'time': '18:00', 'km': 3.0},  # No surge
            {'time': '18:01', 'km': 4.0},  # Surge
            {'time': '19:00', 'km': 1.5}   # Surge
        ]
        expected = [44.0, 66.0, 176.0, 66.0]
        self.assertEqual(fare(rides), expected)
    
    def test_edge_cases(self):
        """Test edge cases and special values."""
        # Empty list
        self.assertEqual(fare([]), [])
        
        # Zero distance
        self.assertEqual(fare([{'time': '10:00', 'km': 0.0}]), [0.0])
        self.assertEqual(fare([{'time': '19:00', 'km': 0.0}]), [0.0])
        
        # Single ride
        self.assertEqual(fare([{'time': '15:30', 'km': 4.5}]), [99.0])
        
        # Decimal distances
        rides = [{'time': '14:30', 'km': 2.5}, {'time': '18:30', 'km': 3.7}]
        self.assertEqual(fare(rides), [55.0, 162.8])
        
        # Large distance
        self.assertEqual(fare([{'time': '20:00', 'km': 1000.0}]), [44000.0])
        
        # Negative distance
        self.assertEqual(fare([{'time': '15:00', 'km': -2.0}]), [-44.0])
    
    def test_rounding_precision(self):
        """Test proper rounding to 2 decimal places."""
        # Test rounding edge cases
        rides = [
            {'time': '15:00', 'km': 1.0/3},  # 7.333... -> 7.33
            {'time': '20:00', 'km': 1.0/3}   # 14.666... -> 14.67
        ]
        self.assertEqual(fare(rides), [7.33, 14.67])
        
        # Test floating point precision
        rides = [{'time': '10:00', 'km': 0.1}]
        self.assertEqual(fare(rides), [2.2])
    
    def test_custom_parameters(self):
        """Test with custom base_per_km and surgeMultiplier."""
        rides = [{'time': '10:00', 'km': 2.0}, {'time': '19:00', 'km': 2.0}]
        expected = [60.0, 180.0]  # 2*30, 2*30*3
        result = fare(rides, base_per_km=30.0, surgeMultiplier=3.0)
        self.assertEqual(result, expected)
        
        # Test with different parameters
        rides = [{'time': '15:00', 'km': 5.0}, {'time': '20:00', 'km': 5.0}]
        expected = [100.0, 500.0]  # 5*20, 5*20*5
        result = fare(rides, base_per_km=20.0, surgeMultiplier=5.0)
        self.assertEqual(result, expected)
    
    def test_midnight_cases(self):
        """Test cases around midnight."""
        rides = [
            {'time': '23:59', 'km': 2.0},  # Surge
            {'time': '00:00', 'km': 2.0},  # No surge
            {'time': '00:01', 'km': 2.0}   # No surge
        ]
        expected = [88.0, 44.0, 44.0]
        self.assertEqual(fare(rides), expected)
    
    def test_multiple_rides_same_time(self):
        """Test multiple rides at the same time."""
        rides = [
            {'time': '18:30', 'km': 1.0},
            {'time': '18:30', 'km': 2.0},
            {'time': '18:30', 'km': 3.0}
        ]
        expected = [44.0, 88.0, 132.0]  # All with surge
        self.assertEqual(fare(rides), expected)
    
    def test_invalid_time_formats(self):
        """Test error handling for invalid time formats."""
        # Invalid hour values
        with self.assertRaises(ValueError) as context:
            fare([{'time': '25:00', 'km': 2.0}])
        self.assertIn("Invalid time value", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            fare([{'time': '-1:00', 'km': 2.0}])
        self.assertIn("Invalid time value", str(context.exception))
        
        # Invalid minute values
        with self.assertRaises(ValueError) as context:
            fare([{'time': '12:60', 'km': 2.0}])
        self.assertIn("Invalid time value", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            fare([{'time': '12:-1', 'km': 2.0}])
        self.assertIn("Invalid time value", str(context.exception))
        
        # Non-numeric time format
        with self.assertRaises(ValueError) as context:
            fare([{'time': 'abc:def', 'km': 2.0}])
        self.assertIn("Invalid time format", str(context.exception))
        
        # Missing colon
        with self.assertRaises(ValueError) as context:
            fare([{'time': '1200', 'km': 2.0}])
        self.assertIn("Invalid time format", str(context.exception))
        
        # Extra colons
        with self.assertRaises(ValueError) as context:
            fare([{'time': '12:00:00', 'km': 2.0}])
        self.assertIn("Invalid time format", str(context.exception))
    
    def test_missing_keys(self):
        """Test error handling for missing dictionary keys."""
        # Missing 'time' key
        with self.assertRaises(KeyError) as context:
            fare([{'km': 2.0}])
        self.assertIn("Each ride must have 'time' and 'km' keys", str(context.exception))
        
        # Missing 'km' key
        with self.assertRaises(KeyError) as context:
            fare([{'time': '15:00'}])
        self.assertIn("Each ride must have 'time' and 'km' keys", str(context.exception))
        
        # Missing both keys
        with self.assertRaises(KeyError) as context:
            fare([{}])
        self.assertIn("Each ride must have 'time' and 'km' keys", str(context.exception))
    
    def test_boundary_times(self):
        """Test boundary conditions around surge time."""
        # Just before surge (17:59)
        self.assertEqual(fare([{'time': '17:59', 'km': 1.0}]), [22.0])
        
        # Exactly at surge boundary (18:00)
        self.assertEqual(fare([{'time': '18:00', 'km': 1.0}]), [22.0])
        
        # Just after surge starts (18:01)
        self.assertEqual(fare([{'time': '18:01', 'km': 1.0}]), [44.0])
        
        # End of day
        self.assertEqual(fare([{'time': '23:59', 'km': 1.0}]), [44.0])
    
    def test_original_example(self):
        """Test the original example from the code."""
        rides = [
            {'time': '08:00', 'km': 3.0},
            {'time': '18:01', 'km': 3.0},
            {'time': '18:00', 'km': 3.0},
            {'time': '20:30', 'km': 5.0}
        ]
        expected = [66.0, 132.0, 66.0, 220.0]
        self.assertEqual(fare(rides), expected)
    
    def test_very_small_values(self):
        """Test with very small distance values."""
        rides = [{'time': '15:00', 'km': 0.001}]
        result = fare(rides)
        self.assertEqual(result, [0.02])  # 0.001 * 22 = 0.022 -> 0.02
    
    def test_very_large_values(self):
        """Test with very large distance values."""
        rides = [{'time': '20:00', 'km': 999999.99}]
        result = fare(rides)
        expected = [43999999.56]  # 999999.99 * 22 * 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
