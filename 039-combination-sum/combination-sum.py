# -*- coding:utf-8 -*-


# English:
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [2,3,6,7], target = 7, A solution set is: [ [7], [2,2,3] ]
# Example 2:
# Input: candidates = [2,3,5], target = 8, A solution set is: [   [2,2,2,2],   [2,3,3],   [3,5] ]
#
# 中文:
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以无限制重复被选取。
# 说明：
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:
# 输入: candidates = [2,3,6,7], target = 7, 所求解集为: [ [7], [2,2,3] ]
# 示例 2:
# 输入: candidates = [2,3,5], target = 8, 所求解集为: [   [2,2,2,2],   [2,3,3],   [3,5] ]


#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (66.21%)
# Likes:    315
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 38.3K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        candidates.sort()
        res = []
        path = []
        self.dfs(candidates, 0, target, path, res)
        return res

    def dfs(self, candidates, begin_level, target, path, res):
        if target == 0:
            res.append(path[:])
        for level in range(begin_level, len(candidates)):
            next_target = target - candidates[level]
            if next_target < 0:
                break
            path.append(candidates[level])
            self.dfs(candidates, level, next_target, path, res)
            path.pop()

if __name__ == "__main__":
    s = Solution().combinationSum(candidates=[2, 3, 6, 7], target=7)
    print(s)
    s = Solution().combinationSum(candidates=[2, 3, 5], target=8)
    print(s)


