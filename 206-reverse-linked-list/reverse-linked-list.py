# -*- coding:utf-8 -*-


# English:
# Reverse a singly linked list.
# Example:
# Input: 1->2->3->4->5->NULL Output: 5->4->3->2->1->NULL
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# 中文:
# 反转一个单链表。
# 示例:
# 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


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

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        new_head = p = ListNode(None)
        new_head.next = head
        p = head
        while p.next:
            tmp = p.next
            p.next = p.next.next
            tmp.next = new_head.next
            new_head.next = tmp
        return new_head.next


