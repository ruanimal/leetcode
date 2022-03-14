# -*- coding:utf-8 -*-


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
# n == number of nodes in the linked list
# 0 <= n <= 104
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


#
# @lc app=leetcode.cn id=328 lang=python
#
# [328] 奇偶链表
#
# https://leetcode-cn.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (53.69%)
# Total Accepted:    7.7K
# Total Submissions: 14K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
#
#
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
#
# 说明:
#
#
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        tmp = []
        node = self
        max_depth = 20
        while node:
            max_depth -= 1
            if max_depth < 0:
                break
            tmp.append(repr(node.val))
            node = node.next
        else:
            tmp.append('None')
        return ' -> '.join(tmp)


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
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

if __name__ == "__main__":
    l = build_list_node(range(1, 10))
    print(Solution().oddEvenList(l))

