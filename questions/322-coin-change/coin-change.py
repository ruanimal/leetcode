# -*- coding:utf-8 -*-

# <SUBID:17470533,UPDATE:20220325>
# English:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
# Example 1:
# Input: coins = [1,2,5], amount = 11 Output: 3 Explanation: 11 = 5 + 5 + 1
# Example 2:
# Input: coins = [2], amount = 3 Output: -1
# Example 3:
# Input: coins = [1], amount = 0 Output: 0
# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104
#
# 中文:
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
# 你可以认为每种硬币的数量是无限的。
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11 输出：3 解释：11 = 5 + 5 + 1
# 示例 2：
# 输入：coins = [2], amount = 3 输出：-1
# 示例 3：
# 输入：coins = [1], amount = 0 输出：0
# 提示：
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104


#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (30.14%)
# Total Accepted:    8.8K
# Total Submissions: 28.3K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
# 说明:
# 你可以认为每种硬币的数量是无限的。
#
#
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        1. f[x], 凑成金额x所需的硬币个数amount；
           到最后一个硬币是，有3总情况 f[x-1] + 1, f[x-2] + 1, f[x-5] + 1; 取最小
        2. f[x] = min(f[x-1] + 1, f[x-2] + 1, f[x-5] + 1)
        3. x < 0时， amount = inf
        """
        if not coins:
            return -1

        inf = float("inf")
        f = {0:0}
        for x in range(1, amount+1):
            f[x] = min((f.get(x-j, inf) + 1) for j in coins)
        if f[amount] == inf:
            return -1
        return f[amount]

if __name__ == "__main__":
    s = Solution().coinChange(coins = [1, 2, 5], amount = 11)
    print(s)
    s = Solution().coinChange(coins = [2], amount = 3)
    print(s)

