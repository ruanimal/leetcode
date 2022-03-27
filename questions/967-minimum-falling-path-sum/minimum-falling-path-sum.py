# -*- coding:utf-8 -*-

# <SUBID:290236737,UPDATE:20220328>
# English:
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
# Example 1:
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]] Output: 13 Explanation: There are two falling paths with a minimum sum as shown.
# Example 2:
# Input: matrix = [[-19,57],[-40,-5]] Output: -59 Explanation: The falling path with a minimum sum is shown.
# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
#
# 中文:
# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
# 示例 1：
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]] 输出：13 解释：如图所示，为和最小的两条下降路径
# 示例 2：
# 输入：matrix = [[-19,57],[-40,-5]] 输出：-59 解释：如图所示，为和最小的下降路径
# 提示：
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100



from copy import deepcopy

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        if length == 0:
            return 0
        if length == 1:
            return matrix[0][0]

        dp = []
        dp.append(matrix[0][:])
        for i in range(1, length):
            dp.append(matrix[i][:])
            for j in range(length):
                dp[i][j] += min([dp[i-1][k] for k in (j-1, j, j+1) if 0 <= k < length])
        return min(dp[length-1])
