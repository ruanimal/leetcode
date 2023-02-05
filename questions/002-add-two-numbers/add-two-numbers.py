# -*- coding:utf-8 -*-

# <SUBID:15086259,UPDATE:20230205>
# English:
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 342 + 465 = 807.
# Example 2:
# Input: l1 = [0], l2 = [0] Output: [0]
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] Output: [8,9,9,9,0,0,0,1]
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
#
# 中文:
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例 1：
# 输入：l1 = [2,4,3], l2 = [5,6,4] 输出：[7,0,8] 解释：342 + 465 = 807.
# 示例 2：
# 输入：l1 = [0], l2 = [0] 输出：[0]
# 示例 3：
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] 输出：[8,9,9,9,0,0,0,1]
# 提示：
# 每个链表中的节点数在范围 [1, 100] 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零


# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.30%)
# Total Accepted:    98.8K
# Total Submissions: 296.6K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def print_list_node(node):
#     while node:
#         print(node.val, '-> ', end='')
#         node = node.next


# def build_list_node(nums):
#     head = node = ListNode(None)
#     for i in nums:
#         node.next = ListNode(i)
#         node = node.next
#     return head.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        按位加法实现
        """

        if not l1:
            return l2
        if not l2:
            return l1

        p1 = l1
        p2 = l2
        p3 = head = ListNode(None)
        tmp = 0

        while p1 or p2:
            if p1:
                tmp += p1.val
                p1 = p1.next
            if p2:
                tmp += p2.val
                p2 = p2.next
            tmp, val = divmod(tmp, 10)
            p3.next = ListNode(val)
            p3 = p3.next
        if tmp:
            p3.next = ListNode(tmp)
        return head.next

if __name__ == "__main__":
    # l1 = build_list_node([3])
    # l2 = build_list_node([5, 6, 6])
    # print_list_node(Solution().addTwoNumbers(l1, l2))
    pass


