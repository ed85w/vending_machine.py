import unittest
from vending_machine import give_change
from vending_machine import give_item_and_change

class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.1, .05, .02],)
        self.assertEqual(give_change(.18), [.1, .05, .02, .01],)
        self.assertEqual(give_change(.04), [.02, .02])

    def test_give_item_and_change(self):
        """normal test"""
        item, change, _ = give_item_and_change('coke', 1)
        self.assertEqual(change,[.2, .05, .02])

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable, they should not be given the item, and their money should be returned"""
        item, change, _ = give_item_and_change('crisps', .50)
        self.assertIsNone(item)
        self.assertEqual(change, 0.5)

    def test_not_enough_money(self):
        """if user does not have enough money for item, they should be told so"""
        item, change, _ = give_item_and_change('coke', 0.2)
        self.assertEqual(change, 0.2,'not enough money')

    def test_lots_of_coins(self):
        """enter multiple coins"""
        item, change, _ = give_item_and_change('coke', [0.5, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1])
        self.assertEqual(change, [.2, .05, .02])