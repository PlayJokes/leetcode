#!/usr/bin/env python3
import unittest

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = {}
        for idx, value in enumerate(nums):
            pos[value] = idx

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in pos and idx != pos[diff]:
                return [idx, pos[diff]]


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([1, 3, 5, 7, 9], 14), [2, 4])
        self.assertEqual(solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])


if __name__ == '__main__':
    unittest.main()
