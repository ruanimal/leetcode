# -*- coding:utf-8 -*-


# English:
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
# Example 1:
# Input: [1,2,3] Output: [1,2,4] Explanation: The array represents the integer 123.
# Example 2:
# Input: [4,3,2,1] Output: [4,3,2,2] Explanation: The array represents the integer 4321.
#
# 中文:
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 示例 1:
# 输入: [1,2,3] 输出: [1,2,4] 解释: 输入数组表示数字 123。
# 示例 2:
# 输入: [4,3,2,1] 输出: [4,3,2,2] 解释: 输入数组表示数字 4321。


#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (37.42%)
# Total Accepted:    43.7K
# Total Submissions: 115K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#
#


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        addtion = 1
        for i in range(len(digits)-1, -1, -1):
            if addtion:
                if digits[i] >= 9:
                    digits[i] = 0
                    addtion = 1
                else:
                    digits[i] += 1
                    addtion = 0
        if addtion:
            digits.insert(0, 1)
        return digits



