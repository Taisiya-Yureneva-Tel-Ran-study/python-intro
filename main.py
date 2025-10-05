from dataclasses import dataclass, field
from sortedcontainers import SortedSet, SortedKeyList
from math import inf

@dataclass(order=True, unsafe_hash=True)
class Person:
    id: int
    age: int = field(compare=False)
    name: str = field(compare=False)

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

if __name__ == "__main__":
    club = Club()
    prs1 = Person(123, 20, 'Vasya')
    prs2 = Person(20, 30, 'Misha')
    prs3 = Person(33, 40, 'Shasha')
    prs4 = Person(5, 40, 'Masha')
    
    club.addPerson(prs1)
    club.addPerson(prs2)
    club.addPerson(prs3)
    club.addPerson(prs4)
    
    print(club.getPersonsSortedById())
    print(club.getPersonsSortedByAgeAndId())
    print(club.getPersonsByAge(20, 30))
