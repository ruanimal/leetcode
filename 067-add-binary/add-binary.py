# -*- coding:utf-8 -*-


# English:
# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.
# Example 1:
# Input: a = "11", b = "1" Output: "100"
# Example 2:
# Input: a = "1010", b = "1011" Output: "10101"
#
# 中文:
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 输入为非空字符串且只包含数字 1 和 0。
# 示例 1:
# 输入: a = "11", b = "1" 输出: "100"
# 示例 2:
# 输入: a = "1010", b = "1011" 输出: "10101"


#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (47.14%)
# Likes:    197
# Dislikes: 0
# Total Accepted:    26.1K
# Total Submissions: 53.7K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return
        return bin(int(a, 2) + int(b, 2))[2:]


