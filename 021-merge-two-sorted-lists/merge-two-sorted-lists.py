# -*- coding:utf-8 -*-


# English:
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Example:
# Input: 1->2->4, 1->3->4 Output: 1->1->2->3->4->4
#
# 中文:
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 示例：
# 输入：1->2->4, 1->3->4 输出：1->1->2->3->4->4


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


def print_list_node(node):
    while node:
        print(node.val, '-> ', end='')
        node = node.next


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
        p1 = p1 or p2 or None

        while p1:
            p.next = p1
            p = p.next
            p1 = p1.next
        return head.next

if __name__ == "__main__":
    l1 = build_list_node([9])
    l2 = build_list_node([1,3,4])
    # import ipdb; ipdb.set_trace()
    print(Solution().mergeTwoLists(l1, l2))

