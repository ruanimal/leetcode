# -*- coding:utf-8 -*-

# <SUBID:282537510,UPDATE:20220325>
# English:
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.
# Note that the linked lists must retain their original structure after the function returns.
# Custom Judge:
# The inputs to the judge are given as follows (your program is not given these inputs):
# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.
# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3 Output: Intersected at '8' Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# Example 2:
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 Output: Intersected at '2' Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 Output: No intersection Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values. Explanation: The two lists do not intersect, so return null.
# Constraints:
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
#
# 中文:
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
# 图示两个链表在节点 c1 开始相交：
# 题目数据 保证 整个链式结构中不存在环。
# 注意，函数返回结果后，链表必须 保持其原始结构 。
# 自定义评测：
# 评测系统 的输入如下（你设计的程序 不适用 此输入）：
# intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
# listA - 第一个链表
# listB - 第二个链表
# skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
# skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
# 评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。
# 示例 1：
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3 输出：Intersected at '8' 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 示例 2：
# 输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1 输出：Intersected at '2' 解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。 从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。 在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
# 示例 3：
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2 输出：null 解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。 这两个链表不相交，因此返回 null 。
# 提示：
# listA 中节点数目为 m
# listB 中节点数目为 n
# 1 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA <= m
# 0 <= skipB <= n
# 如果 listA 和 listB 没有交点，intersectVal 为 0
# 如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]
# 进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？


#
# @lc app=leetcode.cn id=160 lang=python3
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

try:
    from comm import *
except ImportError:
    LOCAL_TEST = False

class Solution_A(object):
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

        count1 = 0
        count2 = 0
        p1 = headA
        p2 = headB

        while p1.next:
            count1 += 1
            p1 = p1.next
        while p2.next:
            count2 += 1
            p2 = p2.next
        if p1 != p2:
            return

        p1 = headA
        p2 = headB
        while count1 > count2:
            p1 = p1.next
            count1 -= 1
        while count1 < count2:
            p2 = p2.next
            count2 -= 1
        while p1 and p2:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next

class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        将A链的末尾链上B链的头部, 转化为求链表环的问题
        """
        if not headA or not headB:
            return

        p = headA
        while p.next:
            p = p.next
        p.next = headB   # 链表相连
        slow = fast = headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:   # 无环
            p.next = None  # 还原相连的链表
            return
        slow = headA
        while slow != fast:
            slow = slow.next
            fast = fast.next
        p.next = None  # 还原相连的链表
        return slow

