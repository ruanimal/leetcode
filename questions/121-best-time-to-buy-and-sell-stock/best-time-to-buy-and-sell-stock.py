# -*- coding:utf-8 -*-

# <SUBID:17417583,UPDATE:20230205>
# English:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:
# Input: prices = [7,1,5,3,6,4] Output: 5 Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1] Output: 0 Explanation: In this case, no transactions are done and the max profit = 0.
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
#
# 中文:
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
# 示例 1：
# 输入：[7,1,5,3,6,4] 输出：5 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。 注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 示例 2：
# 输入：prices = [7,6,4,3,1] 输出：0 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
# 提示：
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (47.83%)
# Total Accepted:    40.7K
# Total Submissions: 82.7K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#
#
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
#
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        1. f[x] 成本, 到x时的最小成本, lv[x], x时卖出获得的利润
        2. f[x] = min(prices[x], f[x-1]); lv[x] = max(prices[x] - f[x])
        3. f[0] = prices[0]; lv[0] = 0
        """
        if not prices:
            return 0

        f = {}
        lv = {}
        f[0] = prices[0]
        lv[0] = 0

        for x in range(1, len(prices)):
            f[x] = min(prices[x], f[x-1])
            lv[x] = max(prices[x] - f[x], lv[x-1])
        return lv[len(prices)-1]

if __name__ == "__main__":
    s = Solution().maxProfit( [7,1,5,3,6,4])
    print(s)
    s = Solution().maxProfit([7,6,4,3,1])
    print(s)

