# -*- coding:utf-8 -*-


# English:
# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
# -1 : My number is lower 1 : My number is higher 0 : Congrats! You got it!
# Example :
# Input: n = 10, pick = 6 Output: 6
#
# 中文:
# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
# -1 : 我的数字比较小 1 : 我的数字比较大 0 : 恭喜！你猜对了！
# 示例 :
# 输入: n = 10, pick = 6 输出: 6


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


