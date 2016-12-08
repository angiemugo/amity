import unittest
from App.Amity import AmityClass
from App.Room import Office,Lspace


class TestRoom(unittest.TestCase):
    def test_office_is_created(self):
        self.purple = AmityClass.create_office("Purple", "office")
        self.assertEqual(self.purple.room_name, "PURPLE")
        self.assertEqual(self.purple.room_description, "OFFICE")

    def test_lspace_is_created(self):
        self.yellow = AmityClass.create_lspace("yellow", "lspace")
        self.assertEqual(self.yellow.room_name, "YELLOW")
        self.assertEqual(self.yellow.room_description, "LSPACE")


