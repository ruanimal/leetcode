# -*- coding:utf-8 -*-


# English:
# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
# Return an array of the k parts.
# Example 1:
# Input: head = [1,2,3], k = 5 Output: [[1],[2],[3],[],[]] Explanation: The first element output[0] has output[0].val = 1, output[0].next = null. The last element output[4] is null, but its string representation as a ListNode is [].
# Example 2:
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3 Output: [[1,2,3,4],[5,6,7],[8,9,10]] Explanation: The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
# Constraints:
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50
#
# 中文:
# 给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。
# 每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。
# 这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。
# 返回一个由上述 k 部分组成的数组。
# 示例 1：
# 输入：head = [1,2,3], k = 5 输出：[[1],[2],[3],[],[]] 解释： 第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。 最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是 [] 。
# 示例 2：
# 输入：head = [1,2,3,4,5,6,7,8,9,10], k = 3 输出：[[1,2,3,4],[5,6,7],[8,9,10]] 解释： 输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。
# 提示：
# 链表中节点的数目在范围 [0, 1000]
# 0 <= Node.val <= 1000
# 1 <= k <= 50


#
# @lc app=leetcode.cn id=725 lang=python
#
# [725] 分隔链表
#
# https://leetcode-cn.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (47.85%)
# Total Accepted:    1.3K
# Total Submissions: 2.7K
# Testcase Example:  '[1,2,3,4]\n5'
#
# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
#
# 每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
#
# 这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
#
# 返回一个符合上述规则的链表的列表。
#
# 举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null ]
#
# 示例 1：
#
#
# 输入:
# root = [1, 2, 3], k = 5
# 输出: [[1],[2],[3],[],[]]
# 解释:
# 输入输出各部分都应该是链表，而不是数组。
# 例如, 输入的结点 root 的 val= 1, root.next.val = 2, \root.next.next.val = 3, 且
# root.next.next.next = null。
# 第一个输出 output[0] 是 output[0].val = 1, output[0].next = null。
# 最后一个元素 output[4] 为 null, 它代表了最后一个部分为空链表。
#
#
# 示例 2：
#
#
# 输入:
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# 输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# 解释:
# 输入被分成了几个连续的部分，并且每部分的长度相差不超过1.前面部分的长度大于等于后面部分的长度。
#
#
#
#
# 提示:
#
#
# root 的长度范围： [0, 1000].
# 输入的每个节点的大小范围：[0, 999].
# k 的取值范围： [1, 50].
#
#
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [None] * k

        count = 0
        ptr = root
        while ptr:
            count += 1
            ptr = ptr.next

        # 计算每部分大小
        s, y = divmod(count, k)
        print(s, y)
        count_part = [s] * k
        i = 0
        while y > 0:
            if i == k:
                i = 0
            count_part[i] += 1
            i += 1
            y -= 1

        ret = []
        ptr = root
        for pre_part in count_part:
            ret.append(ptr)
            for _ in range(pre_part-1):
                if not ptr.next:
                    break
                ptr = ptr.next
            if not ptr.next:
                break
            tmp = ptr.next
            ptr.next = None
            ptr = tmp
        ret.extend([None]*(k-len(ret)))
        return ret

if __name__ == "__main__":
    l = build_list_node(range(4))
    print(Solution().splitListToParts(l, 5))

