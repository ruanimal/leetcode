# -*- coding:utf-8 -*-

# <SUBID:319333096,UPDATE:20230205>
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


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """动态规划
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
