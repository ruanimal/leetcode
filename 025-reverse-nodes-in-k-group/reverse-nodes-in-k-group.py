# -*- coding:utf-8 -*-


# English:
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# Example:
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5
# Note:
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
#
# 中文:
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 示例：
# 给你这个链表：1->2->3->4->5
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 说明：
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


# -*- coding:utf-8 -*-#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] k个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (49.82%)
# Total Accepted:    7.9K
# Total Submissions: 15.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
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
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        """k个一组翻转链表"""
        # 递归解法
        def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
            if head is None:
                return
            if head.next is None:
                newhead = head
            else:
                newhead = recurse(head.next, newhead)
                head.next.next = head
                head.next = None
            # print(newhead)
            return newhead

        if head is None:
            return
        if head.next is None:
            return head

        length = 0  # 链表长度

        # p 段前指针
        # sub_head 段头部指针,
        # sub_tail 段尾部指针
        new_head = p = sub_head = sub_tail = ListNode(None)
        sub_head.next = head

        # 找到第一段的位置
        sub_head = sub_head.next
        for _ in range(k):
            if not sub_tail.next:
                return head
            sub_tail = sub_tail.next
        # 移动这个段到合适的位置, 合适则反转段
        while sub_tail:
            if length % k == 0:
                # 断开段末尾
                tmp = sub_tail.next
                sub_tail.next = None
                # 反转
                recurse(sub_head, None)
                # 将翻转后的段接上
                p.next = sub_tail
                sub_head.next = tmp
                # 调整反转的指针
                sub_head, sub_tail = sub_tail, sub_head
            sub_head = sub_head.next
            sub_tail = sub_tail.next
            p = p.next
            length += 1
        return new_head.next

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        思路：每次反转k个链表，如果不满k个则说明到达末尾，对这一次重新反转使之保持原有顺序
        """
        if not head or k <= 1:
            return head

        new_head = ListNode(None)
        new_head.next = head
        sub_head = new_head.next   # 当前段头部
        p = new_head   # 当前段前一个位置
        while sub_head:
            try:
                # 反转当前段: 将段头部之后的节点逐个插入到段前的位置
                for _ in range(k-1):
                    tmp = sub_head.next  # 保持要移动的节点
                    sub_head.next = sub_head.next.next  # 删除改节点
                    tmp.next = p.next  # 接上节点尾部
                    p.next = tmp  # 接上节点头部
            except AttributeError:
                # 最后不满k个, 此时最后一段已经反转
                sub_head = p.next  # 将段头指向反转后的头部
                while sub_head.next:
                    tmp = sub_head.next
                    sub_head.next = sub_head.next.next
                    tmp.next = p.next
                    p.next = tmp
                break
            p = sub_head
            sub_head = sub_head.next
        return new_head.next

if __name__ == "__main__":
    l = build_list_node(range(11))
    print(Solution().reverseKGroup(l, 3))


