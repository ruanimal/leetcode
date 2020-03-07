# -*- coding:utf-8 -*-


# English:
# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists:
# begin to intersect at node c1.
# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3 Output: Reference of the node with value = 8 Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# Example 2:
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 Output: Reference of the node with value = 2 Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 Output: null Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values. Explanation: The two lists do not intersect, so return null.
# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
# 中文:
# 编写一个程序，找到两个单链表相交的起始节点。
# 如下面的两个链表：
# 在节点 c1 开始相交。
# 示例 1：
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3 输出：Reference of the node with value = 8 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 示例 2：
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 输出：Reference of the node with value = 2 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
# 示例 3：
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 输出：null 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。 解释：这两个链表不相交，因此返回 null。
# 注意：
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。


#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (35.50%)
# Total Accepted:    19.2K
# Total Submissions: 49.9K
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,0,1,8,4,5]\n2\n3'
#
# 编写一个程序，找到两个单链表相交的起始节点。
#
# 如下面的两个链表：
#
#
#
# 在节点 c1 开始相交。
#
#
#
# 示例 1：
#
#
#
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2,
# skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为
# [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#
#
#
#
# 示例 2：
#
#
#
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
# 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为
# [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#
#
#
#
# 示例 3：
#
#
#
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为
# 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#
#
#
#
# 注意：
#
#
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode

        遍历一次链表, 记录两个链表的长度, a, b
        用两个指针, 让长的链表先走 abs(a-b)步, 然后两个指针同时遍历, 指针相等时, 值就为链表交点

        """

        if not (headA and headB):
            return
        if headA == headB:
            return headA
        if headA.next == headB.next:
            return headA.next

        count_a = 0
        count_b = 0
        ptr_a = headA
        ptr_b = headB

        while ptr_a.next:
            count_a += 1
            ptr_a = ptr_a.next
        while ptr_b.next:
            count_b += 1
            ptr_b = ptr_b.next
        if ptr_a != ptr_b:
            return

        ptr_a = headA
        ptr_b = headB
        while count_a > count_b:
            ptr_a = ptr_a.next
            count_a -= 1
        while count_a < count_b:
            ptr_b = ptr_b.next
            count_b -= 1
        while ptr_a and ptr_b:
            if ptr_a == ptr_b:
                return ptr_a
            else:
                ptr_a = ptr_a.next
                ptr_b = ptr_b.next


