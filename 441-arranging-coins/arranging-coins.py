# -*- coding:utf-8 -*-


# English:
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
# Example 1:
# n = 5 The coins can form the following rows: ¤ ¤ ¤ ¤ ¤ Because the 3rd row is incomplete, we return 2.
# Example 2:
# n = 8 The coins can form the following rows: ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ Because the 4th row is incomplete, we return 3.
#
# 中文:
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
# 给定一个数字 n，找出可形成完整阶梯行的总行数。
# n 是一个非负整数，并且在32位有符号整型的范围内。
# 示例 1:
# n = 5 硬币可排列成以下几行: ¤ ¤ ¤ ¤ ¤ 因为第三行不完整，所以返回2.
# 示例 2:
# n = 8 硬币可排列成以下几行: ¤ ¤ ¤ ¤ ¤ ¤ ¤ ¤ 因为第四行不完整，所以返回3.


#
# @lc app=leetcode.cn id=441 lang=python
#
# [441] 排列硬币
#
# https://leetcode-cn.com/problems/arranging-coins/description/
#
# algorithms
# Easy (35.33%)
# Total Accepted:    6.1K
# Total Submissions: 16.8K
# Testcase Example:  '5'
#
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
#
# 给定一个数字 n，找出可形成完整阶梯行的总行数。
#
# n 是一个非负整数，并且在32位有符号整型的范围内。
#
# 示例 1:
#
#
# n = 5
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤
#
# 因为第三行不完整，所以返回2.
#
#
# 示例 2:
#
#
# n = 8
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# 因为第四行不完整，所以返回3.
#
#
#
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        n = ret(ret+1)/2
        ret =
        """
        import math

        ret = (-1 + math.sqrt(1**2 + 4*1*2*n)) / 2
        return int(ret // 1)

if __name__ == "__main__":
    s = Solution().arrangeCoins(10)
    print(s)
        # ret = binary_search(num)


