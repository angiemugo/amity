import unittest
import App.Amity


class ClassAmitySuccessTest(unittest.TestCase):

    def test_office_added_to_list(self):
        App.Amity.AmityClass.amity_offices = []
        self.assertFalse("Purple" in App.Amity.AmityClass.amity_offices)
        App.Amity.AmityClass.create_room("Purple", "office")
        self.assertTrue("Purple" in App.Amity.AmityClass.amity_offices)
        new_office_count = len(App.Amity.AmityClass.amity_offices)
        self.assertEqual(self.previous_office_count + 1, new_office_count)

    def test_office_added_to_list(self):
        App.Amity.AmityClass.amity_lspaces = []
        self.assertFalse("Yellow" in App.Amity.AmityClass.amity_lspaces)
        App.Amity.AmityClass.create_room("Yellow", "lspaces")
        self.assertTrue("Yellow" in App.Amity.AmityClass.amity_lspaces)
        new_lspaces_count = len(App.Amity.AmityClass.amity_lspaces)
        self.assertEqual(self.previous_lspaces_count + 1, new_lspaces_count)

    def test_office_allocation(self):
        App.Amity.AmityClass.office_allocations = []
        self.assertEqual(len(App.Amity.AmityClass.office_allocations), 0)
        App.Amity.AmityClass.create_person("Angie", "Staff")
        self.assertNotEqual(len(App.Amity.AmityClass.office_allocations), 0)

    def test_lspace_allocation(self):
        App.Amity.AmityClass.lspace_allocations = []
        self.assertEqual(len(App.Amity.AmityClass.lspace_allocations), 0)
        App.Amity.AmityClass.create_person("mugo", "staff")
        self.assertEqual(len(App.Amity.AmityClass.lspace_allocations), 0,
                         msg="staff cannot be assigned a living space")
        App.Amity.AmityClass.create_person("njeri", "fellow")
        self.assertNotEqual(len(App.Amity.AmityClass.lspace_allocations), 0,
                            msg="a fellow is assigned a room by default")

    def test_reallocate_person(self):
        App.Amity.AmityClass.office_allocations = []
        self.assertIn("Angie", "Purple",
                      msg="Angie is assigned to room purple")
        App.Amity.AmityClass.reallocate_person("angie")
        self.assertNotEqual("Angie","purple", msg="Angie not assigned to purple")

    def test_load_from_file(self):
        App.Amity.AmityClass. amity_fellows = []
        App.Amity.AmityClass. amity_staff = []
        self.assertEqual(len(self.amity_fellows, 0))
        self.assertEqual(len(self.amity_staff,0))
        App.Amity.AmityClass.load_people()
        self.assertEqual(len(self.amity_fellows, 4))
        self.assertEqual(len(self.amity_staff, 3))

























if __name__ == '__main__':
    unittest.main()
