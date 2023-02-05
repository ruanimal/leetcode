# -*- coding:utf-8 -*-

# <SUBID:302050093,UPDATE:20230205>
# English:
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8 Output: [ [1,1,6], [1,2,5], [1,7], [2,6] ]
# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5 Output: [ [1,2,2], [5] ]
# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
# 中文:
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。
# 示例 1:
# 输入: candidates = [10,1,2,7,6,1,5], target = 8, 输出: [ [1,1,6], [1,2,5], [1,7], [2,6] ]
# 示例 2:
# 输入: candidates = [2,5,2,1,2], target = 5, 输出: [ [1,2,2], [5] ]
# 提示:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, idx, total):
            if total == target:
                ans.append(track[::])
                return
            if total > target:
                return
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                total += nums[i]
                track.append(nums[i])
                backtrack(nums, i+1, total)
                track.pop()
                total -= nums[i]

        ans = []
        track = []
        backtrack(sorted(candidates), 0, 0)
        return ans

