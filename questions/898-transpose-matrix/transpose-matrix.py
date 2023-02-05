# -*- coding:utf-8 -*-

# <SUBID:319562303,UPDATE:20230205>
# English:
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
# Input: matrix = [[1,2,3],[4,5,6]] Output: [[1,4],[2,5],[3,6]]
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# -109 <= matrix[i][j] <= 109
#
# 中文:
# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
# 矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]] 输出：[[1,4,7],[2,5,8],[3,6,9]]
# 示例 2：
# 输入：matrix = [[1,2,3],[4,5,6]] 输出：[[1,4],[2,5],[3,6]]
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 105
# -109 <= matrix[i][j] <= 109


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans
