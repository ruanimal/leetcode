# -*- coding:utf-8 -*-

# <SUBID:319268165,UPDATE:20230205>
# English:
# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Implement KthLargest class:
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
# Example 1:
# Input ["KthLargest", "add", "add", "add", "add", "add"] [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]] Output [null, 4, 5, 5, 8, 8] Explanation KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]); kthLargest.add(3); // return 4 kthLargest.add(5); // return 5 kthLargest.add(10); // return 5 kthLargest.add(9); // return 8 kthLargest.add(4); // return 8
# Constraints:
# 1 <= k <= 104
# 0 <= nums.length <= 104
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you search for the kth element.
#
# 中文:
# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
# 请实现 KthLargest 类：
# KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
# int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
# 示例：
# 输入： ["KthLargest", "add", "add", "add", "add", "add"] [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]] 输出： [null, 4, 5, 5, 8, 8] 解释： KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]); kthLargest.add(3); // return 4 kthLargest.add(5); // return 5 kthLargest.add(10); // return 5 kthLargest.add(9); // return 8 kthLargest.add(4); // return 8
# 提示：
# 1 <= k <= 104
# 0 <= nums.length <= 104
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# 最多调用 add 方法 104 次
# 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素


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
    """利用最小堆"""

    def __init__(self, k, nums):
        self.max_length = k
        self.min_heap = MinHeap()
        for i in nums:
            self.add(i)

    def add(self, val):
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
