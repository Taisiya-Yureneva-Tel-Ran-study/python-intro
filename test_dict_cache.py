from unittest import TestCase, main
from main import DictCache
class TestDictCache(TestCase):
    def setUp(self):
        self.dictCache: DictCache[str, int] = DictCache(2)
        self.dictCache['a'] = 1
        self.dictCache['b'] = 2
    def test_inserting_removes_eldest(self):
        self.dictCache['c'] = 30 #insert 'c':30 exceeds maximal size and eldest 'a':1 should be removed 
        with self.assertRaises(KeyError):
            self.dictCache['a'] 
        self.assertEqual(2, self.dictCache['b'])
        self.assertEqual(30, self.dictCache['c']) 
    def test_access_order(self) :
        self.assertEqual(1, self.dictCache['a'])   # access 'a':1 makes the item as most recent 
        self.dictCache['c'] = 30 #insert 'c':30 exceeds maximal size and eldest 'b':2 should be removed 
        with self.assertRaises(KeyError):
            self.dictCache['b'] 
        self.assertEqual(1, self.dictCache['a'])
        self.assertEqual(30, self.dictCache['c'])   
    def test_update_order(self) :
        self.dictCache['a'] = 10  # update 'a':1 to 'a':10 makes the item as most recent 
        self.dictCache['c'] = 30 #insert 'c':30 exceeds maximal size and eldest 'b':2 should be removed 
        with self.assertRaises(KeyError):
            self.dictCache['b'] 
        self.assertEqual(10, self.dictCache['a'])
        self.assertEqual(30, self.dictCache['c'])      
        