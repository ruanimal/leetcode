# -*- coding:utf-8 -*-

# <SUBID:302067557,UPDATE:20230205>
# English:
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# Example 1:
# Input: nums = [1,1,2] Output: [[1,1,2], [1,2,1], [2,1,1]]
# Example 2:
# Input: nums = [1,2,3] Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
# 中文:
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
# 示例 1：
# 输入：nums = [1,1,2] 输出： [[1,1,2], [1,2,1], [2,1,1]]
# 示例 2：
# 输入：nums = [1,2,3] 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 提示：
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums):
            if len(track) == len(nums):
                ans.append(track[::])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                track.append(nums[i])
                used[i] = True
                backtrack(nums)
                used[i] = False
                track.pop()

        ans = []
        track = []
        used = [False] * len(nums)
        backtrack(sorted(nums))
        return ans

