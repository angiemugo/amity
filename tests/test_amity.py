import unittest
from ..App.Amity import AmityClass
from ..App.Room import Office,Lspace


class ClassAmitySuccessTest(unittest.TestCase):

    def test_office_added_to_list(self):
        AmityClass.amity_offices = []
        self.assertFalse("Purple" in AmityClass.amity_offices)
        AmityClass.create_room("Purple", "office")
        self.assertTrue("Purple" in AmityClass.amity_offices)
        new_office_count = len(AmityClass.amity_offices)
        self.assertEqual(self.previous_office_count + 1, new_office_count)

    def test_office_added_to_list(self):
        AmityClass.amity_lspaces = []
        self.assertFalse("Yellow" in AmityClass.amity_lspaces)
        AmityClass.create_room("Yellow", "lspaces")
        self.assertTrue("Yellow" in AmityClass.amity_lspaces)
        new_lspaces_count = len(AmityClass.amity_lspaces)
        self.assertEqual(self.previous_lspaces_count + 1, new_lspaces_count)

    def test_office_allocation(self):
        AmityClass.office_allocations = []
        self.assertEqual(len(AmityClass.office_allocations), 0)
        AmityClass.create_person("Angie", "Staff")
        self.assertNotEqual(len(AmityClass.office_allocations), 0)

    def test_lspace_allocation(self):
        AmityClass.lspace_allocations = []
        self.assertEqual(len(AmityClass.lspace_allocations), 0)
        AmityClass.create_person("mugo", "staff")
        self.assertEqual(len(AmityClass.lspace_allocations), 0, msg="staff cannot be assigned a living space")
        AmityClass.create_person("njeri", "fellow")
        self.assertEqual(len(AmityClass.lspace_allocations), 0, msg="a fellow is assigned a room by default")



























if __name__ == '__main__':
    unittest.main()
