# -*- coding:utf-8 -*-

# <SUBID:15987381,UPDATE:20230205>
# English:
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.
# Example 1:
# Input: n = 16 Output: true
# Example 2:
# Input: n = 5 Output: false
# Example 3:
# Input: n = 1 Output: true
# Constraints:
# -231 <= n <= 231 - 1
# Follow up: Could you solve it without loops/recursion?
#
# 中文:
# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4x
# 示例 1：
# 输入：n = 16 输出：true
# 示例 2：
# 输入：n = 5 输出：false
# 示例 3：
# 输入：n = 1 输出：true
# 提示：
# -231 <= n <= 231 - 1
# 进阶：你能不使用循环或者递归来完成本题吗？


#
# @lc app=leetcode.cn id=342 lang=python
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (44.12%)
# Total Accepted:    6.5K
# Total Submissions: 14.6K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
#
#
# 示例 2:
#
# 输入: 5
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#
class Solution(object):
    powers = {1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144,
                1048576, 4194304, 16777216, 67108864, 268435456, 1073741824}
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in Solution.powers


