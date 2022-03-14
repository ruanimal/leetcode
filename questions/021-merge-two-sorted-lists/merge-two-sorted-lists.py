# -*- coding:utf-8 -*-


# English:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4] Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = [] Output: []
# Example 3:
# Input: list1 = [], list2 = [0] Output: [0]
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
#
# 中文:
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 示例 1：
# 输入：l1 = [1,2,4], l2 = [1,3,4] 输出：[1,1,2,3,4,4]
# 示例 2：
# 输入：l1 = [], l2 = [] 输出：[]
# 示例 3：
# 输入：l1 = [], l2 = [0] 输出：[0]
# 提示：
# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列


# -*- coding:utf-8 -*-

# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (52.27%)
# Total Accepted:    51.5K
# Total Submissions: 96.9K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        while l1 and l2:
            if l1.val > l2.val:
                result.append(l2.val)
                l2 = l2.next
            else:
                result.append(l1.val)
                l1 = l1.next

        aa = l1 or l2 or 0
        while aa:
            result.append(aa.val)
            aa = aa.next
        return result
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        tmp = []
        node = self
        while node:
            tmp.append(str(node.val))
            node = node.next
        return ' -> '.join(tmp)

def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        参考 插入排序,将一个链表插入到另一个链表中
        """

        if not l1:
            return l2
        if not l2:
            return l1

        p1 = l1
        p2 = l2
        p = head = ListNode(None)

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        p.next = p1 or p2
        return head.next

if __name__ == "__main__":
    l1 = build_list_node([9])
    l2 = build_list_node([1,3,4])
    # import ipdb; ipdb.set_trace()
    print(Solution().mergeTwoLists(l1, l2))

