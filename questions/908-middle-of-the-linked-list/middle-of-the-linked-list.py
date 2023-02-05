# -*- coding:utf-8 -*-

# <SUBID:16863496,UPDATE:20230205>
# English:
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# Example 1:
# Input: head = [1,2,3,4,5] Output: [3,4,5] Explanation: The middle node of the list is node 3.
# Example 2:
# Input: head = [1,2,3,4,5,6] Output: [4,5,6] Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
#
# 中文:
# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
# 示例 1：
# 输入：[1,2,3,4,5] 输出：此列表中的结点 3 (序列化形式：[3,4,5]) 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。 注意，我们返回了一个 ListNode 类型的对象 ans，这样： ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
# 示例 2：
# 输入：[1,2,3,4,5,6] 输出：此列表中的结点 4 (序列化形式：[4,5,6]) 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
# 提示：
# 给定链表的结点数介于 1 和 100 之间。


#
# @lc app=leetcode.cn id=876 lang=python
#
# [876] 一手顺子
#
# https://leetcode-cn.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (57.24%)
# Total Accepted:    8.7K
# Total Submissions: 14.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
#
# 如果有两个中间结点，则返回第二个中间结点。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next =
# NULL.
#
#
# 示例 2：
#
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
#
#
#
#
# 提示：
#
#
# 给定链表的结点数介于 1 和 100 之间。
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

    def __str__(self):
        tmp = []
        node = self
        while node:
            tmp.append(repr(node.val))
            node = node.next
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
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head

        ptr = ptr_fast = head
        while ptr_fast.next and ptr_fast.next.next:
            ptr = ptr.next
            ptr_fast = ptr_fast.next.next
        if ptr_fast.next:
            ptr = ptr.next
        return ptr

if __name__ == "__main__":
    l = build_list_node([1,2,3])
    print(l)
    s = Solution().middleNode(l)
    print(s)

