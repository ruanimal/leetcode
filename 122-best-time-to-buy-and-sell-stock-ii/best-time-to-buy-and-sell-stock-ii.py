# -*- coding:utf-8 -*-


# English:
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
# Example 1:
# Input: [7,1,5,3,6,4] Output: 7 Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.   Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:
# Input: [1,2,3,4,5] Output: 4 Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.   Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are   engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
# Input: [7,6,4,3,1] Output: 0 Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
# 中文:
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 示例 1:
# 输入: [7,1,5,3,6,4] 输出: 7 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
# 示例 2:
# 输入: [1,2,3,4,5] 输出: 4 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 示例 3:
# 输入: [7,6,4,3,1] 输出: 0 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


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



