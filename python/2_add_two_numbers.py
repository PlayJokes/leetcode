#!/usr/bin/env python3
import unittest

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def print_list(node):
    while node:
        print(node.val)
        node = node.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)

        carry = 0
        p1 = l1
        p2 = l2
        result = dummy
        while p1 and p2:
            tmp = p1.val + p2.val + carry
            carry = int(tmp / 10)
            tmp = tmp % 10
            result.next = ListNode(tmp)
            result = result.next
            p1 = p1.next
            p2 = p2.next

        while p1:
            tmp = p1.val + carry
            carry = int(tmp / 10)
            tmp = tmp % 10
            result.next = ListNode(tmp)
            result = result.next
            p1 = p1.next

        while p2:
            tmp = p2.val + carry
            carry = int(tmp / 10)
            tmp = tmp % 10
            result.next = ListNode(tmp)
            result = result.next
            p2 = p2.next

        if carry:
            result.next = ListNode(carry)

        return dummy.next


class TestSolution(unittest.TestCase):
    def test_add_two_numbers(self):
        solution = Solution()
        num1 = ListNode(2)
        n2 = ListNode(4)
        n3 = ListNode(3)
        num1.next = n2
        n2.next = n3
        num2 = ListNode(5)
        n4 = ListNode(6)
        n5 = ListNode(4)
        num2.next = n4
        n4.next = n5
        answer = ListNode(7)
        n6 = ListNode(0)
        n7 = ListNode(8)
        answer.next = n6
        n6.next = n7
        result = solution.addTwoNumbers(num1, num2)
        while result and answer:
            self.assertEqual(result.val, answer.val)
            result = result.next
            answer = answer.next


if __name__ == '__main__':
    unittest.main()
