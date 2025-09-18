
import unittest

def sliding_windows(xs, w):
    """Yield all contiguous windows of size w from xs."""
    if w <= 0:
        raise ValueError("Window size must be positive")
    if w > len(xs):
        return
    for i in range(len(xs) - w + 1):
        yield xs[i:i+w]

class TestSlidingWindows(unittest.TestCase):
    def test_basic(self):
        xs = [13, 14, 15, 16]
        w = 2
        result = list(sliding_windows(xs, w))
        expected = [
            [13, 14],
            [14, 15],
            [15, 16]
        ]
        self.assertEqual(result, expected)
        self.assertEqual(len(result), len(xs) - w + 1)

    def test_window_equals_length(self):
        xs = [1, 2, 3]
        w = 3
        result = list(sliding_windows(xs, w))
        self.assertEqual(result, [[1, 2, 3]])

    def test_window_larger_than_length(self):
        xs = [1, 2]
        w = 3
        result = list(sliding_windows(xs, w))
        self.assertEqual(result, [])

    def test_window_size_one(self):
        xs = [5, 6, 7]
        w = 1
        result = list(sliding_windows(xs, w))
        self.assertEqual(result, [[5], [6], [7]])

    def test_empty_list(self):
        xs = []
        w = 1
        result = list(sliding_windows(xs, w))
        self.assertEqual(result, [])

    def test_invalid_window_size(self):
        xs = [1, 2, 3]
        with self.assertRaises(ValueError):
            list(sliding_windows(xs, 0))
        with self.assertRaises(ValueError):
            list(sliding_windows(xs, -1))

if __name__ == "__main__":
    unittest.main()
