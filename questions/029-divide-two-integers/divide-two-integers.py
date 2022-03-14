# -*- coding:utf-8 -*-


# English:
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
# Example 1:
# Input: dividend = 10, divisor = 3 Output: 3 Explanation: 10/3 = 3.33333.. which is truncated to 3.
# Example 2:
# Input: dividend = 7, divisor = -3 Output: -2 Explanation: 7/-3 = -2.33333.. which is truncated to -2.
# Constraints:
# -231 <= dividend, divisor <= 231 - 1
# divisor != 0
#
# 中文:
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
# 示例 1:
# 输入: dividend = 10, divisor = 3 输出: 3 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 示例 2:
# 输入: dividend = 7, divisor = -3 输出: -2 解释: 7/-3 = truncate(-2.33333..) = -2
# 提示：
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。


#
# @lc app=leetcode.cn id=29 lang=python
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (18.46%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    20.2K
# Total Submissions: 108.2K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
#
# 示例 2:
#
# 输入: dividend = 7, divisor = -3
# 输出: -2
#
# 说明:
#
#
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
#
#
#
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if divisor == 0:
            return

        if (dividend < 0 and divisor < 0) or (dividend >0 and divisor >0):
            neg_flag = False
        else:
            neg_flag = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        divisors = [divisor]
        ans = 0

        while divisors[-1] < dividend:
            divisors.append(divisors[-1] + divisors[-1])

        for idx in range(len(divisors)-1, -1, -1):
            if dividend == 0:
                break
            elem = divisors[idx]
            if dividend - elem >= 0:
                ans += 2 ** (idx)
                dividend -= elem
        ans = ans if not neg_flag else -ans
        if ans > 2147483647:
            return 2147483647
        elif ans < -2147483648:
            return -2147483648
        else:
            return ans

if __name__ == "__main__":
    s = Solution().divide(-22, -1)
    print(s)


