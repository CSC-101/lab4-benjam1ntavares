import data
from math import sqrt
from data import Point

# Write your functions for each part in the space below.
#########################################################
# Part 1
# Function first_element will take an imput of a nested integer lists and returns a list containing the first element
# in each nested list from the input

def first_element(inlist: list[list[int]]) -> list[int]:
    first_elements = []
    for list in inlist:
        if len(list) > 0:
            first_elements.append(list[0])
    return first_elements

#########################################################
# Part 2
#Function x_coordinates takes a parameter of type list[point] (using the point class) and returns a list of the x
# coordinate in each point
def x_coordinates(points: list[data.Point]) -> list[float]:
    x_coordinates = []
    for point in points:
        x_coordinates.append(int(point.x))
    return x_coordinates

#########################################################
# Part 3
# Function are_in_positive_quadrant takes one parameter of type list[Point] and that returns all points from the input
# list that are in the first quadrant (i.e., both x- and y-components are positive) of the Cartesian plane.
def are_in_positive_quadrant(points: list[data.Point]) -> list[data.Point]:
    positive_points = []
    for point in points:
        if point.x >= 0 and point.y >= 0:
            positive_points.append(point)
    return positive_points

# Part 4
# Function distance takes two parameters of type Point and returns the Euclidean distance to an external site. (a float)
# between these two points.

# imported math.sqrt to take the square root
def euclidean_distance(point1: data.Point, point2: data.Point) -> float:
    x_distance = point1.x - point2.x
    y_distance = point1.y - point2.y
    return sqrt(x_distance**2 + y_distance**2)


# Part 5
# Funciton manhattan_distance takes two (Point) parameters and returns the manhattan distance between the two points
def manhattan_distance(point1: data.Point, point2: data.Point) -> float:
    x_distance = abs(point1.x - point2.x)
    y_distance = abs(point1.y - point2.y)
    return x_distance + y_distance

# Part 6
# Function distance_all takes a single parameter of type list[Point] (list of points) and returns each of the points
# distances from the origin (using one of the distance funcitons from above)

def distance_all(points: list[Point]) -> list[float]:
    distances = []
    for point in points:
        distances.append(manhattan_distance(Point(0,0), point))
    return distances