# -*- coding:utf-8 -*-

# <SUBID:21302765,UPDATE:20220325>
# English:
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# Example 1:
# Input: nums = [1,2,3] Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1] Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1] Output: [[1]]
# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
#
# 中文:
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 示例 1：
# 输入：nums = [1,2,3] 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
# 输入：nums = [0,1] 输出：[[0,1],[1,0]]
# 示例 3：
# 输入：nums = [1] 输出：[[1]]
# 提示：
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同


#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (68.43%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 40.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # from itertools import permutations

        # return list(list(i) for i in permutations(nums))
        ans = []
        def dfs(level, visited):
            if level >= len(nums):
                ans.append(list(visited))
                return
            for i in nums:
                if i not in visited:
                    visited.append(i)
                    dfs(level+1, visited)
                    visited.pop()

        if not nums:
            return []
        dfs(0, [])
        return ans

if __name__ == "__main__":
    s = Solution().permute([1,2,3])
    print(s)
    s = Solution().permute([])
    print(s)


