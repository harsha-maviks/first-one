import unittest
from mutable_list import (
    change_item, add_item, insert_item, remove_item,
    pop_last, sort_list, reverse_list,
)


class TestMutableList(unittest.TestCase):

    def setUp(self):
        self.fruits = ["apple", "banana", "cherry"]

    def test_change_item(self):
        change_item(self.fruits, 1, "mango")
        self.assertEqual(self.fruits, ["apple", "mango", "cherry"])

    def test_add_item(self):
        add_item(self.fruits, "orange")
        self.assertEqual(self.fruits, ["apple", "banana", "cherry", "orange"])

    def test_insert_item(self):
        insert_item(self.fruits, 0, "grapes")
        self.assertEqual(self.fruits[0], "grapes")

    def test_remove_item(self):
        remove_item(self.fruits, "apple")
        self.assertNotIn("apple", self.fruits)

    def test_remove_missing_item_raises(self):
        with self.assertRaises(ValueError):
            remove_item(self.fruits, "kiwi")

    def test_pop_last(self):
        self.assertEqual(pop_last(self.fruits), "cherry")
        self.assertEqual(len(self.fruits), 2)

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            pop_last([])

    def test_sort_list(self):
        lst = [3, 1, 2]
        sort_list(lst)
        self.assertEqual(lst, [1, 2, 3])

    def test_reverse_list(self):
        reverse_list(self.fruits)
        self.assertEqual(self.fruits, ["cherry", "banana", "apple"])

    def test_function_mutates_original_object(self):
        original_id = id(self.fruits)
        result = add_item(self.fruits, "kiwi")
        self.assertIs(result, self.fruits)
        self.assertEqual(id(self.fruits), original_id)

    def test_reference_shares_changes(self):
        a = [1, 2, 3]
        b = a
        add_item(b, 4)
        self.assertEqual(a, [1, 2, 3, 4])

    def test_copy_is_independent(self):
        a = [1, 2, 3]
        c = a.copy()
        add_item(c, 5)
        self.assertEqual(a, [1, 2, 3])

    def test_tuple_is_immutable(self):
        t = (1, 2, 3)
        with self.assertRaises(TypeError):
            t[0] = 10


if __name__ == "__main__":
    unittest.main()