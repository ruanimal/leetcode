# -*- coding:utf-8 -*-

# <SUBID:194526612,UPDATE:20230205>
# English:
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]] Explanation: The input board is shown above and the only valid solution is shown below:
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
#
# 中文:
# 编写一个程序，通过填充空格来解决数独问题。
# 数独的解法需 遵循如下规则：
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用 '.' 表示。
# 示例 1：
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]] 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
# 提示：
# board.length == 9
# board[i].length == 9
# board[i][j] 是一位数字或者 '.'
# 题目数据 保证 输入数独仅有一个解


EMPTY = '.'

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def solve(board):
            for i in range(9):
                for j in range(9):
                    box_index = (i // 3 ) * 3 + j // 3
                    if board[i][j] == EMPTY:
                        for c in (rows[i] & columns[j] & boxes[box_index]):    # 通过集合来剪枝
                            # 设置状态
                            board[i][j] = c
                            tmp = [False, False, False]
                            for idx, elem in enumerate((rows[i], columns[j], boxes[box_index])):
                                if c in elem:
                                    elem.remove(c)
                                    tmp[idx] = True
                            # 进入下一层递归
                            if solve(board):
                                return True
                            # 还原状态
                            board[i][j] = EMPTY
                            for idx, elem in zip(tmp, (rows[i], columns[j], boxes[box_index])):
                                if idx:
                                    elem.add(c)
                        return False
            return True

        # 验证题目是否合法, 初始化每一格可选择项
        rows = [set(str(i) for i in range(1,10)) for i in range(9)]
        columns = [set(str(i) for i in range(1,10)) for i in range(9)]
        boxes = [set(str(i) for i in range(1,10)) for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != EMPTY:
                    box_index = (i // 3 ) * 3 + j // 3
                    if num not in rows[i]:
                        return False
                    rows[i].remove(num)
                    if num not in columns[j]:
                        return False
                    columns[j].remove(num)
                    if num not in boxes[box_index]:
                        return False
                    boxes[box_index].remove(num)
        return solve(board)
