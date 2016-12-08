import unittest
from App.Amity import AmityClass


class TestRoom(unittest.TestCase):
    def test_office_is_created(self):
        office = AmityClass.create_office("Purple", "office")
        self.assertEqual(office.person_name, "PURPLE")
        self.assertEqual(office.person_description, "OFFICE")

    def test_lspace_is_created(self):
        lspace = AmityClass.create_lspace("yellow", "lspace")
        self.assertEqual(lspace.person_name, "YELLOW")
        self.assertEqual(lspace.person_description, "YELLOW")


