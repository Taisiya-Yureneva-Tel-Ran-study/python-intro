from unittest import TestCase
from main import MyDictionary, MySortedDict

class MyDictionaryTest(TestCase):
    def setUp(self):
        self.dict: MyDictionary = MyDictionary()
        
    def test_add_values(self):
        self.dict["q"] = 1
        self.assertEqual(self.dict["q"], 1)
        # test __set_item__ updates existing key
        self.dict["q"] = 2
        self.assertEqual(self.dict["q"], 2)
        
    def test_len(self):
        self.assertEqual(len(self.dict), 0)
        self.dict["q"] = 1
        self.dict["w"] = 2
        self.assertEqual(len(self.dict), 2)
        
    def test_setdefault(self):
        self.dict["a"] = 1
        self.dict["c"] = 3
        self.assertEqual(self.dict.setdefault("b", 2), 2) # b is missing, so insert and return default
        self.assertEqual(self.dict.setdefault("a", 10), 1) # a exists, so return existing value
        
    def test_keys(self):
        self.assertEqual(self.dict.keys(), [])
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 4
        self.assertCountEqual(self.dict.keys(), ['a', 'd', 'm', 'k'])

    def test_items(self):
        self.assertEqual(self.dict.items(), [])
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 4
        self.assertCountEqual(self.dict.items(), [('a', 1), ('d', 4), ('m', 13), ('k', 11)])

    def test_values(self):
        self.assertEqual(self.dict.values(), [])
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 4
        self.assertCountEqual(self.dict.values(), [1, 4, 13, 11])
        rList = self.dict.values()
        rList.sort()
        self.assertListEqual(rList, [1, 4, 11, 13])
                
    def test_update(self):
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict.update('a', 10) # update existing key
        self.assertEqual(self.dict['a'], 10)
        self.dict.update('m', 100)
        self.assertEqual(self.dict['m'], 100)
        self.assertEqual(len(self.dict), 3)
        
    def test_pop(self):
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 4
        self.assertEqual(self.dict.pop('k'), 11) # remove existing key
        self.assertEqual(len(self.dict), 3)
        self.assertEqual(self.dict.pop('m', None), 13) # remove existing key with None as a default value
        self.assertEqual(len(self.dict), 2)
        with self.assertRaises(KeyError):
            self.dict.pop('b')
        self.assertEqual(self.dict.pop('b', None), None)
        self.assertEqual(self.dict.pop('b', 100500), 100500)
        self.assertEqual(len(self.dict), 2)

class MySortedDictTest(TestCase):
    def setUp(self):
        self.dict: MySortedDict = MySortedDict()
        
    def test_add_and_get_values(self):
        self.dict["a"] = 1
        self.dict["q"] = 10
        self.dict["b"] = 2
        self.dict["m"] = 13
        self.assertEqual(self.dict["q"], 10)
        print(self.dict)
        # test __set_item__ updates existing key
        self.dict["q"] = 2
        self.assertEqual(self.dict["q"], 2)
        with self.assertRaises(KeyError):
            self.dict["z"]
            
    def test_setdefault(self):
        self.dict["a"] = 1
        self.dict["c"] = 3
        self.assertEqual(self.dict.setdefault("b", 2), 2) # b is missing, so insert and return default
        self.assertEqual(self.dict.setdefault("a", 10), 1) # a exists, so return existing value
        
    def test_get(self):
        self.dict["a"] = 1
        self.dict["c"] = 3
        self.assertEqual(self.dict.get("b"), None) # b is missing, so return default None
        self.assertEqual(self.dict.get("b", 2), 2) # b is missing, so return default 2
        self.assertEqual(self.dict.get("a", 10), 1) # a exists, so return existing value
        
    def test_keys_and_values(self):
        self.assertEqual(self.dict.keys(), [])
        self.assertEqual(self.dict.values(), [])
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 32
        self.assertListEqual(self.dict.keys(), ['a', 'd', 'k', 'm'])
        self.assertListEqual(self.dict.values(), [1, 32, 11, 13])
        
    def test_update(self):
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict.update('a', 10) # update existing key
        self.assertEqual(self.dict['a'], 10)
        self.dict.update('m', 100)
        self.assertEqual(self.dict['m'], 100)
        self.assertEqual(len(self.dict), 3)
        
    def test_pop(self):
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 4
        self.assertEqual(self.dict.pop('k'), 11) # remove existing key
        self.assertEqual(len(self.dict), 3)
        self.assertEqual(self.dict.pop('m', None), 13) # remove existing key with None as a default value
        self.assertEqual(len(self.dict), 2)
        with self.assertRaises(KeyError):
            self.dict.pop('b')
        self.assertEqual(self.dict.pop('b', None), None)
        self.assertEqual(self.dict.pop('b', 100500), 100500)
        self.assertEqual(len(self.dict), 2)
        
    def test_bisect_left(self):
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 4
        self.assertEqual(self.dict.bisect_left('a'), 0)
        self.assertEqual(self.dict.bisect_left('A'), 0)
        self.assertEqual(self.dict.bisect_left('b'), 1)
        self.assertEqual(self.dict.bisect_left('d'), 1)
        self.assertEqual(self.dict.bisect_left('c'), 1)
        self.assertEqual(self.dict.bisect_left('k'), 2) # there is 'd' at index 1
        self.assertEqual(self.dict.bisect_left('z'), 4)
        
    def test_bisect_right(self):
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 4
        self.assertEqual(self.dict.bisect_right('a'), 1)
        self.assertEqual(self.dict.bisect_right('A'), 0)
        self.assertEqual(self.dict.bisect_right('b'), 1)
        self.assertEqual(self.dict.bisect_right('d'), 2)
        self.assertEqual(self.dict.bisect_right('c'), 1)
        self.assertEqual(self.dict.bisect_right('k'), 3) 
        self.assertEqual(self.dict.bisect_right('z'), 4)
        
    def test_peekitem(self):
        self.dict['a'] = 1
        self.dict['k'] = 11
        self.dict['m'] = 13
        self.dict['d'] = 4
        self.assertEqual(self.dict.peekitem(0), ('a', 1))
        self.assertEqual(self.dict.peekitem(1), ('d', 4))
        self.assertEqual(self.dict.peekitem(2), ('k', 11))
        self.assertEqual(self.dict.peekitem(3), ('m', 13))
        self.assertEqual(self.dict.peekitem(-1), ('m', 13))
        self.assertEqual(self.dict.peekitem(-2), ('k', 11))
        self.assertEqual(self.dict.peekitem(-3), ('d', 4))
        self.assertEqual(self.dict.peekitem(-4), ('a', 1))
        with self.assertRaises(IndexError):
            self.dict.peekitem(4)
        with self.assertRaises(IndexError):
            self.dict.peekitem(-5)