# -*- coding:utf-8 -*-


# English:
# Reverse a linked list from position m to n. Do it in one-pass.
# Note: 1 ≤ m ≤ n ≤ length of list.
# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4 Output: 1->4->3->2->5->NULL
#
# 中文:
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 示例:
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4 输出: 1->4->3->2->5->NULL


# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (41.13%)
# Total Accepted:    7.6K
# Total Submissions: 18K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
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
        tmp.append('None')
        return ' -> '.join(tmp)

    __repr__ = __str__


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        使用头指针, 先走m-1步
        将m+1到n的节点插入到m前面
        """

        if not head or not head.next:
            return head

        new_head = ptr = ListNode(None)
        new_head.next = head

        for _ in range(m-1):
            ptr = ptr.next
        edge_ptr = ptr.next
        for _ in range(n-m):
            tmp = edge_ptr.next
            edge_ptr.next = edge_ptr.next.next
            tmp.next = ptr.next
            ptr.next = tmp
        return new_head.next

if __name__ == "__main__":
    l = build_list_node(range(1,10))
    print(Solution().reverseBetween(l, 2, 9))

