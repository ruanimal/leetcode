# -*- coding:utf-8 -*-


# English:
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
# Example 1:
# Input: nums = [1,4,3,2] Output: 4 Explanation: All possible pairings (ignoring the ordering of elements) are: 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4 So the maximum possible sum is 4.
# Example 2:
# Input: nums = [6,2,6,5,1,2] Output: 9 Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
# Constraints:
# 1 <= n <= 104
# nums.length == 2 * n
# -104 <= nums[i] <= 104
#
# 中文:
# 给定长度为 2n 的整数数组 nums ，你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从 1 到 n 的 min(ai, bi) 总和最大。
# 返回该 最大总和 。
# 示例 1：
# 输入：nums = [1,4,3,2] 输出：4 解释：所有可能的分法（忽略元素顺序）为： 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4 所以最大总和为 4
# 示例 2：
# 输入：nums = [6,2,6,5,1,2] 输出：9 解释：最优的分法为 (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9
# 提示：
# 1 <= n <= 104
# nums.length == 2 * n
# -104 <= nums[i] <= 104


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

