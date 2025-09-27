from unittest import TestCase
from main import bSearchInSortedList, maxNegativeRepr

class BinarySearchTest(TestCase):
    def setUp(self):
        self.numbers: list[int] = [1, 2, 3, 5, 5, 5, 7, 8, 9, 10]
        
    def test_found_first(self):
        self.assertEqual(bSearchInSortedList(self.numbers, 1), 0)
         
    def test_found_last(self):
        self.assertEqual(bSearchInSortedList(self.numbers, 10), 9) 
        
    def test_found_first_av(self):
        self.assertEqual(bSearchInSortedList(self.numbers, 5), 3) 
        
    def test_not_found(self):
        self.assertEqual(bSearchInSortedList(self.numbers, 4), -4)
        self.assertEqual(bSearchInSortedList(self.numbers, 11), -10)
        self.assertEqual(bSearchInSortedList(self.numbers, 0), -1)
        
class MaxNegativeTest(TestCase):
    def setUp(self):
        self.numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.nums: list[int] = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]
        
    def test_not_found(self):
        self.assertEqual(maxNegativeRepr(self.numbers), -1)
        self.assertEqual(maxNegativeRepr([]), -1)
        self.assertEqual(maxNegativeRepr(self.nums), -1)
        
    def found(self):
        self.assertEqual(maxNegativeRepr([0]), 0)
        self.assertEqual(maxNegativeRepr([100, 4, 1, -1, -4, -100]), 100)
        self.assertEqual(maxNegativeRepr([100, 4, 1, 1, 4, 100, -1]), 1)
        self.assertEqual(maxNegativeRepr([-1, -2, 0, 100, 200, 1, -5, 8, 2, -300, 3]), 2)
