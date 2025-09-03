import unittest
from task_4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item_new(self):
        self.cart.add_item('apple', 1.5, 2)
        self.assertIn('apple', self.cart.items)
        self.assertEqual(self.cart.items['apple']['quantity'], 2)
        self.assertEqual(self.cart.items['apple']['price'], 1.5)

    def test_add_item_existing(self):
        self.cart.add_item('banana', 0.5, 3)
        self.cart.add_item('banana', 0.5, 2)
        self.assertEqual(self.cart.items['banana']['quantity'], 5)

    def test_remove_item_partial(self):
        self.cart.add_item('orange', 2.0, 5)
        self.cart.remove_item('orange', 2)
        self.assertEqual(self.cart.items['orange']['quantity'], 3)

    def test_remove_item_all(self):
        self.cart.add_item('pear', 1.0, 2)
        self.cart.remove_item('pear', 2)
        self.assertNotIn('pear', self.cart.items)

    def test_remove_item_not_found(self):
        # Should not raise, just print
        self.cart.remove_item('notfound', 1)
        self.assertNotIn('notfound', self.cart.items)

    def test_total_cost(self):
        self.cart.add_item('apple', 1.5, 2)
        self.cart.add_item('banana', 0.5, 4)
        self.assertAlmostEqual(self.cart.total_cost(), 1.5*2 + 0.5*4)

if __name__ == '__main__':
    unittest.main()