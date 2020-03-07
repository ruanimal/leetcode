# -*- coding:utf-8 -*-


# English:
# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
# Example 1:
#
# Input: [1,4,3,2] Output: 4 Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
#
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
#
# 中文:
# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
# 示例 1:
# 输入: [1,4,3,2] 输出: 4 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
# 提示:
# n 是正整数,范围在 [1, 10000].
# 数组中的元素范围在 [-10000, 10000].


#
# @lc app=leetcode.cn id=561 lang=python
#
# [561] 数组拆分 I
#
# https://leetcode-cn.com/problems/array-partition-i/description/
#
# algorithms
# Easy (62.97%)
# Total Accepted:    11.8K
# Total Submissions: 18.3K
# Testcase Example:  '[1,4,3,2]'
#
# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n
# 的 min(ai, bi) 总和最大。
#
# 示例 1:
#
#
# 输入: [1,4,3,2]
#
# 输出: 4
# 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
#
#
# 提示:
#
#
# n 是正整数,范围在 [1, 10000].
# 数组中的元素范围在 [-10000, 10000].
#
#
#
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])

if __name__ == "__main__":
    pass

