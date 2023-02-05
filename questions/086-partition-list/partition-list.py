# -*- coding:utf-8 -*-

# <SUBID:308662144,UPDATE:20230205>
# English:
# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3 Output: [1,2,2,4,3,5]
# Example 2:
# Input: head = [2,1], x = 2 Output: [1,2]
# Constraints:
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
#
# 中文:
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
# 你应当 保留 两个分区中每个节点的初始相对位置。
# 示例 1：
# 输入：head = [1,4,3,2,5,2], x = 3 输出：[1,2,2,4,3,5]
# 示例 2：
# 输入：head = [2,1], x = 2 输出：[1,2]
# 提示：
# 链表中节点的数目在范围 [0, 200] 内
# -100 <= Node.val <= 100
# -200 <= x <= 200




class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        用一个链表 gt_head 存储大于 x 的值,
        遍历 head 将 >=x 的节点都放到 gt_head 中
        再将gt_head练到head末尾
        """
        if not head:
            return
        if not head.next:
            return head

        new_head = ptr = ListNode(None)
        ptr.next = head

        gt_head = gt_ptr = ListNode(None)

        while ptr.next:
            if ptr.next.val >= x:
                tmp = ptr.next
                ptr.next = ptr.next.next
                gt_ptr.next = tmp
                gt_ptr = gt_ptr.next
            else:
                ptr = ptr.next
        if gt_head.next:
            ptr.next = gt_head.next
            gt_ptr.next = None
        return new_head.next

