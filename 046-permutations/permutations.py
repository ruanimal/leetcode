# -*- coding:utf-8 -*-


# English:
# Given a collection of distinct integers, return all possible permutations.
# Example:
# Input: [1,2,3] Output: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
#
# 中文:
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 示例:
# 输入: [1,2,3] 输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]


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


