import unittest
from quicksort import quicksort

# tests for the quick sort implementation
class TestQuickSort(unittest.TestCase):
    
    def test_empty_list(self):
        empty_case = []
        quicksort(empty_case, 0, 0)
        self.assertEqual(empty_case, [])

    def test_one_element(self):
        one_element = [2]
        quicksort(one_element, 0, 1)
        self.assertEqual(one_element, [2])

    def test_two_element_unsorted(self):
        two_element = [32, 5]
        quicksort(two_element, 0, 2)
        self.assertEqual(two_element, [5, 32])

    def test_two_element_sorted(self):
        two_element_sorted = [16, 236]
        quicksort(two_element_sorted, 0, 2)
        self.assertEqual(two_element_sorted, [16, 236])

    def test_seven_element(self):
        seven_element = [3, 626, 55, 72, 14, 0, -23]
        quicksort(seven_element, 0, 7)
        self.assertEqual(seven_element, [-23, 0, 3, 14, 55, 72, 626])

    def test_twelve_element(self):
        twelve_element = [-325, 235, 4, 13, -36, 457, -2, 10, 6, 1, 4, 62]
        quicksort(twelve_element, 0, 12)
        self.assertEqual(
            twelve_element, [-325, -36, -2, 1, 4, 4, 6, 10, 13, 62, 235, 457])

















if __name__ == '__main__':
    unittest.main()
