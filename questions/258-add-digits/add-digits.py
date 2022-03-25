# -*- coding:utf-8 -*-

# <SUBID:15986811,UPDATE:20220325>
# English:
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# Example 1:
# Input: num = 38 Output: 2 Explanation: The process is 38 --> 3 + 8 --> 11 11 --> 1 + 1 --> 2 Since 2 has only one digit, return it.
# Example 2:
# Input: num = 0 Output: 0
# Constraints:
# 0 <= num <= 231 - 1
# Follow up: Could you do it without any loop/recursion in O(1) runtime?
#
# 中文:
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
# 示例 1:
# 输入: num = 38 输出: 2 解释: 各位相加的过程为： 38 --> 3 + 8 --> 11 11 --> 1 + 1 --> 2 由于 2 是一位数，所以返回 2。
# 示例 1:
# 输入: num = 0 输出: 0
# 提示：
# 0 <= num <= 231 - 1
# 进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？


#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#
# https://leetcode-cn.com/problems/add-digits/description/
#
# algorithms
# Easy (62.09%)
# Total Accepted:    11.8K
# Total Submissions: 18.8K
# Testcase Example:  '38'
#
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
#
# 示例:
#
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
#
#
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
#
#
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def func(num):
            result = 0
            for i in str(num):
                result += int(i)
            if num > 10:
                return func(result)
            else:
                return result
        return func(num)

