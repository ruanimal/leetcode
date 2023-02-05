# -*- coding:utf-8 -*-

# <SUBID:15363949,UPDATE:20230205>
# English:
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Example 1:
# Input: head = [1,2,2,1] Output: true
# Example 2:
# Input: head = [1,2] Output: false
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
# Follow up: Could you do it in O(n) time and O(1) space?
#
# 中文:
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：head = [1,2,2,1] 输出：true
# 示例 2：
# 输入：head = [1,2] 输出：false
# 提示：
# 链表中节点数目在范围[1, 105] 内
# 0 <= Node.val <= 9
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (34.89%)
# Total Accepted:    18.3K
# Total Submissions: 51.3K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True

        fast_ptr = slow_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        head_b = slow_ptr.next
        slow_ptr.next = None

        new_head = ListNode(None)
        new_head.next = ptr = head_b
        print(head, head_b)
        while ptr.next:
            tmp = ptr.next
            ptr.next = ptr.next.next
            tmp.next = new_head.next
            new_head.next = tmp

        ptr_a = head
        ptr_b = new_head.next
        # print(ptr_a, ptr_b)
        while ptr_b:
            if ptr_a.val != ptr_b.val:
                return False
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next
        return True

if __name__ == "__main__":
    ll = build_list_node([1,2])
    print(Solution().isPalindrome(ll))



