# -*- coding:utf-8 -*-


# English:
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
# The steps of the insertion sort algorithm:
# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
# Example 1:
# Input: head = [4,2,1,3] Output: [1,2,3,4]
# Example 2:
# Input: head = [-1,5,3,4,0] Output: [-1,0,3,4,5]
# Constraints:
# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000
#
# 中文:
# 给定单个链表的头
# head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。
# 插入排序 算法的步骤:
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。
# 对链表进行插入排序。
# 示例 1：
# 输入: head = [4,2,1,3] 输出: [1,2,3,4]
# 示例 2：
# 输入: head = [-1,5,3,4,0] 输出: [-1,0,3,4,5]
# 提示：
# 列表中的节点数在 [1, 5000]范围内
# -5000 <= Node.val <= 5000


# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=147 lang=python
#
# [147] 对链表进行插入排序
#
# https://leetcode-cn.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (54.38%)
# Total Accepted:    4.9K
# Total Submissions: 8.8K
# Testcase Example:  '[4,2,1,3]'
#
# 对链表进行插入排序。
#
#
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
#
#
#
# 插入排序算法：
#
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#
#
#
#
# 示例 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
# 示例 2：
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#
#
#


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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        采用头尾指针
        """

        if not head or not head.next:
            return head

        new_head = ptr = ListNode(None)
        new_head.next = head
        while ptr.next:
            sub_ptr = new_head
            tmp = ptr.next
            while sub_ptr != ptr:
                if tmp.val < sub_ptr.next.val:
                    ptr.next = ptr.next.next
                    tmp.next = sub_ptr.next
                    sub_ptr.next = tmp
                    break
                sub_ptr = sub_ptr.next
            if sub_ptr == ptr:
                ptr = ptr.next
        return new_head.next

if __name__ == "__main__":
    l = build_list_node(range(9, 0, -1))
    print(Solution().insertionSortList(l))

