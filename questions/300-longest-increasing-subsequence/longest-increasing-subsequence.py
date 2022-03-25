# -*- coding:utf-8 -*-

# <SUBID:24996762,UPDATE:20220325>
# English:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18] Output: 4 Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
# Input: nums = [0,1,0,3,2,3] Output: 4
# Example 3:
# Input: nums = [7,7,7,7,7,7,7] Output: 1
# Constraints:
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
#
# 中文:
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
# 示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18] 输出：4 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
# 输入：nums = [0,1,0,3,2,3] 输出：4
# 示例 3：
# 输入：nums = [7,7,7,7,7,7,7] 输出：1
# 提示：
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
# 进阶：
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?


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

