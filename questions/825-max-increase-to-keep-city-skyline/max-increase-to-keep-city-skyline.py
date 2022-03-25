# -*- coding:utf-8 -*-

# <SUBID:22403725,UPDATE:20220325>
# English:
# There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.
# A city's skyline is the the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.
# We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.
# Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.
# Example 1:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]] Output: 35 Explanation: The building heights are shown in the center of the above image. The skylines when viewed from each cardinal direction are drawn in red. The grid after increasing the height of buildings without affecting skylines is: gridNew = [ [8, 4, 8, 7], [7, 4, 7, 7], [9, 4, 8, 7], [3, 3, 3, 3] ]
# Example 2:
# Input: grid = [[0,0,0],[0,0,0],[0,0,0]] Output: 0 Explanation: Increasing the height of any building will result in the skyline changing.
# Constraints:
# n == grid.length
# n == grid[r].length
# 2 <= n <= 50
# 0 <= grid[r][c] <= 100
#
# 中文:
# 给你一座由 n x n 个街区组成的城市，每个街区都包含一座立方体建筑。给你一个下标从 0 开始的 n x n 整数矩阵 grid ，其中 grid[r][c] 表示坐落于 r 行 c 列的建筑物的 高度 。
# 城市的 天际线 是从远处观察城市时，所有建筑物形成的外部轮廓。从东、南、西、北四个主要方向观测到的 天际线 可能不同。
# 我们被允许为 任意数量的建筑物 的高度增加 任意增量（不同建筑物的增量可能不同） 。 高度为 0 的建筑物的高度也可以增加。然而，增加的建筑物高度 不能影响 从任何主要方向观察城市得到的 天际线 。
# 在 不改变 从任何主要方向观测到的城市 天际线 的前提下，返回建筑物可以增加的 最大高度增量总和 。
# 示例 1：
# 输入：grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]] 输出：35 解释：建筑物的高度如上图中心所示。 用红色绘制从不同方向观看得到的天际线。 在不影响天际线的情况下，增加建筑物的高度： gridNew = [ [8, 4, 8, 7], [7, 4, 7, 7], [9, 4, 8, 7], [3, 3, 3, 3] ]
# 示例 2：
# 输入：grid = [[0,0,0],[0,0,0],[0,0,0]] 输出：0 解释：增加任何建筑物的高度都会导致天际线的变化。
# 提示：
# n == grid.length
# n == grid[r].length
# 2 <= n <= 50
# 0 <= grid[r][c] <= 100


#
# @lc app=leetcode.cn id=807 lang=python
#
# [807] 保持城市天际线
#
# https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline/description/
#
# algorithms
# Medium (75.54%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 5.1K
# Testcase Example:  '[[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]'
#
# 在二维数组grid中，grid[i][j]代表位于某处的建筑物的高度。 我们被允许增加任何数量（不同建筑物的数量可能不同）的建筑物的高度。 高度 0
# 也被认为是建筑物。
#
# 最后，从新数组的所有四个方向（即顶部，底部，左侧和右侧）观看的“天际线”必须与原始数组的天际线相同。
# 城市的天际线是从远处观看时，由所有建筑物形成的矩形的外部轮廓。 请看下面的例子。
#
# 建筑物高度可以增加的最大总和是多少？
#
#
# 例子：
# 输入： grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# 输出： 35
# 解释：
# The grid is:
# [ [3, 0, 8, 4],
# ⁠ [2, 4, 5, 7],
# ⁠ [9, 2, 6, 3],
# ⁠ [0, 3, 1, 0] ]
#
# 从数组竖直方向（即顶部，底部）看“天际线”是：[9, 4, 8, 7]
# 从水平水平方向（即左侧，右侧）看“天际线”是：[8, 7, 9, 3]
#
# 在不影响天际线的情况下对建筑物进行增高后，新数组如下：
#
# gridNew = [ [8, 4, 8, 7],
# ⁠           [7, 4, 7, 7],
# ⁠           [9, 4, 8, 7],
# ⁠           [3, 3, 3, 3] ]
#
#
# 说明:
#
#
# 1 < grid.length = grid[0].length <= 50。
# grid[i][j] 的高度范围是： [0, 100]。
# 一座建筑物占据一个grid[i][j]：换言之，它们是 1 x 1 x grid[i][j] 的长方体。
#
#
#
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_x = [max(i) for i in grid]
        max_y = [max(i) for i in zip(*grid)]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += (min(max_x[i], max_y[j]) - grid[i][j])
        return ans

if __name__ == "__main__":
    s = Solution().maxIncreaseKeepingSkyline( [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
    print(s)

