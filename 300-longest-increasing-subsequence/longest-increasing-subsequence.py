# -*- coding:utf-8 -*-


# English:
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# Example:
# Input: [10,9,2,5,3,7,101,18] Output: 4 Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
#
# 中文:
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 示例:
# 输入: [10,9,2,5,3,7,101,18] 输出: 4 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (42.45%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 44.5K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        动态规划
        dp[]
        """
        if not nums:
            return 0
        dp = [1]
        for i in range(1, len(nums)):
            max_val = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_val = max(max_val, dp[j])
            dp.append(max_val + 1)
        return max(dp)

if __name__ == "__main__":
    s = Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
    print(s)
    s = Solution().lengthOfLIS([1])
    print(s)

