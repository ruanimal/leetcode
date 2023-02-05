# -*- coding:utf-8 -*-

# <SUBID:308542428,UPDATE:20230205>
# English:
# Given the head of a linked list, rotate the list to the right by k places.
# Example 1:
# Input: head = [1,2,3,4,5], k = 2 Output: [4,5,1,2,3]
# Example 2:
# Input: head = [0,1,2], k = 4 Output: [2,0,1]
# Constraints:
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109
#
# 中文:
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# 示例 1：
# 输入：head = [1,2,3,4,5], k = 2 输出：[4,5,1,2,3]
# 示例 2：
# 输入：head = [0,1,2], k = 4 输出：[2,0,1]
# 提示：
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109



class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if not head.next or k==0:
            return head

        new_head = p1 = p2 = ListNode(None)
        new_head.next = head
        count = k
        while count > 0:
            if not p1.next:   # k 大于链表长度, 则取余数
                count = k % (k - count)
                if count == 0:
                    return head
                p1 = new_head
            p1 = p1.next
            count -= 1

        # 将后半段放到前半段的头部
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        tmp = p2.next
        p2.next = None
        p1.next = new_head.next
        new_head.next = tmp
        return new_head.next

