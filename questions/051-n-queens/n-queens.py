# -*- coding:utf-8 -*-


# English:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
# Example 1:
# Input: n = 4 Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:
# Input: n = 1 Output: [["Q"]]
# Constraints:
# 1 <= n <= 9
#
# 中文:
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 示例 1：
# 输入：n = 4 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
# 输入：n = 1 输出：[["Q"]]
# 提示：
# 1 <= n <= 9


EMPTY = '.'
QUEEN = 'Q'

class Solution(object):
    def solveNQueens(self, n):
        def can_put(i, j):
            return (heng.get(i, 0) == 0 and shu.get(j, 0) == 0
                    and pie.get(i+j, 0) == 0 and na.get(i-j, 0) == 0)

        def backtrack(res, i):
            if i == n:
                res.append([''.join(i) for i in board])
                return

            for j in range(n):
                if can_put(i, j):
                    board[i][j] = QUEEN
                    heng[i] = 1
                    shu[j] = 1
                    pie[i+j] = 1
                    na[i-j] = 1
                    backtrack(res, i+1)
                    heng[i] = 0
                    shu[j] = 0
                    pie[i+j] = 0
                    na[i-j] = 0
                    board[i][j] = EMPTY

        if n == 1:
            return [['Q']]
        board = [['.'] * n for _ in range(n)]
        res = []
        heng = {}
        shu = {}
        pie = {}
        na = {}
        backtrack(res, 0)
        return res
