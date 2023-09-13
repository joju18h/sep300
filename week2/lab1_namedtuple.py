from collections import namedtuple
from math import *

#Point class
Point = namedtuple('Point', ['x', 'y'])

#class instances
p1 = Point(4,5)
p2 = Point(2,3)

distance = dist(p1,p2)
print("Distance between the two points on the x-axis:", abs((p2.x - p1.x)))
print("Distance between the two points: %.2f" %distance)

