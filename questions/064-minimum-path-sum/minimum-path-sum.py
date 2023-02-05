# -*- coding:utf-8 -*-

# <SUBID:308548124,UPDATE:20230205>
# English:
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]] Output: 7 Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:
# Input: grid = [[1,2,3],[4,5,6]] Output: 12
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
#
# 中文:
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。
# 示例 1：
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]] 输出：7 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：
# 输入：grid = [[1,2,3],[4,5,6]] 输出：12
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100


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

        1. f[x][y] 表示到x， y位置时的最短路径; 只能往下或者往右到达该位置
            最后一步： min(f[x-1][y] + grid[x][y], f[x][y-1] + grid[x][y])
        2. f[x][y] = min(f[x-1][y] + grid[x][y], f[x][y-1] + grid[x][y])
        3. 0 <= x < len(grid[0]), 0 <= y < len(grid)
        """
        if not grid:
            return 0

        f = [{} for _ in range(len(grid))]
        for y in range(len(grid[0])):  # 处理上边沿的情况
            f[0][y] = f[0].get(y-1, 0) + grid[0][y]
        # pprint(f)
        for x in range(1, len(grid)):
            f[x][0] = grid[x][0] + f[x-1][0]   # # 处理左边沿的情况
            for y in range(1, len(grid[x])):
                f[x][y] = min(f[x-1][y] + grid[x][y], f[x][y-1] + grid[x][y])
        # print(f)
        return f[len(grid)-1][len(grid[0])-1]

