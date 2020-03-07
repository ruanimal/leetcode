# -*- coding:utf-8 -*-


# English:
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# Example:
# Input: 19 Output: true Explanation: 12 + 92 = 82 82 + 22 = 68 62 + 82 = 100 12 + 02 + 02 = 1
#
# 中文:
# 编写一个算法来判断一个数是不是“快乐数”。
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
# 示例:
# 输入: 19 输出: true 解释: 12 + 92 = 82 82 + 22 = 68 62 + 82 = 100 12 + 02 + 02 = 1


#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (51.82%)
# Total Accepted:    14.4K
# Total Submissions: 27.5K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到
# 1。如果可以变为 1，那么这个数就是快乐数。
#
# 示例: 
#
# 输入: 19
# 输出: true
# 解释:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
#


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = set()
        while (n != 1):
            n = sum(map(lambda x: int(x)**2, str(n)))
            if n in history:
                return False
            history.add(n)
        return True


