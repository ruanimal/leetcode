# -*- coding:utf-8 -*-

# <SUBID:314399727,UPDATE:20230205>
# English:
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
# Example 1:
# Input ["NumArray", "sumRange", "sumRange", "sumRange"] [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]] Output [null, 1, -1, -3] Explanation NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]); numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1 numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1 numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
# Constraints:
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.
#
# 中文:
# 给定一个整数数组  nums，处理以下类型的多个查询:
# 计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right
# 实现 NumArray 类：
# NumArray(int[] nums) 使用数组 nums 初始化对象
# int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )
# 示例 1：
# 输入： ["NumArray", "sumRange", "sumRange", "sumRange"] [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]] 输出： [null, 1, -1, -3] 解释： NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]); numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3) numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
# 提示：
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= i <= j < nums.length
# 最多调用 104 次 sumRange 方法


#
# @lc app=leetcode.cn id=303 lang=python3
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

    def __init__(self, nums: list):
        self.sum_result = {}
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        """动态规划
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


