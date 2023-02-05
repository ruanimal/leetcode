# -*- coding:utf-8 -*-

# <SUBID:319153760,UPDATE:20230205>
# English:
# There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).
# Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
# Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
# Example 1:
# Input: moves = "UD" Output: true Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
# Example 2:
# Input: moves = "LL" Output: false Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
# Constraints:
# 1 <= moves.length <= 2 * 104
# moves only contains the characters 'U', 'D', 'L' and 'R'.
#
# 中文:
# 在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。
# 移动顺序由字符串 moves 表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。
# 如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
# 注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。
# 示例 1:
# 输入: moves = "UD" 输出: true 解释：机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。
# 示例 2:
# 输入: moves = "LL" 输出: false 解释：机器人向左移动两次。它最终位于原点的左侧，距原点有两次 “移动” 的距离。我们返回 false，因为它在移动结束时没有返回原点。
# 提示:
# 1 <= moves.length <= 2 * 104
# moves 只包含字符 'U', 'D', 'L' 和 'R'


#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#
# https://leetcode-cn.com/problems/robot-return-to-origin/description/
#
# algorithms
# Easy (68.82%)
# Total Accepted:    14.1K
# Total Submissions: 20.2K
# Testcase Example:  '"UD"'
#
# 在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。
#
# 移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和
# D（下）。如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
#
# 注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。
#
#
#
# 示例 1:
#
# 输入: "UD"
# 输出: true
# 解释：机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。
#
# 示例 2:
#
# 输入: "LL"
# 输出: false
# 解释：机器人向左移动两次。它最终位于原点的左侧，距原点有两次 “移动” 的距离。我们返回 false，因为它在移动结束时没有返回原点。
#
#
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """直接判断 R和L的数目是否相等， 且UD的数目是否相等
        """
        if not moves:
            return True

        x = 0
        y = 0
        # R（右），L（左），U（上）和 D（下）
        for i in moves:
            if i == 'R':
                x += 1
            elif i == 'L':
                x -= 1
            elif i == 'U':
                y -= 1
            elif i == 'D':
                y += 1
        return (x, y) == (0, 0)

if __name__ == "__main__":
    s = Solution().judgeCircle("UD")
    print(s)
    s = Solution().judgeCircle("LL")
    print(s)


