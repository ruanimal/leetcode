# -*- coding:utf-8 -*-

# <SUBID:305832356,UPDATE:20230205>
# English:
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# Example 1:
# Input: head = [1,2,3,4,5], k = 2 Output: [2,1,4,3,5]
# Example 2:
# Input: head = [1,2,3,4,5], k = 3 Output: [3,2,1,4,5]
# Constraints:
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# Follow-up: Can you solve the problem in O(1) extra memory space?
#
# 中文:
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2 输出：[2,1,4,3,5]
# 示例 2：
# 输入：head = [1,2,3,4,5], k = 3 输出：[3,2,1,4,5]
# 提示：
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？




class Solution_A:
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

class Solution:
    def reverseN(self, head, n):
        if n == 1:
            return head

        others = head.next
        head.next = None
        new_head = self.reverseN(others, n-1)
        head.next = others.next
        others.next = head
        return new_head

    def reverseKGroup(self, head, k):
        """
        递归的方法

        求出前k个的尾部, 反转
        递归这个过程
        """

        if not head or k <= 1:
            return head

        # 求出前k个的尾部
        n = k
        p = head
        while n > 0 and p:
            n -= 1
            p = p.next
        if n > 0:   # 不足k
            return head

        new_head = self.reverseN(head, k)
        if p:
            head.next = self.reverseKGroup(p, k)  # tail = head
        return new_head

