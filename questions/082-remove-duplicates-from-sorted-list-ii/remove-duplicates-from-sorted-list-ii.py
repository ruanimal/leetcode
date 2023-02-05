# -*- coding:utf-8 -*-

# <SUBID:308636246,UPDATE:20230205>
# English:
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
# Example 1:
# Input: head = [1,2,3,3,4,4,5] Output: [1,2,5]
# Example 2:
# Input: head = [1,1,1,2,3] Output: [2,3]
# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
#
# 中文:
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
# 示例 1：
# 输入：head = [1,2,3,3,4,4,5] 输出：[1,2,5]
# 示例 2：
# 输入：head = [1,1,1,2,3] 输出：[2,3]
# 提示：
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列



class SolutionA:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        new_head = ptr = ListNode(None)
        ptr.next = head
        if ptr.next.val == ptr.next.next.val:
            current_num = ptr.next.val
        else:
            current_num = None
        while ptr.next and ptr.next.next:
            if ptr.next.val == current_num:
                ptr.next = ptr.next.next
            elif ptr.next.val == ptr.next.next.val:
                current_num = ptr.next.val
            else:
                ptr = ptr.next
        if ptr.next.val == current_num:
            ptr.next = ptr.next.next
        return new_head.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = p2 = ListNode(None)

        p = head
        count = 1
        while p and p.next:
            if p.val == p.next.val:
                count += 1
            else:
                if count == 1:
                    p2.next = p
                    p2 = p2.next
                count = 1
            p = p.next
        if count == 1:
            p2.next = p
        else:
            p2.next = None
        return new_head.next

