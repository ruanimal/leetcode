# -*- coding:utf-8 -*-

# <SUBID:25059861,UPDATE:20230205>
# English:
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123 Output: 321
# Example 2:
# Input: x = -123 Output: -321
# Example 3:
# Input: x = 120 Output: 21
# Constraints:
# -231 <= x <= 231 - 1
#
# 中文:
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 示例 1：
# 输入：x = 123 输出：321
# 示例 2：
# 输入：x = -123 输出：-321
# 示例 3：
# 输入：x = 120 输出：21
# 示例 4：
# 输入：x = 0 输出：0
# 提示：
# -231 <= x <= 231 - 1


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

