# -*- coding:utf-8 -*-

# <SUBID:319943855,UPDATE:20230205>
# English:
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]] Output: 4
# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]] Output: -1 Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
# Input: grid = [[0,2]] Output: 0 Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
# 中文:
# 在给定的 m x n 网格
# grid 中，每个单元格可以有以下三个值之一：
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
# 示例 1：
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]] 输出：4
# 示例 2：
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]] 输出：-1 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
# 示例 3：
# 输入：grid = [[0,2]] 输出：0 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] 仅为 0、1 或 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """暴力法"""

        level = []
        marked = []
        good = 0
        bad = 0
        empty = 0
        total = 0
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    level.append((i, j))
                    tmp.append(True)
                    bad += 1
                elif grid[i][j] == 0:
                    tmp.append(True)
                    empty += 1
                else:
                    tmp.append(False)
                    good += 1
                total += 1
            marked.append(tmp)

        # print(total, empty, good)
        if total == empty:
            return 0
        if total == (good+empty):
            return -1

        days = -1
        max_x, max_y = len(grid), len(grid[0])

        while level:
            next_level = []
            for x, y in level:
                for next_x, next_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if next_x < 0 or next_x >= max_x:
                        continue
                    if next_y < 0 or next_y >= max_y:
                        continue
                    if marked[next_x][next_y]:
                        continue
                    if grid[next_x][next_y] == 1:
                        grid[next_x][next_y] = 2
                        marked[next_x][next_y] = True
                        next_level.append((next_x, next_y))
            days += 1
            level = next_level
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return days
