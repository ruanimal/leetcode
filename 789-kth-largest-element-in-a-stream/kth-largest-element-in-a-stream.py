# -*- coding:utf-8 -*-


# English:
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.
# Example:
# int k = 3; int[] arr = [4,5,8,2]; KthLargest kthLargest = new KthLargest(3, arr); kthLargest.add(3);   // returns 4 kthLargest.add(5);   // returns 5 kthLargest.add(10);  // returns 5 kthLargest.add(9);   // returns 8 kthLargest.add(4);   // returns 8
# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.
#
# 中文:
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。
# 示例:
# int k = 3; int[] arr = [4,5,8,2]; KthLargest kthLargest = new KthLargest(3, arr); kthLargest.add(3);   // returns 4 kthLargest.add(5);   // returns 5 kthLargest.add(10);  // returns 5 kthLargest.add(9);   // returns 8 kthLargest.add(4);   // returns 8
# 说明:
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。


#
# @lc app=leetcode.cn id=703 lang=python
#
# [703] Kth Largest Element in a Stream
#
# https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (34.43%)
# Total Accepted:    3.3K
# Total Submissions: 9K
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
#
# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用
# KthLargest.add，返回当前数据流中第K大的元素。
#
# 示例:
#
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
#
#
# 说明:
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。
#
#

class MinHeap(object):
    def __init__(self):
        self._items = [None]

    @property
    def length(self):
        return len(self._items) - 1

    def more(self, i, j):
        return self._items[i] > self._items[j]

    def exch(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def swim(self, k):
        while k > 1 and self.more(k//2, k):
            self.exch(k//2, k)
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.length:
            j = 2 * k
            # 左右两个子节点, 和大于且最接近的节点交换
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
        if len(self._items) > 1:
            return self._items[1]

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.max_length = k
        self.min_heap = MinHeap()
        for i in nums:
            self.add(i)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heap = self.min_heap
        if heap.length < self.max_length:
            heap.Insert(val)
            if heap.length == self.max_length:
                return heap.min()
            else:
                return

        if val < heap.min():
            return heap.min()
        heap._items[1] = val
        heap.sink(1)
        return heap.min()


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == "__main__":
    obj = KthLargest(3,[4,5,8,2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))

