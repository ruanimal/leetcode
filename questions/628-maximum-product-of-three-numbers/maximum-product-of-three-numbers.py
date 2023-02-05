# -*- coding:utf-8 -*-

# <SUBID:318956935,UPDATE:20230205>
# English:
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
# Example 1:
# Input: nums = [1,2,3] Output: 6
# Example 2:
# Input: nums = [1,2,3,4] Output: 24
# Example 3:
# Input: nums = [-1,-2,-3] Output: -6
# Constraints:
# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000
#
# 中文:
# 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 示例 1：
# 输入：nums = [1,2,3] 输出：6
# 示例 2：
# 输入：nums = [1,2,3,4] 输出：24
# 示例 3：
# 输入：nums = [-1,-2,-3] 输出：-6
# 提示：
# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000


class Solution(object):
    def maximumProduct(self, nums: List[int]) -> int:
        """排序

        如果数组中有正数有负数，则最大乘积既可能是三个最大正数的乘积，也可能是两个最小负数（即绝对值最大）与最大正数的乘积。
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

