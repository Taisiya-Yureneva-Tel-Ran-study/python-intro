from unittest import TestCase
from main import Club, Person

class ClubTest(TestCase):
    def setUp(self):
        self.club: Club = Club()
        self.prs1 = Person(123, 20, 'Vasya')
        self.prs2 = Person(20, 30, 'Misha')
        self.prs3 = Person(33, 40, 'Shasha')
        self.prs4 = Person(5, 40, 'Masha')
        self.invalid_person = Person(123, 25, 'Invalid')
        
    def test_add_person(self):
        self.club.addPerson(self.prs1)
        self.club.addPerson(self.prs2)
        self.club.addPerson(self.prs3)
        self.club.addPerson(self.prs4)
        self.assertEqual(self.club.getPersonsSortedById(), [self.prs4, self.prs2, self.prs3, self.prs1])
        self.assertEqual(self.club.getPersonsSortedByAgeAndId(), [self.prs1, self.prs2, self.prs4, self.prs3])

    def test_add_duplicate_id_person(self):
        self.club.addPerson(self.prs1)
        with self.assertRaises(ValueError):
            self.club.addPerson(self.invalid_person)
            
    def test_get_persons_sorted_by_id(self):
        self.club.addPerson(self.prs1)
        self.club.addPerson(self.prs2)
        self.club.addPerson(self.prs3)
        self.club.addPerson(self.prs4)
        self.assertEqual(self.club.getPersonsSortedById(), [self.prs4, self.prs2, self.prs3, self.prs1])
        
    def test_get_persons_sorted_by_age_and_id(self):
        self.club.addPerson(self.prs1)
        self.club.addPerson(self.prs2)
        self.club.addPerson(self.prs3)
        self.club.addPerson(self.prs4)
        self.assertEqual(self.club.getPersonsSortedByAgeAndId(), [self.prs1, self.prs2, self.prs4, self.prs3])
        
    def test_get_persons_by_age(self):
        self.club.addPerson(self.prs1)
        self.club.addPerson(self.prs2)
        self.club.addPerson(self.prs3)
        self.club.addPerson(self.prs4)
        # Inclusive range
        self.assertEqual(self.club.getPersonsByAge(20, 30), [self.prs1, self.prs2])
        # Edge case: no persons in range
        self.assertEqual(self.club.getPersonsByAge(50, 60), [])
        