# -*- coding:utf-8 -*-

# <SUBID:315717557,UPDATE:20230205>
# English:
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example 1:
# Input: l1 = [7,2,4,3], l2 = [5,6,4] Output: [7,8,0,7]
# Example 2:
# Input: l1 = [2,4,3], l2 = [5,6,4] Output: [8,0,7]
# Example 3:
# Input: l1 = [0], l2 = [0] Output: [0]
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
# Follow up: Could you solve it without reversing the input lists?
#
# 中文:
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 示例1：
# 输入：l1 = [7,2,4,3], l2 = [5,6,4] 输出：[7,8,0,7]
# 示例2：
# 输入：l1 = [2,4,3], l2 = [5,6,4] 输出：[8,0,7]
# 示例3：
# 输入：l1 = [0], l2 = [0] 输出：[0]
# 提示：
# 链表的长度范围为 [1, 100]
# 0 <= node.val <= 9
# 输入数据保证链表代表的数字无前导 0
# 进阶：如果输入链表不能翻转该如何解决？




class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        stack1 = []
        stack2 = []
        ptr_1 = l1
        ptr_2 = l2
        while ptr_1:
            stack1.append(ptr_1.val)
            ptr_1 = ptr_1.next
        while ptr_2:
            stack2.append(ptr_2.val)
            ptr_2 = ptr_2.next
        tmp = 0
        new_head = ListNode(None)
        while True:
            if not stack1 and not stack2:
                break
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            tmp, val = divmod(tmp + a + b, 10)
            node = ListNode(val)
            node.next, new_head.next = new_head.next, node
        if tmp:
            new_head.val = tmp
            return new_head
        return new_head.next

