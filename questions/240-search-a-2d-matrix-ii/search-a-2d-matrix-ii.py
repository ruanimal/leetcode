# -*- coding:utf-8 -*-

# <SUBID:23469807,UPDATE:20220325>
# English:
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5 Output: true
# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20 Output: false
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -109 <= target <= 109
#
# 中文:
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例 1：
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5 输出：true
# 示例 2：
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20 输出：false
# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -109 <= matrix[i][j] <= 109
# 每行的所有元素从左到右升序排列
# 每列的所有元素从上到下升序排列
# -109 <= target <= 109


#
# @lc app=leetcode.cn id=240 lang=python
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (37.13%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    19.5K
# Total Submissions: 52.6K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
#
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
#
#
# 示例:
#
# 现有矩阵 matrix 如下：
#
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
#
#
# 给定 target = 5，返回 true。
#
# 给定 target = 20，返回 false。
#
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False

        for i in matrix:
            if i[-1] < target or i[0] > target:
                continue
            if self.binary_search(i, target):
                return True
        return False

    @staticmethod
    def binary_search(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True
        return False

if __name__ == "__main__":
    s = Solution().searchMatrix([
        [1,3,5,7,9],
        [2,4,6,8,10],
        [11,13,15,17,19],
        [12,14,16,18,20],
        [21,22,23,24,25]
    ], 13)
    print(s)



