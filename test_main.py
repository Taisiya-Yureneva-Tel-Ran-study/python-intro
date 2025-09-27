from unittest import TestCase
from main import bSearchInSortedList, maxNegativeRepr

class BinarySearchTest(TestCase):
    def setUp(self):
        self.numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
    def test_found_first(self):
        self.assertEqual(bSearchInSortedList(self.numbers, 1), 0) 
        
class MaxNegativeTest(TestCase):
    def setUp(self):
        self.numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.numsWithNegatives: list[int] = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]
        
    def test_not_found(self):
        self.assertEqual(maxNegativeRepr(self.numbers), -1)
        self.assertEqual(maxNegativeRepr([]), -1)
        self.assertEqual(maxNegativeRepr(self.numsWithNegatives), -1)
        
    def found(self):
        self.assertEqual(maxNegativeRepr([0]), 0)
        self.assertEqual(maxNegativeRepr([1, 0, -1]), 1)
        self.assertEqual(maxNegativeRepr([-1, -2, 0, 100, 200, 1, -5, 8, 2, -300, 3]), 2)
