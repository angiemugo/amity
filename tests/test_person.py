
import unittest
from App.Amity import AmityClass
from App.Employee import Fellow,Staff


class TestPerson(unittest.TestCase):
    def test_fellow_is_created(self):

        self.angie = Staff("Angie")
        self.assertEqual(self.angie.person_name, "Angie")
        self.assertEqual(self.angie.person_description, "staff")

    def test_staff_is_created(self):
        self.mugo = Fellow("Mugo")
        self.assertEqual(self.mugo.person_name, "Mugo")
        self.assertEqual(self.mugo.person_description, "fellow")




