# -*- coding:utf-8 -*-

# <SUBID:21003233,UPDATE:20220325>
# English:
# Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
# Example 1:
# Input: n = 3 Output: 3
# Example 2:
# Input: n = 11 Output: 0 Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
# Constraints:
# 1 <= n <= 231 - 1
#
# 中文:
# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位上的数字。
# 示例 1：
# 输入：n = 3 输出：3
# 示例 2：
# 输入：n = 11 输出：0 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
# 提示：
# 1 <= n <= 231 - 1


#
# @lc app=leetcode.cn id=400 lang=python
#
# [400] 第N个数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Easy (31.01%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 11.2K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
#
# 注意:
# n 是正数且在32为整形范围内 ( n < 2^31)。
#
# 示例 1:
#
#
# 输入:
# 3
#
# 输出:
# 3
#
#
# 示例 2:
#
#
# 输入:
# 11
#
# 输出:
# 0
#
# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
#
#
#
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        def func(x):
            if x == 0: return 0
            a = len(str(x))
            return x * a + a - sum(10**i for i in range(a))

        if n < 1:
            return

        left = 0
        right = 2 ** 31
        target = n
        mid = None
        found = False
        while left < right-1:
            mid = (left + right)//2
            mid_val = func(mid)
            if mid_val > target:
                right = mid
            elif mid_val < target:
                left = mid
            else:
                found = True
                break
        # print(left, right)
        if found:
            return str(mid)[-1]
        if func(mid) > target:
            right = mid
        offset = func(right) - n
        return str(right)[-1-offset]
if __name__ == "__main__":
    s = Solution().findNthDigit(15384)
    print(s)
    s = Solution().findNthDigit(10)
    print(s)

