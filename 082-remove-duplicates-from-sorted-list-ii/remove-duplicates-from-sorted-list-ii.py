# -*- coding:utf-8 -*-


# English:
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# Return the linked list sorted as well.
# Example 1:
# Input: 1->2->3->3->4->4->5 Output: 1->2->5
# Example 2:
# Input: 1->1->1->2->3 Output: 2->3
#
# 中文:
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 示例 1:
# 输入: 1->2->3->3->4->4->5 输出: 1->2->5
# 示例 2:
# 输入: 1->1->1->2->3 输出: 2->3


#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (39.09%)
# Total Accepted:    7.6K
# Total Submissions: 19.2K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
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


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        new_head = ptr = ListNode(None)
        ptr.next = head
        if ptr.next.val == ptr.next.next.val:
            current_num = ptr.next.val
        else:
            current_num = None
        while ptr.next and ptr.next.next:
            if ptr.next.val == current_num:
                ptr.next = ptr.next.next
            elif ptr.next.val == ptr.next.next.val:
                current_num = ptr.next.val
            else:
                ptr = ptr.next
        if ptr.next.val == current_num:
            ptr.next = ptr.next.next
        return new_head.next


if __name__ == "__main__":
    l = build_list_node([1, 1, 2, 2, 2, 3, 4, 4, 6, 8,8])
    #l = build_list_node([1, 1])
    print(l)
    print(Solution().deleteDuplicates(l))


