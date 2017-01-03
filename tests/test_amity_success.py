import unittest
from app.amity import Amity
from collections import defaultdict


class ClassAmitySuccessTest(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()

    def test_add_person(self):
        self.amity.all_people = []
        self.assertEqual(len(self.amity.all_people), 0)
        self.amity.add_person("awesome", "fellow","y" )
        self.assertNotEqual(len(self.amity.all_people), 0)
        self.amity.all_people = []



    def test_office_added_to_list(self):
        self.amity.office_list = []
        self.assertEqual(len(self.amity.all_rooms), 0)
        self.amity.create_room("purple", "office")
        self.assertNotEqual(len(self.amity.all_rooms), 0)
        self.amity.office_list = []

    def test_lspace_added_to_list(self):
        self.amity.lspace_list = []
        self.assertEqual(len(self.amity.all_rooms), 0)
        self.amity.create_room("purple", "lspace")
        self.assertNotEqual(len(self.amity.all_rooms), 0)
        self.amity.lspace_list = []


    def test_office_allocation(self):
        self.amity.office_allocations = defaultdict()
        self.amity.add_person("Angie", "Staff", "Y")
        for room, occupants in self.amity. office_allocations:
            self.assertIn("Angie", self.amity.office_allocations[occupants])
        self.amity.office_allocations = defaultdict()

    def test_lspace_allocation(self):
        self.amity.lspace_allocations = defaultdict()
        self.amity.add_person("Angie", "fellow", "Y")
        for room, occupants in self.amity.lspace_allocations:
            self.assertIn("Angie", self.amity.lspace_allocations[occupants])
        self.amity.lspace_allocations = defaultdict()

    def test_reallocate_person(self):
        self.amity.office_allocations = {}
        self.amity.reallocate_person("angie","blue")
        self.assertIn("Angie", self.amity.office_allocations["blue"])
        self.amity.office_allocations = {}

    def test_load_from_file(self, people_file):
        self.amity.fellows_list = []
        self.amity.staff_list = []
        self.assertEqual(len(self.amity.fellows_list), 0)
        self.assertEqual(len(self.amity.staff_list),0)
        self.amity.load_people(self, people_file)
        self.assertEqual(len(self.amity.fellows_list), 4)
        self.assertEqual(len(self.amity.staff_list), 3)


if __name__ == '__main__':
    unittest.main()
