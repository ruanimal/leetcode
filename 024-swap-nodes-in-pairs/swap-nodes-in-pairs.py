# -*- coding:utf-8 -*-


# English:
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# Example:
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# 中文:
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 示例:
# 给定 1->2->3->4, 你应该返回 2->1->4->3.


#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (56.91%)
# Total Accepted:    15.7K
# Total Submissions: 27K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        tmp = []
        node = self
        while node:
            tmp.append(repr(node.val))
            node = node.next
        return ' -> '.join(tmp)

    __repr__ = __str__


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        使用一个长度为2的stack, 注意清理node的next指针,防止死循环
        """

        if not head:
            return None
        if not head.next:
            return head

        stack = []
        p = head_node = ListNode(None)
        p.next = head
        while p.next:
            while len(stack) < 2:
                if not p or not p.next:
                    break
                tmp = p.next
                stack.append(tmp)
                p.next = p.next.next
                tmp.next = None
            # print(stack)
            while stack:
                tmp = p.next
                p.next = stack.pop()
                p.next.next = tmp
                p = p.next
            # print(head_node.next)
        if stack:
            p.next = stack.pop()
        return head_node.next
'''

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        直接交换值
        """
        pointer = head
        while pointer and pointer.next is not None:
            pointer.val, pointer.next.val = pointer.next.val, pointer.val
            pointer = pointer.next.next
        return head

if __name__ == "__main__":
    l = build_list_node([1,2,3,4])
    print(Solution().swapPairs(l))

