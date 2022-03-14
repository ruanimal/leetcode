# -*- coding:utf-8 -*-


# English:
# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
# After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.
# Return the total surface area of the resulting shapes.
# Note: The bottom face of each shape counts toward its surface area.
# Example 1:
# Input: grid = [[1,2],[3,4]] Output: 34
# Example 2:
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]] Output: 32
# Example 3:
# Input: grid = [[2,2,2],[2,1,2],[2,2,2]] Output: 46
# Constraints:
# n == grid.length == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] <= 50
#
# 中文:
# 给你一个 n * n 的网格 grid ，上面放置着一些 1 x 1 x 1 的正方体。每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
# 放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成一些不规则的三维形体。
# 请你返回最终这些形体的总表面积。
# 注意：每个形体的底面也需要计入表面积中。
# 示例 1：
# 输入：grid = [[1,2],[3,4]] 输出：34
# 示例 2：
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]] 输出：32
# 示例 3：
# 输入：grid = [[2,2,2],[2,1,2],[2,2,2]] 输出：46
# 提示：
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] <= 50


#
# @lc app=leetcode.cn id=892 lang=python
#
# [892] 和至少为 K 的最短子数组
#
# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (48.26%)
# Total Accepted:    1.5K
# Total Submissions: 3K
# Testcase Example:  '[[2]]'
#
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
#
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
#
# 返回结果形体的总表面积。
#
#
#
#
#
#
# 示例 1：
#
# 输入：[[2]]
# 输出：10
#
#
# 示例 2：
#
# 输入：[[1,2],[3,4]]
# 输出：34
#
#
# 示例 3：
#
# 输入：[[1,0],[0,2]]
# 输出：16
#
#
# 示例 4：
#
# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
#
#
# 示例 5：
#
# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#
#
#
#
# 提示：
#
#
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
#
#
#
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.res = 0
        def is_marked(x, y):
            if x < 0 or x >= grid_size:
                return False
            if y < 0 or y >= grid_size:
                return False
            return marked[x][y]

        def count_one_block(x, y, level=0):
            if level == 0:   # 第一层的顶部面积就是整体的顶部面积
                self.res += 2
            if not is_marked(x-1, y):
                self.res += 1
            else:
                self.res -= 1
            if not is_marked(x+1, y):
                self.res += 1
            else:
                self.res -= 1
            if not is_marked(x, y-1):
                self.res += 1
            else:
                self.res -= 1
            if not is_marked(x, y+1):
                self.res += 1
            else:
                self.res -= 1
            marked[x][y] = True

        grid_size = len(grid)
        max_n = max([i for row in grid for i in row])
        print(max_n)
        for level in range(max_n):
            marked = [[False for _ in range(grid_size)] for i in range(grid_size)]
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] <= 0:
                        continue
                    count_one_block(x, y, level)
                    grid[x][y] -= 1

        return self.res

if __name__ == "__main__":
    # data = [[2]]
    # data = [[1,0],[0,2]]
    data = [[2,2,2],[2,1,2],[2,2,2]]
    s = Solution().surfaceArea(data)
    print(s)



