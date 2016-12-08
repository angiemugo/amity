
import unittest
from App.Amity import AmityClass


class TestPerson(unittest.TestCase):
    def test_fellow_is_created(self):
        person = AmityClass.create_person("Angie", "staff")
        self.assertEqual(person.person_name, "Angie")
        self.assertEqual(person.person_description, "staff")

    def test_staff_is_created(self):
        fellow = AmityClass.create_person("Mugo", "fellow")
        self.assertEqual(fellow.person_name, "Mugo")
        self.assertEqual(fellow.person_designation, "staff")


