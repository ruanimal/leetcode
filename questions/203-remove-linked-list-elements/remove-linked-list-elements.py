# -*- coding:utf-8 -*-


# English:
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6 Output: [1,2,3,4,5]
# Example 2:
# Input: head = [], val = 1 Output: []
# Example 3:
# Input: head = [7,7,7,7], val = 7 Output: []
# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50
#
# 中文:
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 示例 1：
# 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]
# 示例 2：
# 输入：head = [], val = 1 输出：[]
# 示例 3：
# 输入：head = [7,7,7,7], val = 7 输出：[]
# 提示：
# 列表中的节点数目在范围 [0, 104] 内
# 1 <= Node.val <= 50
# 0 <= val <= 50


#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (38.99%)
# Total Accepted:    18.8K
# Total Submissions: 47.3K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        new_head = ptr = ListNode(None)
        new_head.next = head
        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return new_head.next


