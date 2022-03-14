# -*- coding:utf-8 -*-


# English:
# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4 Output: [[1,2,3,4]]
# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4 Output: [[1,2],[3,4]]
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300
#
# 中文:
# 在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。
# 给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
# 重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
# 如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
# 示例 1：
# 输入：mat = [[1,2],[3,4]], r = 1, c = 4 输出：[[1,2,3,4]]
# 示例 2：
# 输入：mat = [[1,2],[3,4]], r = 2, c = 4 输出：[[1,2],[3,4]]
# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# -1000 <= mat[i][j] <= 1000
# 1 <= r, c <= 300


#
# @lc app=leetcode.cn id=566 lang=python
#
# [566] 重塑矩阵
#
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat_nums = sum(nums, [])
        if r * c != len(flat_nums):
            return nums

        ans = []
        for i in range(r):
            tmp = flat_nums[i*c:(i+1)*c]
            ans.append(tmp)
        return ans

if __name__ == "__main__":
    s = Solution().matrixReshape([[1,2], [3,4]], r = 2, c = 4)
    print(s)


