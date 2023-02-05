# -*- coding:utf-8 -*-

# <SUBID:318307430,UPDATE:20230205>
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



class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        """求出所有操作的面积的交集
        """
        if not ops:
            return m * n
        return min(i[0] for i in ops) * min(i[1] for i in ops)

