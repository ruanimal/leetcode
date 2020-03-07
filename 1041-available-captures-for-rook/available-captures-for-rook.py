# -*- coding:utf-8 -*-


# English:
# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.
# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.
# Return the number of pawns the rook can capture in one move.
# Example 1:
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]] Output: 3 Explanation: In this example the rook is able to capture all the pawns.
# Example 2:
# Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]] Output: 0 Explanation: Bishops are blocking the rook to capture any pawn.
# Example 3:
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]] Output: 3 Explanation: The rook can capture the pawns at positions b5, d6 and f5.
# Note:
# board.length == board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'
#
# 中文:
# 在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
# 车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。
# 返回车能够在一次移动中捕获到的卒的数量。
#
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


#
# @lc app=leetcode.cn id=999 lang=python
#
# [999] 车的可用捕获量
#
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        '''
        # 广度优先检索, 求所有能走到的方格, 与题意不符
        marks_map = []
        rook = None
        total_pawn_count = 0
        for x in range(len(board)):
            marks_map.append([])
            for y in range(len(board[0])):
                if board[x][y] == 'B':
                    marks_map[x].append(True)
                elif board[x][y] == 'R':
                    rook = (x, y)
                    marks_map[x].append(True)
                elif board[x][y] == 'p':
                    total_pawn_count += 1
                    marks_map[x].append(False)
                else:
                    marks_map[x].append(False)

        level = []
        marks_map[rook[0]][rook[1]] = True
        level.append(rook)
        pawn_count = 0
        while level:
            next_level = []
            for x, y in level:
                if board[x][y] == 'p':
                    pawn_count += 1
                marks_map[x][y] = True
                for nx, ny in [ (x+1, y), (x-1, y), (x, y+1), (x, y-1),]:
                    if ( (0 <= nx < len(board)) and (0 <= ny < len(board[0])) and not marks_map[nx][ny]):
                        next_level.append((nx, ny))
            level = next_level
        return pawn_count
        '''

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

if __name__ == "__main__":
    s = Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]])
    print(s)


