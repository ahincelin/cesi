import unittest
import random
import sortlib

class TestSortLib(unittest.TestCase):

    def test_BubbleSort(self):
        data = [3, 9, 1, 79, 3, 65, 7, 42]
        data = sortlib.BubbleSort(data)
        print('[BubbleSort] Sorted Array in Ascending Order:')
        print(data)
        self.assertEqual(data, [1, 3, 3, 7, 9, 42, 65, 79])

    def test_QuickSort(self):
        data = [3, 9, 1, 79, 3, 65, 7, 42]
        data = sortlib.QuickSort(data)
        print('[QickSort] Sorted Array in Ascending Order:')
        print(data)
        self.assertEqual(data, [1, 3, 3, 7, 9, 42, 65, 79])

            
if __name__ == '__main__':
    unittest.main()

