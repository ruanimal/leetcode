# -*- coding:utf-8 -*-

# <SUBID:314347040,UPDATE:20230205>
# English:
# You are playing the following Nim Game with your friend:
# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# The one who removes the last stone is the winner.
# Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
# Example 1:
# Input: n = 4 Output: false Explanation: These are the possible outcomes: 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins. 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins. 3. You remove 3 stones. Your friend removes the last stone. Your friend wins. In all outcomes, your friend wins.
# Example 2:
# Input: n = 1 Output: true
# Example 3:
# Input: n = 2 Output: true
# Constraints:
# 1 <= n <= 231 - 1
#
# 中文:
# 你和你的朋友，两个人一起玩 Nim 游戏：
# 桌子上有一堆石头。
# 你们轮流进行自己的回合， 你作为先手 。
# 每一回合，轮到的人拿掉 1 - 3 块石头。
# 拿掉最后一块石头的人就是获胜者。
# 假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 n 的情况下赢得游戏。如果可以赢，返回 true；否则，返回 false 。
# 示例 1：
# 输入：n = 4 输出：false 解释：以下是可能的结果: 1. 移除1颗石头。你的朋友移走了3块石头，包括最后一块。你的朋友赢了。 2. 移除2个石子。你的朋友移走2块石头，包括最后一块。你的朋友赢了。 3.你移走3颗石子。你的朋友移走了最后一块石头。你的朋友赢了。 在所有结果中，你的朋友是赢家。
# 示例 2：
# 输入：n = 1 输出：true
# 示例 3：
# 输入：n = 2 输出：true
# 提示：
# 1 <= n <= 231 - 1


#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim游戏
#
# https://leetcode-cn.com/problems/nim-game/description/
#
# algorithms
# Easy (65.93%)
# Total Accepted:    13K
# Total Submissions: 19.4K
# Testcase Example:  '4'
#
# 你和你的朋友，两个人一起玩 Nim游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。
#
# 你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
#
# 示例:
#
# 输入: 4
# 输出: false
# 解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
# 因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
#
#
#
class Solution(object):
    def canWinNim(self, n: int) -> bool:
        """
        如果石头是4的倍数, 那么等你拿了a个之后, 他可以拿4-a个, 最终和4个的情况是一样的, 对手赢
        """
        if n % 4 == 0:
            return False
        else:
            return True


