# -*- coding:utf-8 -*-

# <SUBID:18690699,UPDATE:20220325>
# English:
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
# Example 1:
# Input: prices = [7,1,5,3,6,4] Output: 7 Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7.
# Example 2:
# Input: prices = [1,2,3,4,5] Output: 4 Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4.
# Example 3:
# Input: prices = [7,6,4,3,1] Output: 0 Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104
#
# 中文:
# 给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。
# 在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
# 返回 你能获得的 最大 利润 。
# 示例 1:
# 输入: prices = [7,1,5,3,6,4] 输出: 7 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:
# 输入: prices = [1,2,3,4,5] 输出: 4 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:
# 输入: prices = [7,6,4,3,1] 输出: 0 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 提示：
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104


#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        buy = sale = None
        for i in range(len(prices)):
            if i == 0:
                a = 2**31
            else:
                a = prices[i-1]
            if i == len(prices)-1:
                c = 0
            else:
                c = prices[i+1]
            b = prices[i]
            if b == min(a, b, c):
                buy = b
            if b == max(a, b, c) and buy is not None:
                sale = b
            # print(buy, sale)
            if buy is not None and sale is not None:
                ans += (sale-buy)
                buy = sale = None
        return ans

if __name__ == "__main__":
    s = Solution().maxProfit([7,1,5,3,6,4])
    print(s)
    s = Solution().maxProfit([1,2,3,4,5])
    print(s)
    s = Solution().maxProfit([1])
    print(s)



