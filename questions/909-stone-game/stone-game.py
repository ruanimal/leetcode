# -*- coding:utf-8 -*-

# <SUBID:319568087,UPDATE:20230205>
# English:
# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.
# Example 1:
# Input: piles = [5,3,4,5] Output: true Explanation: Alice starts first, and can only take the first 5 or the last 5. Say she takes the first 5, so that the row becomes [3, 4, 5]. If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points. If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points. This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
# Example 2:
# Input: piles = [3,7,2,3] Output: true
# Constraints:
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles[i]) is odd.
#
# 中文:
# Alice 和 Bob 用几堆石子在做游戏。一共有偶数堆石子，排成一行；每堆都有 正 整数颗石子，数目为 piles[i] 。
# 游戏以谁手中的石子最多来决出胜负。石子的 总数 是 奇数 ，所以没有平局。
# Alice 和 Bob 轮流进行，Alice 先开始 。 每回合，玩家从行的 开始 或 结束 处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中 石子最多 的玩家 获胜 。
# 假设 Alice 和 Bob 都发挥出最佳水平，当 Alice 赢得比赛时返回 true ，当 Bob 赢得比赛时返回 false 。
# 示例 1：
# 输入：piles = [5,3,4,5] 输出：true 解释： Alice 先开始，只能拿前 5 颗或后 5 颗石子 。 假设他取了前 5 颗，这一行就变成了 [3,4,5] 。 如果 Bob 拿走前 3 颗，那么剩下的是 [4,5]，Alice 拿走后 5 颗赢得 10 分。 如果 Bob 拿走后 5 颗，那么剩下的是 [3,4]，Alice 拿走后 4 颗赢得 9 分。 这表明，取前 5 颗石子对 Alice 来说是一个胜利的举动，所以返回 true 。
# 示例 2：
# 输入：piles = [3,7,2,3] 输出：true
# 提示：
# 2 <= piles.length <= 500
# piles.length 是 偶数
# 1 <= piles[i] <= 500
# sum(piles[i]) 是 奇数


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        由于堆数是偶数, 先手总能拿到两者中较大的, 所以先手必胜
        """
        return True

