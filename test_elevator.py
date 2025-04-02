import unittest
from main import elevator

class TestElevatorFunction(unittest.TestCase):

    def test_basic_movement(self):
        self.assertEqual(elevator(12, [2, 9, 1, 32]), (560, [12, 9, 2, 1, 32]))

    def test_only_downward(self):
        self.assertEqual(elevator(6, [2, 4]), (40, [6, 4, 2]))

    def test_only_upward(self):
        self.assertEqual(elevator(2, [5, 8]), (60, [2, 5, 8]))

    def test_mixed_floors(self):
        self.assertEqual(elevator(5, [2, 8, 3]), (90, [5, 3, 2, 8]))

    def test_no_floors_to_visit(self):
        self.assertEqual(elevator(4, []), (0, [4]))

    def test_single_floor_visit(self):
        self.assertEqual(elevator(3, [6]), (30, [3, 6]))

    def test_unordered_floors(self):
        self.assertEqual(elevator(7, [10, 3, 5]), (80, [7, 5, 3, 10]))

if __name__ == '__main__':
    unitt
