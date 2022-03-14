# -*- coding:utf-8 -*-


# English:
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5] Output: [5,4,3,2,1]
# Example 2:
# Input: head = [1,2] Output: [2,1]
# Example 3:
# Input: head = [] Output: []
# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# 中文:
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
# 示例 1：
# 输入：head = [1,2,3,4,5] 输出：[5,4,3,2,1]
# 示例 2：
# 输入：head = [1,2] 输出：[2,1]
# 示例 3：
# 输入：head = [] 输出：[]
# 提示：
# 链表中节点的数目范围是 [0, 5000]
# -5000 <= Node.val <= 5000
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？


#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (57.78%)
# Total Accepted:    42.1K
# Total Submissions: 71.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

try:
    from comm import *
except ImportError:
    LOCAL_TEST = False

class Solution_A:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        逐个取出放到dummy节点之后
        """

        if not head:
            return
        if not head.next:
            return head

        dummy = p = ListNode(None)
        dummy.next = head
        p = head
        while p.next:
            tmp = p.next
            p.next = p.next.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归版本, 把链表分成两部分
        head -> others  转变成 reverseList(others) -> head
        """
        if not head or not head.next:
            return head

        others = head.next
        head.next = None
        reversed = self.reverseList(others)
        others.next = head   # 反转之后others变成尾部
        return reversed

if LOCAL_TEST:
    n = build_list_node(range(5))
    print(Solution().reverseList(n))


