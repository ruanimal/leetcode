# -*- coding:utf-8 -*-


# English:
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# Example:
# Input: 4 Output: [ [".Q..", // Solution 1 "...Q", "Q...", "..Q."], ["..Q.", // Solution 2 "Q...", "...Q", ".Q.."] ] Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
#
# 中文:
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 上图为 8 皇后问题的一种解法。
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 示例:
# 输入: 4 输出: [ [".Q..", // 解法 1 "...Q", "Q...", "..Q."], ["..Q.", // 解法 2 "Q...", "...Q", ".Q.."] ] 解释: 4 皇后问题存在两个不同的解法。


#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (58.59%)
# Total Accepted:    5.5K
# Total Submissions: 9.2K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
class Solution(object):
    def solveNQueens_1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        求一种解法
        """
        def queens(board, current):
            if current == n:
                return True
            else:
                for i in range(n):
                    board[current] = i
                    if no_confict(board, current):
                        done = queens(board, current+1)
                        if done:
                            return True
                return False

        def no_confict(board, current):
            for i in range(current):
                if board[i] == board[current]:
                    return False
                if (current-i) == abs(board[i] - board[current]):
                    return False
            return True

        board = [-1] * n
        if queens(board, 0):
            return board


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(n, pie, na, res, path):
            # 第n行, 撇, 捺, 结果,
            #终止的条件
            #res 可以把列数存下来
            row = len(path)   # 行
            if row == n:
                res.append(path)
                return

            for col in range(n):  # 列
                if (
                        col not in path and   # 竖向没被占用
                        (row-col) not in pie and  #  行减列的数值可以代表一条斜线上的位置
                        (row+col) not in na  # 另一个方向斜线
                ):
                    pie[row-col] = 1
                    na[row+col] = 1
                    dfs(n, pie, na, res, path+[col])
                    del pie[row-col]
                    del na[row+col]
        res = []
        dfs(n, {}, {}, res, [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in res]



if __name__ == "__main__":
    pass
    print(Solution().solveNQueens(4))
    # print(Solution().solveNQueens(10))

