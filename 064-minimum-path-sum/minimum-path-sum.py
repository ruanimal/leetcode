# -*- coding:utf-8 -*-


# English:
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Example:
# Input: [   [1,3,1], [1,5,1], [4,2,1] ] Output: 7 Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
# 中文:
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 示例:
# 输入: [   [1,3,1], [1,5,1], [4,2,1] ] 输出: 7 解释: 因为路径 1→3→1→1→1 的总和最小。


#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (59.23%)
# Total Accepted:    13.9K
# Total Submissions: 23.1K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        1. f[x][y] 到x， y位置时的最短路径
            最后一步： min(f[x-1][y] + grid[x][y], f[x][y-1] + grid[x][y])
        2. f[x][y] = min(f[x-1][y] + grid[x][y], f[x][y-1] + grid[x][y])
        3. 0 <= x < len(grid[0]), 0 <= y < len(grid)
        """
        if not grid:
            return 0

        f = [{} for _ in range(len(grid))]
        for y in range(len(grid[0])):
            f[0][y] = f[0].get(y-1, 0) + grid[0][y]
        for x in range(1, len(grid)):
            f[x][0] = grid[x][0] + f[x-1][0]
            for y in range(1, len(grid[x])):
                f[x][y] = min(f[x-1][y] + grid[x][y], f[x][y-1] + grid[x][y])
        # print(f)
        return f[len(grid)-1][len(grid[0])-1]

if __name__ == "__main__":
    s = Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])
    print(s)
    s = Solution().minPathSum([[1,2],[1,1]])
    print(s)

