from dataclasses import dataclass, field
from typing import Generic, Hashable, TypeVar
from collections import OrderedDict
from sortedcontainers import SortedSet

K = TypeVar('K', bound=Hashable)
V = TypeVar('V')

@dataclass(order=True, frozen=True)
class Entry(Generic[K, V]):
    key: K
    val: V = field(compare=False, hash=False)
    def __str__(self) -> str:
        return f"{self.key}: {self.val}"
    
class MyDictionary(Generic[K, V]):
    def __init__(self):
        self.__entries: set[Entry[K, V]] = set()
        
    def __getitem__(self, key: K) -> V:
        entry: Entry[K, V] = self.__getEntryByKey(key)
        if not entry:
            raise KeyError(key)
        return entry.val
    
    def __getEntryByKey(self, key: K) -> Entry[K, V]:
        res: Entry[K, V] = None
        probe: Entry[K, V] = Entry(key, None)
        if probe in self.__entries:
            res = next((e for e in self.__entries if e == probe))
        return res
    
    def __setitem__(self, key: K, val: V):
        probe: Entry[K, V] = Entry(key, val)
        self.__entries.discard(probe)
        self.__entries.add(probe)
        
    def __str__(self) -> str:
        return "{" + ", ".join([str(e) for e in self.__entries]) + "}"
        
    # HW #24
    def __len__(self):
        # returns count of the entries
        # this is a magic method allowing using the function len of Python
        return sum(1 for _ in self.__entries)
        # return len(self.__entries) # I'm not sure i can use it, but it's available for set and more efficient
    
    def setdefault(self, key: K, default: V = None):
        # If key missing, insert key: default; return the default.
        # If key exists, no insert, no update; return the value
        probe: Entry[K, V] = Entry(key, default)
        res: V = default
        if probe in self.__entries:
            res = self.__getEntryByKey(key).val
        else:
            self.__entries.add(probe)
        return res
    
    def get(self, key: K, default: V = None):
        # returns value for key or any default if key missing
        probe: Entry[K, V] = Entry(key, default)
        res = default
        if probe in self.__entries:
            res = self.__getEntryByKey(key).val
        return res
    
    def items(self) -> list[(K,  V)]:
        # returns list of tuples (key, value)
        # tuple is an immutable list 
        # [1, 2] - list, (1, 2) - tuple
        # assume that e is Entry, then to create tuple from Entry e - (e.key, e.value)
        # try to write one code line using so called comprehension expresson
        # [<expression with item> for <item> in <items>] 
       return [(e.key, e.val) for e in self.__entries]
    
    def keys(self) -> list[K]:
        # returns list of keys
        return [e.key for e in self.__entries]
    
    def values(self) -> list[V]:
        # returns list of values
        return [e.val for e in self.__entries]
    
    def update(self, key: K, value: V):
        # if key exists, updates value for the key
        # if key missing, inserts key: value entry
        probe: Entry[K, V] = Entry(key, value)
        self.__entries.discard(probe)
        self.__entries.add(probe)
    
    _sentinel = object()
    def pop(self, key: K, default=_sentinel)->V:
        # removes key if the key exists, return the associated value
        # line 72 with default value is intended for differentiating optional parameter. As None may be value passed by a caller 
        # if default is _sentinel, a caller has not passed default value.
        # Operator "is" implies the same reference. It differs from '==' (equility) 
        # if key missing and default value having been passed that value will be returned
        # if key missing and default value not passed KeyError should be raised
        res: V = default if default is not self._sentinel else None
        probe: Entry[K, V] = Entry(key, default)
        if probe in self.__entries:
            res = self.__getEntryByKey(key).val
            self.__entries.discard(probe)
        else: 
            if default is self._sentinel:
                raise KeyError(key)
        return res 
        
 ###########################################################################################
class MySortedDict(Generic[K,V]):
    def __init__(self) :
        self.__entries: SortedSet[K, V] = SortedSet()       
    
    def __getitem__(self, key: K) -> V :
        # see implementation of MyDict,
        # but it should be implemented with O[LogN] complexity
        raise NotImplementedError()    
    def __setitem__(self, key: K, value: V):
        # TODO see implementation of MyDict, O[LogN] complexity
        raise NotImplementedError()    
    
    def __str__(self) :
        return  '{' + ", ".join([str(e) for e in self.__entries]) + '}'
    
    def __len__(self):
        # returns count of the entries
        # this is a magic method allowing using the function len of Python
        raise NotImplementedError()
    def setdefault(self, key: K, default: V = None):
        # TODO: If key missing, insert key: default; return the default.
        #    If key exists, no insert, no update; return the value
        raise NotImplementedError()
    
    def get(self, key: K, default: V = None):
        # TODO returns value for key or any default if key missing
        # O[LogN] complexity
        raise NotImplementedError()
    
    def items(self) -> list[(K,  V)]:
        # returns list of tuples (key, value)
        # tuple is an immutable list 
        # [1, 2] - list, (1, 2) - tuple
        # assume that e is Entry, then to create tuple from Entry e - (e.key, e.value)
        # try to write one code line using so called comprehension expresson
        # [<expression with item> for <item> in <items>] 
       return [(e.key, e.value) for e in self.__entries]
    
    def keys(self) -> list[K]:
        # TODO returns list of keys
        raise NotImplementedError()
    
    def values(self) -> list[V]:
        # TODO returns list of values
        raise NotImplementedError()
    
    def update(self, key: K, value: V):
        # TODO if key exists, updates value for the key
        # if key missing, inserts key: value entry
        raise NotImplementedError()
    _sentinel = object()
    def pop(self, key: K, default=_sentinel) -> V:
        # TODO removes key if the key exists with returning associated value
        # if key missing and default exists, returns default
        
        raise NotImplementedError() 
    def bisect_left(self, key:K)->int:
        # TODO returns first index of key that >= a given key
        raise NotImplementedError()
    def bisect_right(self, key:K)->int:
        # TODO returns first index of key that > a given key
        raise NotImplementedError()
    def peekitem(self, ind: int)->tuple[K,V] :
        # TODO returns received from Entry tuple at a specified index
        # may take a negative index with meaning the indexing from the end (index -1 designates the kast key
        # raises error for an index out of a possible range (index < -len(self) or index >= len(self))
        raise NotImplementedError()
  ####################################################################################
  
class DictCache(OrderedDict[K, V]) :
    def __init__(self, maxsize=128):
        super().__init__() # calls constructor of OrderedDict that has all methods for keeping insertion order
        self.maxsize = maxsize
    # TODO     
    # The  methods __getitem__ and __setitem__ should be overriden
    # Assumption: only following methods should be overriden for making tests from test_dict_cache.py passed
    # Hints as follows: 
    # super().__getitem__(key) calls method __getitem__ of OrderedDict
    # super().__setitem__(key, value) calls method __setitem__ of OrderedDict
    # consider using self.move_to_end(key) of OrderedDict for making item with the given key as most recent
    # consider using self.popitem(last=False) for removing least recent (eldest item)
    
    def __getitem__(self, key):
        raise NotImplementedError()

    def __setitem__(self, key, value):
        raise NotImplementedError()
    
if __name__ == "__main__":
    aMap: dict[str, int] = dict()
    dict: MyDictionary[str, int] = MyDictionary()
    aMap["a"] = 1
    dict["b"] = 2
    dict["d"] = 9
    print(aMap, dict)