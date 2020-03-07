# -*- coding:utf-8 -*-


# English:
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0,   F(1) = 1 F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).
# Example 1:
# Input: 2 Output: 1 Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
# Input: 3 Output: 2 Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
# Input: 4 Output: 3 Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# Note:
# 0 ≤ N ≤ 30.
#
# 中文:
# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
# F(0) = 0,   F(1) = 1 F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 给定 N，计算 F(N)。
# 示例 1：
# 输入：2 输出：1 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
# 示例 2：
# 输入：3 输出：2 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
# 示例 3：
# 输入：4 输出：3 解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
# 提示：
# 0 ≤ N ≤ 30


#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] Fibonacci Number
#
# https://leetcode-cn.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (64.56%)
# Total Accepted:    6.3K
# Total Submissions: 9.7K
# Testcase Example:  '2'
#
# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
#
#
# 给定 N，计算 F(N)。
#
#
#
# 示例 1：
#
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
#
#
# 示例 2：
#
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
#
#
# 示例 3：
#
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
#
#
# 提示：
#
#
# 0 ≤ N ≤ 30
#
#
#
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        f0, f1 = 0, 1
        for i in range(N):
            f1, f0 = f1+f0, f1
        return f0

if __name__ == "__main__":
    s = Solution().fib(4)
    print(s)

