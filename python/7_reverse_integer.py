#!/usr/bin/env python3
import unittest
import string

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1

        if x < 0:
            flag = -1
            x = -x

        result = 0
        while x:
            result = result * 10 + x % 10
            x = int(x / 10)
        return flag * result * (result < 2**31)


class TestSolution(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(-123), -321)


if __name__ == '__main__':
    unittest.main()
