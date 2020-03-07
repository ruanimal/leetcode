# -*- coding:utf-8 -*-


# English:
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1] sumRange(0, 2) -> 1 sumRange(2, 5) -> -1 sumRange(0, 5) -> -3
# Note:
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
#
# 中文:
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 示例：
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange() sumRange(0, 2) -> 1 sumRange(2, 5) -> -1 sumRange(0, 5) -> -3
# 说明:
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。


#
# @lc app=leetcode.cn id=303 lang=python
#
# [303] 区域和检索 - 数组不可变
#
# https://leetcode-cn.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (50.97%)
# Total Accepted:    9.9K
# Total Submissions: 18.7K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# 示例：
#
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
# 说明:
#
#
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。
#
#
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum_result = {}
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int

        f[x]: 从0到该位置的总和
        f[x] = f[x-1] + nums[x]
        s(i, j) = f[j] - f[i-1]

        """
        nums = self.nums
        if len(nums) == 0:
            return 0
        f = self.sum_result
        if not f:
            f[-1] = 0
            f[0] = nums[0]
            for x in range(1, len(nums)):
                f[x] = f[x-1] + nums[x]
        return f[j] - f[i-1]


if __name__ == "__main__":
    s = NumArray([-2, 0, 3, -5, 2, -1])
    print(s.sumRange(0, 2))
    print(s.sumRange(2, 5))
    print(s.sumRange(0, 5))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


