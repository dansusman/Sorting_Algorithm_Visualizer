import unittest
from mergesort import mergesort

# tests for the merge sort implementation
class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        empty_case = []
        mergesort(empty_case)
        self.assertEqual(empty_case, [])

    def test_one_element(self):
        one_element = [2]
        mergesort(one_element)
        self.assertEqual(one_element, [2])
    
    def test_two_element_unsorted(self):
        two_element = [32, 5]
        mergesort(two_element)
        self.assertEqual(two_element, [5, 32])

    def test_two_element_sorted(self):
        two_element_sorted = [16, 236]
        mergesort(two_element_sorted)
        self.assertEqual(two_element_sorted, [16, 236])
    
    def test_seven_element(self):
        seven_element = [3, 626, 55, 72, 14, 0, -23]
        mergesort(seven_element)
        self.assertEqual(seven_element, [-23, 0, 3, 14, 55, 72, 626])

    def test_twelve_element(self):
        twelve_element = [-325, 235, 4, 13, -36, 457, -2, 10, 6, 1, 4, 62]
        mergesort(twelve_element)
        self.assertEqual(twelve_element, [-325, -36, -2, 1, 4, 4, 6, 10, 13, 62, 235, 457])


if __name__ == '__main__':
    unittest.main()
