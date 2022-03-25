# -*- coding:utf-8 -*-

# <SUBID:16375617,UPDATE:20220325>
# English:
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
# Example 1:
# Input: n = 1 Output: true Explanation: 20 = 1
# Example 2:
# Input: n = 16 Output: true Explanation: 24 = 16
# Example 3:
# Input: n = 3 Output: false
# Constraints:
# -231 <= n <= 231 - 1
# Follow up: Could you solve it without loops/recursion?
#
# 中文:
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
# 示例 1：
# 输入：n = 1 输出：true 解释：20 = 1
# 示例 2：
# 输入：n = 16 输出：true 解释：24 = 16
# 示例 3：
# 输入：n = 3 输出：false
# 示例 4：
# 输入：n = 4 输出：true
# 示例 5：
# 输入：n = 5 输出：false
# 提示：
# -231 <= n <= 231 - 1
# 进阶：你能够不使用循环/递归解决此问题吗？


#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (43.97%)
# Total Accepted:    15.6K
# Total Submissions: 34.9K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#
class Solution(object):
    bits = {2**i for i in range(32)}
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n in Solution.bits


