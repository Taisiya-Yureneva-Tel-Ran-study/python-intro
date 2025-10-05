from dataclasses import dataclass, field
from sortedcontainers import SortedSet, SortedKeyList
from math import inf

@dataclass(order=True, unsafe_hash=True)
class Person:
    id: int
    age: int = field(compare=False)
    name: str = field(compare=False)

class Dictionary:
    def __init__(self):
        self.__words = SortedSet()
        self.__sortedWords = SortedKeyList(key=str.lower)
        
    def addWord(self, word: str):
        if word.lower() in self.__words:
            raise ValueError(f'Word "{word}" already exists')
        self.__words.add(word.lower())
        self.__sortedWords.add(word)
        
    def getWords(self) -> list[str]:
        return list(self.__sortedWords)
        
    def getWordsByPrefix(self, prefix: str) -> list[str]:
        start = prefix
        end = prefix + chr(0x10FFFF)
        return list(self.__sortedWords.irange(start, end))
        
class Club:
    def __init__(self):
        self.__sortedSet = SortedSet()
        self.__sortedKeyList = SortedKeyList(key=lambda person: (person.age, person.id))
        
    def addPerson(self, person: Person):
        if person in self.__sortedSet:
            raise ValueError(f'Person with id {person.id} already exists')
        self.__sortedSet.add(person)
        self.__sortedKeyList.add(person)
    
    def getPersonsSortedById(self) -> list[Person]:
        return list(self.__sortedSet)
        
    def getPersonsSortedByAgeAndId(self) -> list[Person]:
        return list(self.__sortedKeyList)
    
    def getPersonsByAge(self, minAge:int, maxAge:int) -> list[Person]:
        start = Person(0, minAge, '')
        # I guess, this is the nuance, we need to use some max value for id
        # to ensure that we get all persons with maxAge
        end = Person(inf, maxAge, '')
        return list(self.__sortedKeyList.irange(start, end))

