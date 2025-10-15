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
        return f"'{self.key}': {self.val}"
    
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
        self.__setitem__(key, value)
    
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
        res = self.__getEntryByKey(key)
        if not res:
            raise KeyError(key)
        return res.val
    
    def __getEntryByKey(self, key: K) -> Entry[K, V]:
        probe: Entry[K, V] = Entry(key, None)
        res = None
        if probe in self.__entries:
            res = self.__entries.bisect_left(probe)
        return self.__entries[res] if res is not None else None
        
        
    def __setitem__(self, key: K, value: V):
        # see implementation of MyDict, O[LogN] complexity
        probe = Entry(key, value)
        self.__entries.discard(probe)
        self.__entries.add(probe)
    
    def __str__(self) :
        return  '{' + ", ".join([str(e) for e in self.__entries]) + '}'
    
    def __len__(self):
        # returns count of the entries
        # this is a magic method allowing using the function len of Python
        return sum(1 for _ in self.__entries)
    
    def setdefault(self, key: K, default: V = None):
        # If key missing, insert key: default; return the default.
        # If key exists, no insert, no update; return the value
        probe: Entry[K, V] = Entry(key, default)
        if probe in self.__entries:
            probe = self.__getEntryByKey(key)
        else:
            self.__entries.add(probe)
        return probe.val
    
    def get(self, key: K, default: V = None) -> V:
        # returns value for key or any default if key missing
        # O[LogN] complexity
        probe: Entry[K, V] = Entry(key, default)
        if probe in self.__entries:
            probe = self.__getEntryByKey(key)
        return probe.val if probe else default
    
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
        return [(e.key) for e in self.__entries]
    
    def values(self) -> list[V]:
        # returns list of values
        return [(e.val) for e in self.__entries]
    
    def update(self, key: K, value: V):
        # TODO if key exists, updates value for the key
        # if key missing, inserts key: value entry
        self.__setitem__(key, value)
    
    _sentinel = object()
    def pop(self, key: K, default=_sentinel) -> V:
        # removes key if the key exists with returning associated value
        # if key missing and default exists, returns default
        res: V = default if default is not self._sentinel else None
        probe: Entry[K, V] = Entry(key, default)
        if probe in self.__entries:
            res = self.__getEntryByKey(key).val
            self.__entries.discard(probe)
        else: 
            if default is self._sentinel:
                raise KeyError(key)
        return res 

    def bisect_left(self, key:K)->int:
        # returns first index of key that >= a given key
        probe: Entry[K, V] = Entry(key, None)
        return self.__entries.bisect_left(probe)

    def bisect_right(self, key:K)->int:
        # returns first index of key that > a given key
        probe: Entry[K, V] = Entry(key, None)
        return self.__entries.bisect_right(probe)
    
    def peekitem(self, ind: int)->tuple[K,V] :
        # returns received from Entry tuple at a specified index
        # may take a negative index with meaning the indexing from the end (index -1 designates the last key
        # raises error for an index out of a possible range (index < -len(self) or index >= len(self))
        e: Entry[K, V] = self.__entries[ind]
        return (e.key, e.val)
    
  ####################################################################################
  
class DictCache(OrderedDict[K, V]) :
    def __init__(self, maxsize=128):
        super().__init__() # calls constructor of OrderedDict that has all methods for keeping insertion order
        self.maxsize = maxsize
    
    def __getitem__(self, key):
        if key not in self:
            raise KeyError(key)
        self.move_to_end(key)
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        if len(self) > self.maxsize:
            self.popitem(last=False)

    
if __name__ == "__main__":
    aMap: dict[str, int] = dict()
    dict: MyDictionary[str, int] = MyDictionary()
    aMap["a"] = 1
    dict["b"] = 2
    dict["d"] = 9
    print(aMap, dict)