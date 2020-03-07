# -*- coding:utf-8 -*-


# English:
# Given a linked list, rotate the list to the right by k places, where k is non-negative.
# Example 1:
# Input: 1->2->3->4->5->NULL, k = 2 Output: 4->5->1->2->3->NULL Explanation: rotate 1 steps to the right: 5->1->2->3->4->NULL rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
# Input: 0->1->2->NULL, k = 4 Output: 2->0->1->NULL Explanation: rotate 1 steps to the right: 2->0->1->NULL rotate 2 steps to the right: 1->2->0->NULL rotate 3 steps to the right: 0->1->2->NULL rotate 4 steps to the right: 2->0->1->NULL
#
# 中文:
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: 1->2->3->4->5->NULL, k = 2 输出: 4->5->1->2->3->NULL 解释: 向右旋转 1 步: 5->1->2->3->4->NULL 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
# 输入: 0->1->2->NULL, k = 4 输出: 2->0->1->NULL 解释: 向右旋转 1 步: 2->0->1->NULL 向右旋转 2 步: 1->2->0->NULL 向右旋转 3 步: 0->1->2->NULL 向右旋转 4 步: 2->0->1->NULL


#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (36.97%)
# Total Accepted:    10.9K
# Total Submissions: 28.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
#
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        tmp = []
        node = self
        while node:
            tmp.append(repr(node.val))
            node = node.next
        tmp.append('Null')
        return ' -> '.join(tmp)

    __repr__ = __str__


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next

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

        while p1.next:
            p1 = p1.next
            p2 = p2.next
        tmp = p2.next
        p2.next = None
        p1.next = new_head.next
        new_head.next = tmp
        return new_head.next

if __name__ == "__main__":
    l = build_list_node(range(5))
    print(Solution().rotateRight(l, 10))

