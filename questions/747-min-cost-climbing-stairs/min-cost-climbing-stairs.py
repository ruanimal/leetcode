# -*- coding:utf-8 -*-


# English:
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# Example 1:
# Input: cost = [10,
# 15
# ,20] Output: 15 Explanation: You will start at index 1. - Pay 15 and climb two steps to reach the top. The total cost is 15.
# Example 2:
# Input: cost = [
# 1
# ,100,
# 1
# ,1,
# 1
# ,100,
# 1
# ,
# 1
# ,100,
# 1
# ] Output: 6 Explanation: You will start at index 0. - Pay 1 and climb two steps to reach index 2. - Pay 1 and climb two steps to reach index 4. - Pay 1 and climb two steps to reach index 6. - Pay 1 and climb one step to reach index 7. - Pay 1 and climb two steps to reach index 9. - Pay 1 and climb one step to reach the top. The total cost is 6.
# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
#
# 中文:
# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
# 请你计算并返回达到楼梯顶部的最低花费。
# 示例 1：
# 输入：cost = [10,15,20] 输出：15 解释：你将从下标为 1 的台阶开始。 - 支付 15 ，向上爬两个台阶，到达楼梯顶部。 总花费为 15 。
# 示例 2：
# 输入：cost = [1,100,1,1,1,100,1,1,100,1] 输出：6 解释：你将从下标为 0 的台阶开始。 - 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。 - 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。 - 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。 - 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。 - 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。 - 支付 1 ，向上爬一个台阶，到达楼梯顶部。 总花费为 6 。
# 提示：
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999


#
# @lc app=leetcode.cn id=746 lang=python
#
# [746] 前缀和后缀搜索
#
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (39.36%)
# Total Accepted:    7.9K
# Total Submissions: 19.1K
# Testcase Example:  '[0,0,0,0]'
#
# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
#
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
#
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
#
# 示例 1:
#
#
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#
#
# 示例 2:
#
#
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#
#
# 注意：
#
#
# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
#
#
#
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        1. f[x], 走完x级时总共的花费; 最后一步只能走x-1, 或者x-2
        2. f[x] = min(cost[x]+f[x-1], cost[x-1]+f[x-2])
        """
        if len(cost) <= 1:
            return 0

        f = {}
        f[-1] = 0
        f[0] = 0
        for x in range(1, len(cost)):
            f[x] = min(cost[x]+f[x-1], cost[x-1]+f[x-2])
        return f[len(cost)-1]

if __name__ == "__main__":
    s = Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    print(s)
    s = Solution().minCostClimbingStairs([10, 15, 20])
    print(s)

