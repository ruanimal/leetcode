# -*- coding:utf-8 -*-

# <SUBID:314403501,UPDATE:20230205>
# English:
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
# Example 1:
# Input: n = 27 Output: true Explanation: 27 = 33
# Example 2:
# Input: n = 0 Output: false Explanation: There is no x where 3x = 0.
# Example 3:
# Input: n = -1 Output: false Explanation: There is no x where 3x = (-1).
# Constraints:
# -231 <= n <= 231 - 1
# Follow up: Could you solve it without loops/recursion?
#
# 中文:
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x
# 示例 1：
# 输入：n = 27 输出：true
# 示例 2：
# 输入：n = 0 输出：false
# 示例 3：
# 输入：n = 9 输出：true
# 示例 4：
# 输入：n = 45 输出：false
# 提示：
# -231 <= n <= 231 - 1
# 进阶：你能不使用循环或者递归来完成本题吗？


#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
# https://leetcode-cn.com/problems/power-of-three/description/
#
# algorithms
# Easy (42.34%)
# Total Accepted:    14.9K
# Total Submissions: 34.7K
# Testcase Example:  '27'
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例 1:
#
# 输入: 27
# 输出: true
#
#
# 示例 2:
#
# 输入: 0
# 输出: false
#
# 示例 3:
#
# 输入: 9
# 输出: true
#
# 示例 4:
#
# 输入: 45
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#


class SolutionA(object):
    def isPowerOfThree(self, n: int) -> bool:
        """
        3 ** 19 = 1162261467, int32范围内最大的3的次方
        如果1162261467能被n整除, 说明n是3的0-19次幂, 否则不是.
        """
        return (n > 0 and 1162261467 % n == 0)

class Solution(object):
    nums = {3 ** i for i in range(20)}
    def isPowerOfThree(self, n: int) -> bool:
        """查表法"""
        return n in self.nums


