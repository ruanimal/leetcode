# -*- coding:utf-8 -*-


# English:
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]] Output: [1,1,2,3,4,4,5,6] Explanation: The linked-lists are: [ 1->4->5, 1->3->4, 2->6 ] merging them into one sorted list: 1->1->2->3->4->4->5->6
# Example 2:
# Input: lists = [] Output: []
# Example 3:
# Input: lists = [[]] Output: []
# Constraints:
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.
#
# 中文:
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 示例 1：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]] 输出：[1,1,2,3,4,4,5,6] 解释：链表数组如下： [ 1->4->5, 1->3->4, 2->6 ] 将它们合并到一个有序链表中得到。 1->1->2->3->4->4->5->6
# 示例 2：
# 输入：lists = [] 输出：[]
# 示例 3：
# 输入：lists = [[]] 输出：[]
# 提示：
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4


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
        l1 = self.mergeKLists(lists[:len(lists)//2])
        l2 = self.mergeKLists(lists[len(lists)//2:])
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        参考 插入排序,将一个链表插入到另一个链表中
        """

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
    pass

