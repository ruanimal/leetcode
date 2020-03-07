# -*- coding:utf-8 -*-


# English:
# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
# Given linked list: 1->2->3->4->5, and n = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Follow up:
# Could you do this in one pass?
#
# 中文:
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2. 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
# 给定的 n 保证是有效的。
# 进阶：
# 你能尝试使用一趟扫描实现吗？


# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (32.60%)
# Total Accepted:    33.9K
# Total Submissions: 103.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        快慢指针

        """
        if n <= 0:
            raise ValueError('wrong n')

        pre_head = ListNode(None)
        pre_head.next = head
        p1 = p2 = pre_head

        while p2.next:
            if n > 0:
                p2 = p2.next
                n -= 1
            else:
                p2 = p2.next
                p1 = p1.next

        if n > 0:
            raise ValueError('n big than listNode length')
        p1.next = p1.next.next
        return pre_head.next


if __name__ == "__main__":
    # n = build_list_node(range(10))
    # print_list_node(n)
    # head = build_list_node([1, 2, 3, 4, 5])
    # print_list_node(Solution().removeNthFromEnd(head, 2))
    pass

