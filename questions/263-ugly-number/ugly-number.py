# -*- coding:utf-8 -*-


# English:
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
# Example 1:
# Input: n = 6 Output: true Explanation: 6 = 2 × 3
# Example 2:
# Input: n = 1 Output: true Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
# Example 3:
# Input: n = 14 Output: false Explanation: 14 is not ugly since it includes the prime factor 7.
# Constraints:
# -231 <= n <= 231 - 1
#
# 中文:
# 给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
# 示例 1：
# 输入：n = 6 输出：true 解释：6 = 2 × 3
# 示例 2：
# 输入：n = 8 输出：true 解释：8 = 2 × 2 × 2
# 示例 3：
# 输入：n = 14 输出：false 解释：14 不是丑数，因为它包含了另外一个质因数 7 。
# 示例 4：
# 输入：n = 1 输出：true 解释：1 通常被视为丑数。
# 提示：
# -231 <= n <= 231 - 1


#
# @lc app=leetcode.cn id=263 lang=python
#
# [263] 丑数
#
# https://leetcode-cn.com/problems/ugly-number/description/
#
# algorithms
# Easy (44.43%)
# Total Accepted:    7.6K
# Total Submissions: 16.8K
# Testcase Example:  '6'
#
# 编写一个程序判断给定的数是否为丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例 1:
#
# 输入: 6
# 输出: true
# 解释: 6 = 2 × 3
#
# 示例 2:
#
# 输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
#
#
# 示例 3:
#
# 输入: 14
# 输出: false
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。
#
# 说明：
#
#
# 1 是丑数。
# 输入不会超过 32 位有符号整数的范围: [−2^31,  2^31 − 1]。
#
#
#


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        div_map = [2, 3, 5]
        while num > 1:
            flags = map(lambda x: num % x, div_map)
            try:
                next_act = flags.index(0)
            except ValueError:
                return False
            else:
                return self.isUgly(num/div_map[next_act])
        if num == 1:
            return True
        return False



