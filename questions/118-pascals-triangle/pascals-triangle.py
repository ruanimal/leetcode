# -*- coding:utf-8 -*-


# English:
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it.
# Example:
# Input: 5 Output: [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
#
# 中文:
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 示例:
# 输入: 5 输出: [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]


#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (59.60%)
# Total Accepted:    19.2K
# Total Submissions: 31.5K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        if numRows == 1:
            return [[1], ]
        lst = [[1]*i for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
        return lst


