# -*- coding:utf-8 -*-


# English:
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 8 -> 0 -> 7
#
# 中文:
# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 进阶:
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 示例:
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4) 输出: 7 -> 8 -> 0 -> 7


#
# @lc app=leetcode.cn id=445 lang=python
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (46.02%)
# Total Accepted:    3.1K
# Total Submissions: 6.5K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
#
#
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 进阶:
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
# 示例:
#
#
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        tmp = []
        node = self
        max_depth = 20
        while node:
            max_depth -= 1
            if max_depth < 0:
                break
            tmp.append(repr(node.val))
            node = node.next
        else:
            tmp.append('None')
        return ' -> '.join(tmp)


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        stack1 = []
        stack2 = []
        ptr_1 = l1
        ptr_2 = l2
        while ptr_1:
            stack1.append(ptr_1.val)
            ptr_1 = ptr_1.next
        while ptr_2:
            stack2.append(ptr_2.val)
            ptr_2 = ptr_2.next
        tmp = 0
        new_head = ListNode(None)
        while True:
            if not stack1 and not stack2:
                break
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            tmp, val = divmod(tmp + a + b, 10)
            node = ListNode(val)
            node.next = new_head.next
            new_head.next = node
        if tmp:
            new_head.val = tmp
            return new_head
        return new_head.next
if __name__ == "__main__":
    l = build_list_node([5])
    l2 = build_list_node([5])
    print(Solution().addTwoNumbers(l, l2))


