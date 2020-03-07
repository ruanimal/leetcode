# -*- coding:utf-8 -*-


# English:
# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
# Example 1:
# Input: 1->2->3->4->5->NULL Output: 1->3->5->2->4->NULL
# Example 2:
# Input: 2->1->3->5->6->4->7->NULL Output: 2->3->6->7->1->5->4->NULL
# Note:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
#
# 中文:
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
# 示例 1:
# 输入: 1->2->3->4->5->NULL 输出: 1->3->5->2->4->NULL
# 示例 2:
# 输入: 2->1->3->5->6->4->7->NULL 输出: 2->3->6->7->1->5->4->NULL
# 说明:
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。


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

