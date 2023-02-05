# -*- coding:utf-8 -*-

# <SUBID:305506191,UPDATE:20230205>
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



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        参考归并排序
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

