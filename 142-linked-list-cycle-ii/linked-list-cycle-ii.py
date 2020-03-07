# -*- coding:utf-8 -*-


# English:
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
# Note: Do not modify the linked list.
# Example 1:
# Input: head = [3,2,0,-4], pos = 1 Output: tail connects to node index 1 Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:
# Input: head = [1,2], pos = 0 Output: tail connects to node index 0 Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:
# Input: head = [1], pos = -1 Output: no cycle Explanation: There is no cycle in the linked list.
# Follow-up:
# Can you solve it without using extra space?
#
# 中文:
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 说明：不允许修改给定的链表。
# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1 输出：tail connects to node index 1 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例 2：
# 输入：head = [1,2], pos = 0 输出：tail connects to node index 0 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例 3：
# 输入：head = [1], pos = -1 输出：no cycle 解释：链表中没有环。
# 进阶：
# 你是否可以不用额外空间解决此题？


#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (33.29%)
# Total Accepted:    11.5K
# Total Submissions: 32.1K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
# 说明：不允许修改给定的链表。
#
#
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
# 示例 2：
#
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
# 示例 3：
#
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#
#
#
#
#
#
# 进阶：
# 你是否可以不用额外空间解决此题？
#
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
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

    __repr__ = __str__


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return

        p1 = p2 = head
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                break
        else:
            return
        p1 = head

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

