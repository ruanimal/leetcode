# -*- coding:utf-8 -*-


# English:
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
# Example:
# Input: [   1->4->5,   1->3->4,   2->6 ] Output: 1->1->2->3->4->4->5->6
#
# 中文:
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 示例:
# 输入: [   1->4->5,   1->3->4,   2->6 ] 输出: 1->1->2->3->4->4->5->6


#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (43.30%)
# Total Accepted:    16.7K
# Total Submissions: 37.8K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
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


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        采用分治法
        """

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            l1 = self.mergeKLists(lists[:len(lists)//2])
            l2 = self.mergeKLists(lists[len(lists)//2:])
            return self.mergeTwoLists(l1, l2)

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
    pass

