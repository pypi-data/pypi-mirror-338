import unittest
from lortools.search.binary_search import BinarySearch as bs
from lortools.sort.sort_tools import SortTools


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        a = [1, 3, 4, 6, 7, 8, 9]
        self.assertEqual(-1, bs.find(a, -5))
        self.assertEqual(-1, bs.find(a, 0))
        self.assertEqual(-2, bs.find(a, 2))
        self.assertEqual(-4, bs.find(a, 5))
        self.assertEqual(-8, bs.find(a, 10))
        self.assertEqual(-1, bs.find(a, 10, b_return_pos=False))
        self.assertEqual(2, bs.find(a, 4))

    def test_binary_search_array(self):
        a = b'123654789'
        end_pos = [3, 6, 9]
        # Using end positions
        self.assertEqual(0, bs.find_in_array(a, b'123', end_pos))
        self.assertEqual(1, bs.find_in_array(a, b'654', end_pos))
        self.assertEqual(2, bs.find_in_array(a, b'789', end_pos))
        self.assertEqual(-1, bs.find_in_array(a, b'ha', end_pos, b_return_pos=False))
        self.assertEqual(-4, bs.find_in_array(a, b'ha', end_pos, b_return_pos=True))

        # Using fixed size; mess up end_pos to make sure it is being ignored
        end_pos = [-1, 'haha', 2876, 37]
        self.assertEqual(0, bs.find_in_array(a, b'123', end_pos, fixed_size=3))
        self.assertEqual(1, bs.find_in_array(a, b'654', end_pos, fixed_size=3))
        self.assertEqual(2, bs.find_in_array(a, b'789', end_pos, fixed_size=3))
        self.assertEqual(-1, bs.find_in_array(a, b'ha', end_pos, fixed_size=3, b_return_pos=False))
        self.assertEqual(-4, bs.find_in_array(a, b'ha', end_pos, fixed_size=3, b_return_pos=True))

        # Automatic assumption of fixed size = 1
        self.assertEqual(1, bs.find_in_array(a, b'2'))
        self.assertEqual(6, bs.find_in_array(a, b'7'))
        self.assertEqual(-1, bs.find_in_array(a, b'0'))
        self.assertEqual(-10, bs.find_in_array(a, b'a'))



class TestSortTogether(unittest.TestCase):
    def test_sort_together(self):
        a = [5, 4, 3, 3, 2, 1]
        b = [3, 2, 4, 6, 1, 5]
        c, d = SortTools.sort_together(a, b)
        self.assertListEqual(c, [1, 2, 3, 3, 4, 5])
        self.assertListEqual(d, [5, 1, 4, 6, 2, 3])
