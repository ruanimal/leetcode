# -*- coding:utf-8 -*-

# <SUBID:19568735,UPDATE:20220325>
# English:
# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
# Count and return the number of maximum integers in the matrix after performing all the operations.
# Example 1:
# Input: m = 3, n = 3, ops = [[2,2],[3,3]] Output: 4 Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
# Example 2:
# Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]] Output: 4
# Example 3:
# Input: m = 3, n = 3, ops = [] Output: 9
# Constraints:
# 1 <= m, n <= 4 * 104
# 0 <= ops.length <= 104
# ops[i].length == 2
# 1 <= ai <= m
# 1 <= bi <= n
#
# 中文:
# 给你一个 m x n 的矩阵 M ，初始化时所有的 0 和一个操作数组 op ，其中 ops[i] = [ai, bi] 意味着当所有的 0 <= x < ai 和 0 <= y < bi 时， M[x][y] 应该加 1。
# 在 执行完所有操作后 ，计算并返回 矩阵中最大整数的个数 。
# 示例 1:
# 输入: m = 3, n = 3，ops = [[2,2],[3,3]] 输出: 4 解释: M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。
# 示例 2:
# 输入: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]] 输出: 4
# 示例 3:
# 输入: m = 3, n = 3, ops = [] 输出: 9
# 提示:
# 1 <= m, n <= 4 * 104
# 0 <= ops.length <= 104
# ops[i].length == 2
# 1 <= ai <= m
# 1 <= bi <= n


#
# @lc app=leetcode.cn id=598 lang=python
#
# [598] 范围求和 II
#
# https://leetcode-cn.com/problems/range-addition-ii/description/
#
# algorithms
# Easy (47.39%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 5K
# Testcase Example:  '3\n3\n[[2,2],[3,3]]'
#
# 给定一个初始元素全部为 0，大小为 m*n 的矩阵 M 以及在 M 上的一系列更新操作。
#
# 操作用二维数组表示，其中的每个操作用一个含有两个正整数 a 和 b 的数组表示，含义是将所有符合 0 <= i < a 以及 0 <= j < b 的元素
# M[i][j] 的值都增加 1。
#
# 在执行给定的一系列操作后，你需要返回矩阵中含有最大整数的元素个数。
#
# 示例 1:
#
#
# 输入:
# m = 3, n = 3
# operations = [[2,2],[3,3]]
# 输出: 4
# 解释:
# 初始状态, M =
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
#
# 执行完操作 [2,2] 后, M =
# [[1, 1, 0],
# ⁠[1, 1, 0],
# ⁠[0, 0, 0]]
#
# 执行完操作 [3,3] 后, M =
# [[2, 2, 1],
# ⁠[2, 2, 1],
# ⁠[1, 1, 1]]
#
# M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。
#
#
# 注意:
#
#
# m 和 n 的范围是 [1,40000]。
# a 的范围是 [1,m]，b 的范围是 [1,n]。
# 操作数目不超过 10000。
#
#
#
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        return min(i[0] for i in ops) * min(i[1] for i in ops)


