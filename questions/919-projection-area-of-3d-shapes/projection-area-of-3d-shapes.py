# -*- coding:utf-8 -*-

# <SUBID:18238350,UPDATE:20220325>
# English:
# You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).
# We view the projection of these cubes onto the xy, yz, and zx planes.
# A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
# Return the total area of all three projections.
# Example 1:
# Input: grid = [[1,2],[3,4]] Output: 17 Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
# Example 2:
# Input: grid = [[2]] Output: 5
# Example 3:
# Input: grid = [[1,0],[0,2]] Output: 8
# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] <= 50
#
# 中文:
# 在
# n x n 的网格
# grid 中，我们放置了一些与 x，y，z 三轴对齐的
# 1 x 1 x 1 立方体。
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
# 现在，我们查看这些立方体在 xy 、yz 和 zx 平面上的投影。
# 投影 就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。
# 返回 所有三个投影的总面积 。
# 示例 1：
# 输入：[[1,2],[3,4]] 输出：17 解释：这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。
# 示例 2:
# 输入：grid = [[2]] 输出：5
# 示例 3：
# 输入：[[1,0],[0,2]] 输出：8
# 提示：
# n == grid.length == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] <= 50


#
# @lc app=leetcode.cn id=883 lang=python
#
# [883] 三维形体投影面积
#
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        for x in range(len(grid)):
            ret += max(grid[x])  # y 方向投影

        for y in range(len(grid[0])):
            tmp = 0
            for x in range(len(grid)):
                if grid[x][y] > 0:
                    ret += 1  # z 方向投影
                tmp = max(tmp, grid[x][y])
            ret += tmp  # x 方向投影
        return ret

if __name__ == "__main__":
    s = Solution().projectionArea([[1,2],[3,4]])
    print(s)

