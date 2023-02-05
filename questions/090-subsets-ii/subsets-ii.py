# -*- coding:utf-8 -*-

# <SUBID:302043423,UPDATE:20230205>
# English:
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
# Input: nums = [1,2,2] Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0] Output: [[],[0]]
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
#
# 中文:
# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
# 示例 1：
# 输入：nums = [1,2,2] 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
# 示例 2：
# 输入：nums = [0] 输出：[[],[0]]
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, idx):
            ans.append(track[::])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:  # 关键剪枝
                    continue
                track.append(nums[i])
                backtrack(nums, i+1)
                track.pop()

        ans = []
        track = []
        backtrack(sorted(nums), 0)
        return ans

