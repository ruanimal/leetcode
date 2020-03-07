# -*- coding:utf-8 -*-


# English:
# Given a binary array, find the maximum number of consecutive 1s in this array.
# Example 1:
#
# Input: [1,1,0,1,1,1] Output: 3 Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
# 中文:
# 给定一个二进制数组， 计算其中最大连续1的个数。
# 示例 1:
# 输入: [1,1,0,1,1,1] 输出: 3 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 注意：
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。


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


