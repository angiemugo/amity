
import unittest
from ..App.Amity import AmityClass


class TestPerson(unittest.TestCase):
    def Test_fellow_is_added(self):
        AmityClass.create_person("Angie", "staff")
        self.assertEqual(self.person_name, "Angie")
        self.assertEqual(self.person_description, "staff")

    def Test_staff_is_added(self):
        AmityClass.create_person("Mugo", "fellow")
        self.assertEqual(self.person_name, "Mugo")
        self.assertEqual(self.person_designation, "staff")


