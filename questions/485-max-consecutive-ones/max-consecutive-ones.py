# -*- coding:utf-8 -*-

# <SUBID:15988513,UPDATE:20220325>
# English:
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1] Output: 3 Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1] Output: 2
# Constraints:
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
#
# 中文:
# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
# 示例 1：
# 输入：nums = [1,1,0,1,1,1] 输出：3 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
# 示例 2:
# 输入：nums = [1,0,1,1,0,1] 输出：2
# 提示：
# 1 <= nums.length <= 105
# nums[i] 不是 0 就是 1.


#
# @lc app=leetcode.cn id=485 lang=python
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (51.82%)
# Total Accepted:    10K
# Total Submissions: 19.1K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#
#
# 注意：
#
#
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
#
#
#
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp += 1
            else:
                if tmp > max_len:
                    max_len = tmp
                tmp = 0
        if tmp > max_len:
            max_len = tmp
        return max_len


