# -*- coding:utf-8 -*-

# <SUBID:307774194,UPDATE:20230205>
# English:
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 Output: true
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 Output: false
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104
#
# 中文:
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 输出：true
# 示例 2：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 输出：false
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        get_val = lambda i: matrix[i//n][i%n]

        left = 0
        right = m * n - 1
        while left < right:
            mid = (left + right) >> 1
            if get_val(mid) < target:
                left = mid + 1
            else:
                right = mid
        if get_val(left) != target:
            return False
        return True

