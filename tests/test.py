import unittest
from app.amity import Amity
from collections import defaultdict
import os


class ClassAmitySuccessTest(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()
        self.amity.all_people = []
        self.amity.all_rooms = []
        self.amity.office_allocations = defaultdict()
        self.amity.lspace_allocations = defaultdict()
        self.amity.fellows_list = []
        self.amity.staff_list = []

    def test_add_person(self):
        self.amity.add_person("awesome", "fellow","y")
        self.assertEqual(len(self.amity.all_people), 1)

    def test_room_added_to_list(self):
        self.amity.create_room("purple", "office")
        self.assertEqual(len(self.amity.all_rooms), 1)

    def test_office_allocation(self):
        self.amity.add_person("Angie", "Staff", "Y")
        for room, occupants in self.amity. office_allocations:
            self.assertIn("Angie", self.amity.office_allocations[occupants])

    def test_lspace_allocation(self):
        self.amity.add_person("Angie", "fellow", "Y")
        for room, occupants in self.amity.lspace_allocations:
            self.assertIn("Angie", self.amity.lspace_allocations[occupants])

    def test_reallocate_person(self):
        self.amity.reallocate_person("angie","blue")
        self.assertIn("Angie", self.amity.office_allocations["blue"])

    def test_person_is_removed_from_old_room(self):
        self.amity.add_person("angie","staff")
        self.assertin("Angie", self.amity.office_allocations["blue"])
        self.amity.reallocate_person("angie","yellow")
        self.assertnotin("Angie", self.amity.office_allocations["blue"])

    def test_load_from_file(self, filename):

        self.amity.load_people(self, filename)
        self.assertEqual(len(self.amity.fellows_list), 4)
        self.assertEqual(len(self.amity.staff_list), 3)

    def test_it_prints_allocations(self):
        Amity.print_allocations('test.txt')
        self.assertTrue(os.path.isfile('test.txt'))
        os.remove('test.txt')

    def test_it_prints_unallocated(self):
        Amity.print_unallocated('test.txt')
        self.assertTrue(os.path.isfile('test.txt'))
        os.remove('test.txt')

    def test_it_saves_state(self):
        Amity.save_state('test.db')
        self.assertTrue(os.path.isfile('test.db'))
        os.remove('test.db')


if __name__ == '__main__':
    unittest.main()
