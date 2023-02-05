# -*- coding:utf-8 -*-

# <SUBID:16923080,UPDATE:20230205>
# English:
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
# Example 1:
# Input: n = 5 Output: 2 Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:
# Input: n = 8 Output: 3 Explanation: Because the 4th row is incomplete, we return 3.
# Constraints:
# 1 <= n <= 231 - 1
#
# 中文:
# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。
# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。
# 示例 1：
# 输入：n = 5 输出：2 解释：因为第三行不完整，所以返回 2 。
# 示例 2：
# 输入：n = 8 输出：3 解释：因为第四行不完整，所以返回 3 。
# 提示：
# 1 <= n <= 231 - 1


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


