# -*- coding:utf-8 -*-

# <SUBID:19689455,UPDATE:20220325>
# English:
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:
# Input: a = "11", b = "1" Output: "100"
# Example 2:
# Input: a = "1010", b = "1011" Output: "10101"
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
# 中文:
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 输入为 非空 字符串且只包含数字 1 和 0。
# 示例 1:
# 输入: a = "11", b = "1" 输出: "100"
# 示例 2:
# 输入: a = "1010", b = "1011" 输出: "10101"
# 提示：
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。


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


