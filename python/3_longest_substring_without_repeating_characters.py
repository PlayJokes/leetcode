#!/usr/bin/env python3
import unittest

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        longest = 0
        prev_idx = -1

        for idx, ch in enumerate(s):
            if ch in pos:
                prev_idx = max(pos[ch], prev_idx)
            longest = max(idx - prev_idx, longest)
            pos[ch] = idx

        return longest


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLongestSubstring("ggububgvfk"), 6)
        self.assertEqual(solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(solution.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("dvdf"), 3)
        self.assertEqual(solution.lengthOfLongestSubstring("bziuwnklhqzrxnb"), 11)


if __name__ == '__main__':
    unittest.main()
