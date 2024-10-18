import data
import lab4
import unittest

from data import Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # first_element test 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    # first_element test 2 (empty nested list)
    def test_first_element_2(self):
        input = [[12,3,4,5],[],[2,1,1,1,1], [3,2,3,4,5,6,7,8,9,10], [4],[5,2]]
        result = lab4.first_element(input)
        expected = [12,2,3,4,5]
        self.assertEqual(expected, result)

    # x_coordinate test 1
    def test_x_coordinate_1(self):
        input = [Point(1,2), Point(3,4), Point(5,6), Point(7,8), Point(9,10)]
        result = lab4.x_coordinates(input)
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(expected, result)

    # x_coordinate test 2
    def test_x_coordinate_2(self):
        input = [Point(4,7), Point(3,2), Point(2,1), Point(1,0)]
        result = lab4.x_coordinates(input)
        expected = [4, 3, 2, 1]
        self.assertEqual(expected, result)

    # positive_quadrant test 1
    def test_are_in_positive_quadrant_1(self):
        input = [Point(1,2), Point(3,4), Point(5,6), Point(7,8), Point(9,10)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [Point(1,2), Point(3,4), Point(5,6), Point(7,8), Point(9,10)]
        self.assertEqual(expected, result)
    # positive_quadrant test 2
    def test_are_in_positive_quadrant_2(self):
        input = [Point(-1,2), Point(3,-4), Point(-5,-6), Point(7,8), Point(0,0)]
        result = lab4.are_in_positive_quadrant(input)
        expected = [Point(7,8), Point(0,0)]
        self.assertEqual(expected, result)

    # Euclidean distance test 1
    def test_euclidean_distance_1(self):
        input1 = Point(1,2)
        input2 = Point(1,4)
        result = lab4.euclidean_distance(input1,input2)
        expected = 2.0
        self.assertEqual(expected, result)
    # Euclidean distance test 2
    def test_euclidean_distance_2(self):
        input1 = Point(1,2)
        input2 = Point(1,2)
        result = lab4.euclidean_distance(input1,input2)
        expected = 0
        self.assertEqual(expected, result)
    # Euclidean distance test 3
    def test_euclidean_distance_2(self):
        input1 = Point(-1, 2)
        input2 = Point(1, 2)
        result = lab4.euclidean_distance(input1, input2)
        expected = 2
        self.assertEqual(expected, result)

    # manhattan_distance test 1
    def test_manhattan_distance_1(self):
        input1 = Point(-1, 2)
        input2 = Point(1, 2)
        result = lab4.manhattan_distance(input1, input2)
        expected = 2
        self.assertEqual(expected, result)

    # manhattan distance test 2
    def test_manhattan_distance_2(self):
        input1 = Point(1, 1)
        input2 = Point(5, 5)
        result = lab4.manhattan_distance(input1, input2)
        expected = 8
        self.assertEqual(expected, result)

    # distance_all test 1
    def test_distance_all_1(self):
        input = [Point(1, 1), Point(5, 5), Point(3, 7)]
        result = lab4.distance_all(input)
        expected = [2, 10, 10]
        self.assertEqual(expected, result)

    # distance_all test 2
    def test_distance_all_1(self):
        input = [Point(-2, -2), Point(-2, 2), Point(6, -5)]
        result = lab4.distance_all(input)
        expected = [4,4,11]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
