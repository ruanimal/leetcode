# -*- coding:utf-8 -*-

# <SUBID:308694743,UPDATE:20230205>
# English:
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4 Output: [1,4,3,2,5]
# Example 2:
# Input: head = [5], left = 1, right = 1 Output: [5]
# Constraints:
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# Follow up: Could you do it in one pass?
#
# 中文:
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
# 示例 1：
# 输入：head = [1,2,3,4,5], left = 2, right = 4 输出：[1,4,3,2,5]
# 示例 2：
# 输入：head = [5], left = 1, right = 1 输出：[5]
# 提示：
# 链表中节点数目为 n
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
# 进阶： 你可以使用一趟扫描完成反转吗？




class Solution_A:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        使用头指针, 先走m-1步
        将m+1到n的节点插入到m前面
        """

        if not head or not head.next:
            return head

        dummy = ptr = ListNode(None)
        dummy.next = head

        for _ in range(m-1):
            ptr = ptr.next
        edge_ptr = ptr.next
        for _ in range(n-m):
            tmp = edge_ptr.next
            edge_ptr.next = edge_ptr.next.next
            tmp.next = ptr.next
            ptr.next = tmp
        return dummy.next

class Solution:
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        """
        递归法, 实现简单, 稍微有理解难度
        """

        if n <= 1 or not head.next:
            self.successor = head.next
            return head
        others = head.next
        head.next = None
        new_head = self.reverseN(others, n-1)
        others.next = head
        head.next = self.successor
        return new_head

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

