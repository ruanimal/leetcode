# -*- coding:utf-8 -*-


# English:
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Example 1:
# Input: [3,2,1,5,6,4] and k = 2 Output: 5
# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4 Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
# 中文:
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 示例 1:
# 输入: [3,2,1,5,6,4] 和 k = 2 输出: 5
# 示例 2:
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4 输出: 4
# 说明:
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。


#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (56.10%)
# Total Accepted:    18.4K
# Total Submissions: 32.7K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明:
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#
#


class MinHeap(object):
    def __init__(self):
        self._items = [None]

    @property
    def length(self):
        return len(self._items) - 1

    @property
    def depth(self):
        return ceil(log(self.length, 2))

    def more(self, i, j):
        return self._items[i] > self._items[j]

    def exch(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def swim(self, k):
        while k > 1 and self.more(k//2, k):
            self.exch(k//2, k)
            k = k//2

    def sink(self, k):
        while 2 * k <= self.length:
            j = 2 * k
            if j < self.length and self.more(j, j+1):
                j += 1
            if not self.more(k, j):
                break
            self.exch(k, j)
            k = j

    def Insert(self, val):
        self._items.append(val)
        self.swim(self.length)

    def min(self):
        if self.length > 0:
            return self._items[1]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = MinHeap()
        for i in nums[:k]:
            heap.Insert(i)
        for i in nums[k:]:
            if i < heap.min():
                continue
            else:
                heap._items[1] = i
                heap.sink(1)
        return heap.min()

if __name__ == "__main__":
    x = [1, 4, 2, 7, 6, 3, 5]
    print(Solution().findKthLargest(x, 3))

