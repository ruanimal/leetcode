# -*- coding:utf-8 -*-


# English:
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
# Input: nums = [1,2,3] Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:
# Input: nums = [0] Output: [[],[0]]
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
# 中文:
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 示例 1：
# 输入：nums = [1,2,3] 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
# 输入：nums = [0] 输出：[[],[0]]
# 提示：
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同


#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (72.66%)
# Likes:    264
# Dislikes: 0
# Total Accepted:    22.9K
# Total Submissions: 31K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def recursion(i, visited):
            if i >= len(nums):
                ans.append([nums[idx] for idx, x in enumerate(visited) if x])
                return

            visited.append(0)
            recursion(i+1, visited)
            visited.pop()

            visited.append(1)
            recursion(i+1, visited)
            visited.pop()

        recursion(0, [])
        return ans

if __name__ == "__main__":
    s = Solution().subsets([1,2,3])
    print(s)


