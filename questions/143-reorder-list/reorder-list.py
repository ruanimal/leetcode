# -*- coding:utf-8 -*-

# <SUBID:15350711,UPDATE:20220325>
# English:
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Example 1:
# Input: head = [1,2,3,4] Output: [1,4,2,3]
# Example 2:
# Input: head = [1,2,3,4,5] Output: [1,5,2,4,3]
# Constraints:
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000
#
# 中文:
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 示例 1：
# 输入：head = [1,2,3,4] 输出：[1,4,2,3]
# 示例 2：
# 输入：head = [1,2,3,4,5] 输出：[1,5,2,4,3]
# 提示：
# 链表的长度范围为 [1, 5 * 104]
# 1 <= node.val <= 1000


#
# @lc app=leetcode.cn id=143 lang=python
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (47.47%)
# Total Accepted:    3.7K
# Total Submissions: 7.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
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

    __repr__ = __str__


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.

        使用两个边界指针, 找到链表中点
        """

        if not head or not head.next:
            return -1

        fast_ptr = slow_ptr = head
        # 求链表中部
        while (fast_ptr.next and fast_ptr.next.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # 翻转
        ptr = slow_ptr.next
        slow_ptr.next = None
        stack = []
        while ptr:
            stack.append(ptr)
            ptr = ptr.next

        # 插入
        ptr = head
        while stack:
            tmp = stack.pop()
            tmp.next = ptr.next
            ptr.next = tmp
            ptr = tmp.next
        return head
if __name__ == "__main__":
    l = build_list_node(range(1,6))
    print(Solution().reorderList(l))


