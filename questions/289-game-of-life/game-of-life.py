# -*- coding:utf-8 -*-

# <SUBID:23422422,UPDATE:20220325>
# English:
# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]] Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:
# Input: board = [[1,1],[1,0]] Output: [[1,1],[1,1]]
# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.
# Follow up:
# Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
#
# 中文:
# 根据 百度百科 ， 生命游戏 ，简称为 生命 ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。
# 示例 1：
# 输入：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]] 输出：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# 示例 2：
# 输入：board = [[1,1],[1,0]] 输出：[[1,1],[1,1]]
# 提示：
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] 为 0 或 1
# 进阶：
# 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
# 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？


#
# @lc app=leetcode.cn id=289 lang=python
#
# [289] 生命游戏
#
# https://leetcode-cn.com/problems/game-of-life/description/
#
# algorithms
# Medium (63.51%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 5.1K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# 根据百度百科，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在1970年发明的细胞自动机。
#
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞具有一个初始状态 live（1）即为活细胞， 或
# dead（0）即为死细胞。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
#
#
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
#
#
#
# 根据当前状态，写一个函数来计算面板上细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
#
# 示例:
#
# 输入:
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# 输出:
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
#
# 进阶:
#
#
# 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
# 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
#
#
#
class Solution(object):
    def gameOfLife2(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.

        通过额外的数组记录周围的细胞个数
        """
        def count_cell(x, y):
            points = [
                (x-1, y-1),
                (x-1, y),
                (x-1, y+1),
                (x, y-1),
                (x, y+1),
                (x+1, y-1),
                (x+1, y),
                (x+1, y+1),
            ]
            return sum(board[i][j] for i, j in points if 0 <= i < max_x and 0 <= j < max_y)


        from copy import deepcopy

        count_board = deepcopy(board)
        max_x, max_y = len(board), len(board[0])

        for i in range(max_x):
            for j in range(max_y):
                count_board[i][j] = count_cell(i, j)

        for i in range(max_x):
            for j in range(max_y):
                count = count_board[i][j]
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                else:
                    if count == 3:
                        board[i][j] = 1
        return board

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.

        通过原数组加位运算
        """

        def count_cell(x, y):
            points = [
                (x-1, y-1),
                (x-1, y),
                (x-1, y+1),
                (x, y-1),
                (x, y+1),
                (x+1, y-1),
                (x+1, y),
                (x+1, y+1),
            ]
            return sum((board[i][j] & 1) for i, j in points if 0 <= i < max_x and 0 <= j < max_y)

        if not board:
            return board

        max_x, max_y = len(board), len(board[0])

        for i in range(max_x):
            for j in range(max_y):
                count = count_cell(i, j)
                count <<= 1
                board[i][j] |= count

        for i in range(max_x):
            for j in range(max_y):
                count = board[i][j] >> 1
                board[i][j] &= 1
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                else:
                    if count == 3:
                        board[i][j] = 1
        return board


if __name__ == "__main__":
    data =  [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    s = Solution().gameOfLife(data)
    print(s)

