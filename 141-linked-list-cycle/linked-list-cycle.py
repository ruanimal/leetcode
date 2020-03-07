# -*- coding:utf-8 -*-


# English:
# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
# Example 1:
# Input: head = [3,2,0,-4], pos = 1 Output: true Explanation: There is a cycle in the linked list, where tail connects to the second node.
# Example 2:
# Input: head = [1,2], pos = 0 Output: true Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Example 3:
# Input: head = [1], pos = -1 Output: false Explanation: There is no cycle in the linked list.
# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?
#
# 中文:
# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1 输出：true 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例 2：
# 输入：head = [1,2], pos = 0 输出：true 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例 3：
# 输入：head = [1], pos = -1 输出：false 解释：链表中没有环。
# 进阶：
# 你能用 O(1)（即，常量）内存解决此问题吗？


# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#
# https://leetcode-cn.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (34.19%)
# Total Accepted:    30.2K
# Total Submissions: 83.1K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
# 示例 2：
#
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
# 示例 3：
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
# 进阶：
#
# 你能用 O(1)（即，常量）内存解决此问题吗？
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

# 求出环的位置的版本
# class Solution(object):
#     def hasCycle(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         if not head or not head.next:
#             return -1

#         pos = -1
#         fast_ptr = slow_ptr = ptr = head
#         # import ipdb; ipdb.set_trace()
#         while True:
#             if not fast_ptr.next or not fast_ptr.next.next:
#                 return -1
#             slow_ptr = slow_ptr.next
#             fast_ptr = fast_ptr.next.next
#             if fast_ptr == slow_ptr:
#                 pos = 0
#                 break

#         if pos == 0:
#             while ptr != slow_ptr:
#                 ptr = ptr.next
#                 slow_ptr = slow_ptr.next
#                 pos += 1
#         return pos

# if __name__ == "__main__":
#     tmp = [ListNode(i) for i in [3, 2, 0, -4]]
#     l = tmp[0]
#     for i in tmp[1:]:
#         l.next = i
#         l = l.next
#     tmp[3].next = tmp[0]
#     print(tmp[0])
#     print(Solution().hasCycle(tmp[0]))


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow_ptr = head
        fast_ptr = head

        while 1:
            if not fast_ptr.next or not fast_ptr.next.next:
                return False
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True

