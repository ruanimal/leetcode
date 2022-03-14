# -*- coding:utf-8 -*-


# English:
# You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).
# Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.
# The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.
# Example 1:
# Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0 Output: [[0,0],[0,1]] Explanation: The distances from (0, 0) to other cells are: [0,1]
# Example 2:
# Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1 Output: [[0,1],[0,0],[1,1],[1,0]] Explanation: The distances from (0, 1) to other cells are: [0,1,1,2] The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
# Example 3:
# Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2 Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]] Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3] There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
# Constraints:
# 1 <= rows, cols <= 100
# 0 <= rCenter < rows
# 0 <= cCenter < cols
#
# 中文:
# 给定四个整数 row ,   cols ,  rCenter 和 cCenter 。有一个 rows x cols 的矩阵，你在单元格上的坐标是 (rCenter, cCenter) 。
# 返回矩阵中的所有单元格的坐标，并按与 (rCenter, cCenter) 的 距离 从最小到最大的顺序排。你可以按 任何 满足此条件的顺序返回答案。
# 单元格(r1, c1) 和 (r2, c2) 之间的距离为|r1 - r2| + |c1 - c2|。
# 示例 1：
# 输入：rows = 1, cols = 2, rCenter = 0, cCenter = 0 输出：[[0,0],[0,1]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
# 示例 2：
# 输入：rows = 2, cols = 2, rCenter = 0, cCenter = 1 输出：[[0,1],[0,0],[1,1],[1,0]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2] [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
# 示例 3：
# 输入：rows = 2, cols = 3, rCenter = 1, cCenter = 2 输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3] 其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
# 提示：
# 1 <= rows, cols <= 100
# 0 <= rCenter < rows
# 0 <= cCenter < cols


#
# @lc app=leetcode.cn id=1030 lang=python
#
# [1030] 距离顺序排列矩阵单元格
#
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        dis_map = {}
        for x in range(0, R):
            for y in range(0, C):
                dis_map[(x, y)] = abs(x-r0) + abs(y-c0)
        return [list(i[0]) for i in sorted(dis_map.items(), key=lambda i: i[1])]

if __name__ == "__main__":
    s = Solution().allCellsDistOrder(R = 1, C = 2, r0 = 0, c0 = 0)
    print(s)
    s = Solution().allCellsDistOrder(R = 2, C = 2, r0 = 0, c0 = 1)
    print(s)
    s = Solution().allCellsDistOrder(R = 3, C = 5, r0 = 2, c0 = 3)
    print(s)



