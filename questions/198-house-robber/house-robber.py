# -*- coding:utf-8 -*-


# English:
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# Example 1:
# Input: nums = [1,2,3,1] Output: 4 Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.
# Example 2:
# Input: nums = [2,7,9,3,1] Output: 12 Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
# 中文:
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
# 示例 1：
# 输入：[1,2,3,1] 输出：4 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。   偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：
# 输入：[2,7,9,3,1] 输出：12 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。   偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400


#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#
# https://leetcode-cn.com/problems/house-robber/description/
#
# algorithms
# Easy (39.04%)
# Total Accepted:    20.2K
# Total Submissions: 51K
# Testcase Example:  '[1,2,3,1]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
# 示例 2:
#
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#
#
#


class Solution(object):
    def rob(self, nums, money=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) < 1:
        #     return 0
        # if len(nums) == 1:
        #     return money + nums[0]
        # elif len(nums) == 2:  # 只有两间房, 投多的那间
        #     return money + max(nums)
        # else:
        #     if nums[0] >= nums[1]:
        #         money += nums[0]
        #         return self.rob(nums[2:], money)
        #     else:
        #         nums[2] = nums[0] + nums[2]
        #         return self.rob(nums[1:], money)

        # 动态规划
        n = len(nums)
        if (n <= 1):
            return  0 if n == 0 else nums[0]
        memo = [0 for _ in range(n)]
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])   # 临近的两间房, 选钱多的那个
        for i in range(2, n):
            memo[i] = max(memo[i-1], nums[i] + memo[i-2])
        return memo[n - 1]

if __name__ == "__main__":
    s = Solution().rob([2,7,9,3,1])
    print(s)




