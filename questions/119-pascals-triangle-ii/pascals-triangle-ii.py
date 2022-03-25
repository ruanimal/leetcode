# -*- coding:utf-8 -*-

# <SUBID:15957213,UPDATE:20220325>
# English:
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
# Example 1:
# Input: rowIndex = 3 Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0 Output: [1]
# Example 3:
# Input: rowIndex = 1 Output: [1,1]
# Constraints:
# 0 <= rowIndex <= 33
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
#
# 中文:
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 示例 1:
# 输入: rowIndex = 3 输出: [1,3,3,1]
# 示例 2:
# 输入: rowIndex = 0 输出: [1]
# 示例 3:
# 输入: rowIndex = 1 输出: [1,1]
# 提示:
# 0 <= rowIndex <= 33
# 进阶：
# 你可以优化你的算法到 O(rowIndex) 空间复杂度吗？


#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (53.78%)
# Total Accepted:    11.8K
# Total Submissions: 21.8K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#


class Solution(object):
    map_dict = {0: [1], 1: [1, 1]}

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex in Solution.map_dict:
            return Solution.map_dict[rowIndex]
        tmp = [1]
        for i in xrange(1, rowIndex):
            tmp.append(self.getRow(rowIndex-1)
                       [i-1] + self.getRow(rowIndex-1)[i])
        tmp.append(1)
        Solution.map_dict[rowIndex] = tmp
        return tmp


