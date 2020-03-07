# -*- coding:utf-8 -*-


# English:
# Remove all elements from a linked list of integers that have value val.
# Example:
# Input: 1->2->6->3->4->5->6, val = 6 Output: 1->2->3->4->5
#
# 中文:
# 删除链表中等于给定值 val 的所有节点。
# 示例:
# 输入: 1->2->6->3->4->5->6, val = 6 输出: 1->2->3->4->5


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


