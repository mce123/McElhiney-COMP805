"""
Lab 4 Test Function
test_lab4.py
Patrick R. McElhiney
2/13/2018
"""

import unittest

class Lab4Test(unittest.TestCase):

    def test_squared(self):
        """
        Tests lab4.squared_nums()
        """
        func = lab4.squared_nums
        case1 = [1, 2, 3]
        expected1 = [1, 4, 9]
        self.assertEqual(func(case1), expected1)

        case2 = []
        expected2 = []
        self.assertEqual(func(case2), expected2)

        case3 = [2, 4, 6]
        expected3 = [4, 16, 36]
        self.assertEqual(func(case3), expected3)

    def test_check_title(self):
        """
        Tests lab4.check_title()
        """
        func = lab4.check_title
        case1 = ['Hello World', 'Hello_world', 'Hello_World']
        expected1 = ['Hello World', 'Hello_World']
        self.assertEqual(func(case1), expected1)

        case2 = []
        expected2 = []
        self.assertEqual(func(case2), expected2)

        case3 = ['Hi There']
        expected3 = ['Hi There']
        self.assertEqual(func(case3), expected3)

    def test_restock_inventory(self):
        """
        Tests lab4.restock_inventory()
        """
        func = lab4.restock_inventory
        case1 = {'apples':5, 'oranges':10, 'peaches':50}
        expected1 = {'peaches': 60, 'apples': 15, 'oranges': 20}
        self.assertEqual(func(case1), expected1)

        case2 = {}
        expected2 = {}
        self.assertEqual(func(case2), expected2)

        case3 = {'bullets':100, 'guns':25, 'grenades':50}
        expected3 = {'bullets': 110, 'guns': 35, 'grenades': 60}
        self.assertEqual(func(case3), expected3)

    def test_filter_0_items(self):
        """
        Tests lab4.filter_0_items()
        """
        func = lab4.filter_0_items
        case1 = {'apples':0, 'oranges':10, 'peaches':50}
        expected1 = {'peaches': 50, 'oranges': 10}
        self.assertEqual(func(case1), expected1)

        case2 = {'apples':0, 'oranges':0, 'peaches':250}
        expected2 = {'peaches': 250}
        self.assertEqual(func(case2), expected2)

        case3 = {'bullets':100, 'guns':0, 'grenades':50}
        expected3 = {'bullets': 100, 'grenades': 50}
        self.assertEqual(func(case3), expected3)

    def test_average_grades(self):
        """
        Tests lab4.average_grades()
        """
        func = lab4.average_grades
        case1 = {'Michael' :[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}
        expected1 = {'Michael': 89, 'Daniel': 79.0, 'Josh': 87}
        self.assertEqual(func(case1), expected1)

        case2 = {'Michael':[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]}
        expected2 = {'Michael': 94.0, 'Daniel': 52.6625, 'Josh': 88.5}
        self.assertEqual(func(case2), expected2)

        case3 = {'Michael' :[78], 'Daniel':[90], 'Josh':[900/-9]}
        expected3 = {'Michael': 78, 'Daniel': 90, 'Josh': -100}
        self.assertEqual(func(case3), expected3)


if __name__ == '__main__':
    try:
        import lab4
        print("lab4.py module found. Testing...")
        unittest.main()
    except ImportError:
        print("Missing lab4.py module")
