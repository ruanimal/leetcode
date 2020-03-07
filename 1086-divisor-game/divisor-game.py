# -*- coding:utf-8 -*-


# English:
# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# Also, if a player cannot make a move, they lose the game.
# Return True if and only if Alice wins the game, assuming both players play optimally.
# Example 1:
# Input: 2 Output: true Explanation: Alice chooses 1, and Bob has no more moves.
# Example 2:
# Input: 3 Output: false Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
# Note:
# 1 <= N <= 1000
#
# 中文:
# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
# 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
# 选出任一 x，满足 0 < x < N 且 N % x == 0 。
# 用 N - x 替换黑板上的数字 N 。
# 如果玩家无法执行这些操作，就会输掉游戏。
# 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。
# 示例 1：
# 输入：2 输出：true 解释：爱丽丝选择 1，鲍勃无法进行操作。
# 示例 2：
# 输入：3 输出：false 解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
# 提示：
# 1 <= N <= 1000


#
# @lc app=leetcode.cn id=1025 lang=python
#
# [1025] 除数博弈
#
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        动态规划

        f[N]: 数字N时能否获胜, 当博弈次数为奇数时爱丽丝获胜
        f[N] = True if any(f[N-x]==False) for x in (N的约数) else False
        """
        f = {}
        f[1] = 0
        f[2] = 1
        f[3] = 0
        for i in range(4, N+1):
            f[i] = 0
            for j in range(1, i):
                if i % j != 0:
                    continue
                if f[i-j] == 0:
                    f[i] = 1
                    break
        return bool(f[N])


if __name__ == "__main__":
    s = Solution().divisorGame(4)
    print(s)

