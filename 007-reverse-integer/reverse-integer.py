# -*- coding:utf-8 -*-


# English:
# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123 Output: 321
# Example 2:
# Input: -123 Output: -321
# Example 3:
# Input: 120 Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
# 中文:
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 示例 1:
# 输入: 123 输出: 321
# 示例 2:
# 输入: -123 输出: -321
# 示例 3:
# 输入: 120 输出: 21
# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.46%)
# Total Accepted:    81.1K
# Total Submissions: 257.7K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#
#
# 示例 2:
#
# 输入: -123
# 输出: -321
#
#
# 示例 3:
#
# 输入: 120
# 输出: 21
#
#
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#
#
class Solution:
    def reverse(self, x):
        ans = 0
        flag = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            x, pop = divmod(x, 10)
            ans = ans * 10 + pop
        if ans > 2 ** 31-1 or ans < -(2 ** 31):
            return 0
        return flag * ans

    def reverse_v1(self, x):
        """转为字符串"""

        str_x = str(x)
        if str_x[0] == '-':
            num = '-' + str_x[1::][::-1]
        else:
            num = str_x[::-1]
        num = int(num)
        if num > 2 ** 31-1 or num < -(2 ** 31):
            return 0
        return num

if __name__ == '__main__':
    print(Solution().reverse(-123))

