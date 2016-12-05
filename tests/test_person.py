import unittest
from amity.app.employee import Person, Fellow


class TestClassFellow(unittest.TestCase):
    def setUp(self):
        self.fellow1 = Fellow("001", "angie")

    def test_Is_Instance(self):
        self.assertIsInstance(self.fellow1, Person, msg="fellow is an instance of class Person")

if __name__ == '__main__':
    unittest.main()
