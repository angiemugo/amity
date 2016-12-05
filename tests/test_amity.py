import unittest
from app.amity import Amity


class TestClassAmity(unittest.TestCase):

    def test_room_added_to_list(self):
        Amity.amity_rooms = {}
        Amity.create_room("Purple", "office")
        self.assertIn("Purple", Amity.amity_rooms.keys(), msg="rooms should be added to dictionary amity_rooms")
        Amity.amity_rooms = {}


if __name__ == '__main__':
    unittest.main()



            #def test_default_wants_accomodation(self):


