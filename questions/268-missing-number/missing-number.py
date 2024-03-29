# -*- coding:utf-8 -*-

# <SUBID:313812649,UPDATE:20230205>
# English:
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Example 1:
# Input: nums = [3,0,1] Output: 2 Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:
# Input: nums = [0,1] Output: 2 Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8 Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.
# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
#
# 中文:
# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
# 示例 1：
# 输入：nums = [3,0,1] 输出：2 解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
# 示例 2：
# 输入：nums = [0,1] 输出：2 解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
# 示例 3：
# 输入：nums = [9,6,4,2,3,5,7,0,1] 输出：8 解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
# 示例 4：
# 输入：nums = [0] 输出：1 解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
# 提示：
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# nums 中的所有数字都 独一无二
# 进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?


#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#
# https://leetcode-cn.com/problems/missing-number/description/
#
# algorithms
# Easy (47.62%)
# Total Accepted:    16.4K
# Total Submissions: 33.4K
# Testcase Example:  '[3,0,1]'
#
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#
# 示例 1:
#
# 输入: [3,0,1]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
#
#
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
#
#
class Solution(object):
    def missingNumber(self, nums: list) -> int:
        """
        求和法
        """
        length = len(nums)
        tmp = (length * (length+1))/2
        return int(tmp - sum(nums))


