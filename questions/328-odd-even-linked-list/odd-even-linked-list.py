# -*- coding:utf-8 -*-

# <SUBID:314405191,UPDATE:20230205>
# English:
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
# Example 1:
# Input: head = [1,2,3,4,5] Output: [1,3,5,2,4]
# Example 2:
# Input: head = [2,1,3,5,6,4,7] Output: [2,3,6,7,1,5,4]
# Constraints:
# The number of nodes in the linked list is in the range [0, 104].
# -106 <= Node.val <= 106
#
# 中文:
# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
# 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
# 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
# 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
# 示例 1:
# 输入: head = [1,2,3,4,5] 输出: [1,3,5,2,4]
# 示例 2:
# 输入: head = [2,1,3,5,6,4,7] 输出: [2,3,6,7,1,5,4]
# 提示:
# n ==  链表中的节点数
# 0 <= n <= 104
# -106 <= Node.val <= 106




class Solution(object):
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        使用dummyhead, 将偶数节点逐个取下, 练到新偶数链表末尾

        将新偶数链表连到原链表末尾
        """
        if not head or not head.next or not head.next.next:
            return head
        new_head = ListNode(None)
        ptr = head
        ptr2 = new_head
        while ptr and ptr.next:
            tmp = ptr.next
            ptr.next = ptr.next.next
            ptr2.next = tmp
            if ptr.next:
                ptr = ptr.next
            ptr2 = ptr2.next
        ptr2.next = None
        ptr.next = new_head.next
        return head

