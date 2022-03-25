# -*- coding:utf-8 -*-

# <SUBID:24139907,UPDATE:20220325>
# English:
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.
# Example 1:
# Input: n = 4 Output: 4 Explanation: T_3 = 0 + 1 + 1 = 2 T_4 = 1 + 1 + 2 = 4
# Example 2:
# Input: n = 25 Output: 1389537
# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.
#
# 中文:
# 泰波那契序列 Tn 定义如下：
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
# 示例 1：
# 输入：n = 4 输出：4 解释： T_3 = 0 + 1 + 1 = 2 T_4 = 1 + 1 + 2 = 4
# 示例 2：
# 输入：n = 25 输出：1389537
# 提示：
# 0 <= n <= 37
# 答案保证是一个 32 位整数，即 answer <= 2^31 - 1。


class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 0:
            return
        if n < 3:
            return dp[n]
        for i in range(3, n+1):
            tmp = dp[i - 3] + dp[i - 2] + dp[i - 1]
            dp.append(tmp)
        return dp[n]

