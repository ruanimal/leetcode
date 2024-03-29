# -*- coding:utf-8 -*-

# <SUBID:319945121,UPDATE:20230205>
# English:
# On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.
# When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.
# Return the number of available captures for the white rook.
# Example 1:
# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]] Output: 3 Explanation: In this example, the rook is attacking all the pawns.
# Example 2:
# Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]] Output: 0 Explanation: The bishops are blocking the rook from attacking any of the pawns.
# Example 3:
# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]] Output: 3 Explanation: The rook is attacking the pawns at positions b5, d6, and f5.
# Constraints:
# board.length == 8
# board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'
#
# 中文:
# 在一个 8 x 8 的棋盘上，有一个白色的车（Rook），用字符 'R' 表示。棋盘上还可能存在空方块，白色的象（Bishop）以及黑色的卒（pawn），分别用字符 '.'，'B' 和 'p' 表示。不难看出，大写字符表示的是白棋，小写字符表示的是黑棋。
# 车按国际象棋中的规则移动。东，西，南，北四个基本方向任选其一，然后一直向选定的方向移动，直到满足下列四个条件之一：
# 棋手选择主动停下来。
# 棋子因到达棋盘的边缘而停下。
# 棋子移动到某一方格来捕获位于该方格上敌方（黑色）的卒，停在该方格内。
# 车不能进入/越过已经放有其他友方棋子（白色的象）的方格，停在友方棋子前。
# 你现在可以控制车移动一次，请你统计有多少敌方的卒处于你的捕获范围内（即，可以被一步捕获的棋子数）。
# 示例 1：
# 输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]] 输出：3 解释： 在本例中，车能够捕获所有的卒。
# 示例 2：
# 输入：[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]] 输出：0 解释： 象阻止了车捕获任何卒。
# 示例 3：
# 输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]] 输出：3 解释： 车可以捕获位置 b5，d6 和 f5 的卒。
# 提示：
# board.length == board[i].length == 8
# board[i][j] 可以是 'R'，'.'，'B' 或 'p'
# 只有一个格子上存在 board[i][j] == 'R'


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        """暴力判断上下左右4个方向"""

        rook = None
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'R':
                    rook = (x, y)
        ret = 0
        for x in range(rook[0]+1, len(board)):
            y = rook[1]
            if board[x][y] == 'p':
                ret += 1
                break
            if board[x][y] == 'B':
                break
        for x in range(rook[0]-1, -1, -1):
            y = rook[1]
            if board[x][y] == 'p':
                ret += 1
                break
            if board[x][y] == 'B':
                break
        for y in range(rook[1]+1, len(board[0])):
            x = rook[0]
            if board[x][y] == 'p':
                ret += 1
                break
            if board[x][y] == 'B':
                break
        for y in range(rook[1]-1, -1, -1):
            x = rook[0]
            if board[x][y] == 'p':
                ret += 1
                break
            if board[x][y] == 'B':
                break
        return ret
