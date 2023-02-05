# -*- coding:utf-8 -*-

# <SUBID:15360308,UPDATE:20230205>
# English:
# Given the head of a linked list, return the list after sorting it in ascending order.
# Example 1:
# Input: head = [4,2,1,3] Output: [1,2,3,4]
# Example 2:
# Input: head = [-1,5,3,4,0] Output: [-1,0,3,4,5]
# Example 3:
# Input: head = [] Output: []
# Constraints:
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
#
# 中文:
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
# 示例 1：
# 输入：head = [4,2,1,3] 输出：[1,2,3,4]
# 示例 2：
# 输入：head = [-1,5,3,4,0] 输出：[-1,0,3,4,5]
# 示例 3：
# 输入：head = [] 输出：[]
# 提示：
# 链表中节点的数目在范围 [0, 5 * 104] 内
# -105 <= Node.val <= 105
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (57.63%)
# Total Accepted:    8.9K
# Total Submissions: 15.2K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
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
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge(left, right):
            p1 = left
            p2 = right
            p = head = ListNode(None)
            while p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            p1 = p1 or p2 or None
            while p1:
                p.next = p1
                p = p.next
                p1 = p1.next
            return head.next

        if not head or not head.next:
            return head

        fast_ptr = slow_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        left, right = head, slow_ptr.next
        slow_ptr.next = None
        return merge(self.sortList(left), self.sortList(right))

if __name__ == "__main__":
    l = build_list_node(range(9, -1, -1))
    print(Solution().sortList(l))


