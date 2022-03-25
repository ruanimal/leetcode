# -*- coding:utf-8 -*-

# <SUBID:15364277,UPDATE:20220325>
# English:
# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.
# Example 1:
# Input: head = [4,5,1,9], node = 5 Output: [4,1,9] Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# Example 2:
# Input: head = [4,5,1,9], node = 1 Output: [4,5,9] Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
# Constraints:
# The number of the nodes in the given list is in the range [2, 1000].
# -1000 <= Node.val <= 1000
# The value of each node in the list is unique.
# The node to be deleted is in the list and is not a tail node
#
# 中文:
# 请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。
# 题目数据保证需要删除的节点 不是末尾节点 。
# 示例 1：
# 输入：head = [4,5,1,9], node = 5 输出：[4,1,9] 解释：指定链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9
# 示例 2：
# 输入：head = [4,5,1,9], node = 1 输出：[4,5,9] 解释：指定链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9
# 提示：
# 链表中节点的数目范围是 [2, 1000]
# -1000 <= Node.val <= 1000
# 链表中每个节点的值都是 唯一 的
# 需要删除的节点 node 是 链表中的节点 ，且 不是末尾节点


#
# @lc app=leetcode.cn id=237 lang=python
#
# [237] 删除链表中的节点
#
# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/description/
#
# algorithms
# Easy (67.88%)
# Total Accepted:    23.8K
# Total Submissions: 33.9K
# Testcase Example:  '[4,5,1,9]\n5'
#
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
#
# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:
#
#
#
#
#
# 示例 1:
#
# 输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#
#
# 示例 2:
#
# 输入: head = [4,5,1,9], node = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#
#
#
#
# 说明:
#
#
# 链表至少包含两个节点。
# 链表中所有节点的值都是唯一的。
# 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
# 不要从你的函数中返回任何结果。
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
       删除当前节点
        """
        if not node:
            return
        node.val = node.next.val
        node.next = node.next.next



