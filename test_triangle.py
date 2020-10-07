# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """define multiple sets of tests as functions with names that begin"""

    def test_right_triangle_a(self):
        """test for a right triangle"""
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """test for a right triangle"""
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        """test for an equilateral triangle"""
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_scalene_triangles(self):
        """test for a scalene triangle"""
        self.assertEqual(classifyTriangle(7,12,15), 'Scalene', '7,12,15 should be scalene')

    def test_isosceles_triangles(self):
        """test for an isosceles triangle"""
        self.assertEqual(classifyTriangle(5,5,4), 'Isosceles', '5,5,4 should be isosceles')

    def test_invalid_triangle_a(self):
        """test for an invalid triangle"""
        self.assertEqual(classifyTriangle(300,400,500), 'InvalidInput', '300,400,500 should be invalid')

    def test_invalid_triangle_b(self):
        """test for an invalid triangle"""
        self.assertEqual(classifyTriangle(2,2,0), 'InvalidInput', '2,2,0 should be invalid')

    def test_invalid_triangle_c(self):
        """test for an invalid triangle"""
        self.assertEqual(classifyTriangle(3.4, 4.5, 7), 'InvalidInput', '3.4, 4.5, 7 should be invalid')

    def test_not_a_triangle(self):
        """test for not a triangle"""
        self.assertEqual(classifyTriangle(4,7,100), 'NotATriangle', '4,7,100 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
