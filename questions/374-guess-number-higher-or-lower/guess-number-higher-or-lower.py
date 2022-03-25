# -*- coding:utf-8 -*-

# <SUBID:16922438,UPDATE:20220325>
# English:
# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
# Example 1:
# Input: n = 10, pick = 6 Output: 6
# Example 2:
# Input: n = 1, pick = 1 Output: 1
# Example 3:
# Input: n = 2, pick = 1 Output: 1
# Constraints:
# 1 <= n <= 231 - 1
# 1 <= pick <= n
#
# 中文:
# 猜数字游戏的规则如下：
# 每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
# 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
# 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：
# -1：我选出的数字比你猜的数字小 pick < num
# 1：我选出的数字比你猜的数字大 pick > num
# 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
# 返回我选出的数字。
# 示例 1：
# 输入：n = 10, pick = 6 输出：6
# 示例 2：
# 输入：n = 1, pick = 1 输出：1
# 示例 3：
# 输入：n = 2, pick = 1 输出：1
# 示例 4：
# 输入：n = 2, pick = 2 输出：2
# 提示：
# 1 <= n <= 231 - 1
# 1 <= pick <= n


#
# @lc app=leetcode.cn id=374 lang=python
#
# [374] 猜数字大小
#
# https://leetcode-cn.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (35.69%)
# Total Accepted:    5.8K
# Total Submissions: 15.7K
# Testcase Example:  '10\n6'
#
# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
#
# -1 : 我的数字比较小
# ⁠1 : 我的数字比较大
# ⁠0 : 恭喜！你猜对了！
#
#
# 示例 :
#
# 输入: n = 10, pick = 6
# 输出: 6
#
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binary_search(target):
            left = 0
            right = 2 ** 32
            while left <= right:
                mid = (left+right) // 2
                if guess(mid) > 0:
                    left = mid + 1
                elif guess(mid) < 0:
                    right = mid - 1
                else:
                    return mid
            return -1
        return binary_search(n)


