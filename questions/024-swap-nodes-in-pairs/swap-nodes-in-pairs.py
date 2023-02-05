# -*- coding:utf-8 -*-

# <SUBID:305525498,UPDATE:20230205>
# English:
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Example 1:
# Input: head = [1,2,3,4] Output: [2,1,4,3]
# Example 2:
# Input: head = [] Output: []
# Example 3:
# Input: head = [1] Output: [1]
# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
#
# 中文:
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 示例 1：
# 输入：head = [1,2,3,4] 输出：[2,1,4,3]
# 示例 2：
# 输入：head = [] 输出：[]
# 示例 3：
# 输入：head = [1] 输出：[1]
# 提示：
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100




class Solution_A:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        使用一个长度为2的stack, 注意清理node的next指针,防止死循环
        """

        if not head:
            return None
        if not head.next:
            return head

        stack = []
        p = head_node = ListNode(None)
        p.next = head
        while p.next:
            while len(stack) < 2:
                if not p or not p.next:
                    break
                tmp = p.next
                stack.append(tmp)
                p.next = p.next.next
                tmp.next = None
            # print(stack)
            while stack:
                tmp = p.next
                p.next = stack.pop()
                p.next.next = tmp
                p = p.next
            # print(head_node.next)
        if stack:
            p.next = stack.pop()
        return head_node.next


class Solution_B(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        直接交换值
        """
        pointer = head
        while pointer and pointer.next is not None:
            pointer.val, pointer.next.val = pointer.next.val, pointer.val
            pointer = pointer.next.next
        return head

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            temp = p.next.next
            p.next.next = p.next.next.next
            temp.next = p.next
            p.next = temp
            p = p.next.next
        return dummy.next

