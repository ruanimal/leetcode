# -*- coding:utf-8 -*-


# English:
# Given two integers a and b, return the sum of the two integers without using the operators + and -.
# Example 1:
# Input: a = 1, b = 2 Output: 3
# Example 2:
# Input: a = 2, b = 3 Output: 5
# Constraints:
# -1000 <= a, b <= 1000
#
# 中文:
# 给你两个整数 a 和 b ，不使用 运算符 + 和 -  ，计算并返回两整数之和。
# 示例 1：
# 输入：a = 1, b = 2 输出：3
# 示例 2：
# 输入：a = 2, b = 3 输出：5
# 提示：
# -1000 <= a, b <= 1000


#
# @lc app=leetcode.cn id=371 lang=python
#
# [371] 两整数之和
#
# https://leetcode-cn.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (57.56%)
# Total Accepted:    8.7K
# Total Submissions: 16.3K
# Testcase Example:  '1\n2'
#
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
#
# 示例 1:
#
# 输入: a = 1, b = 2
# 输出: 3
#
#
# 示例 2:
#
# 输入: a = -2, b = 3
# 输出: 1
#
#
class Solution(object):
    def getSum1(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        半加器就是2bit的异或
        通过两个半加器实现全加器
        https://blog.csdn.net/mote0714/article/details/42292299
        """

        def half_adder(a, b):
            return (a & b), (a ^ b)

        def full_adder(a, b, c):
            co, s = half_adder(a, b)
            co2, s2 = half_adder(c, s)
            return (co | co2), s2

        bit_a = 0   # 加法器参数a
        bit_b = 0   # 加法器参数b
        bit_c = 0   # 进位
        ret = 0
        count = 0
        while a > 0 or b >0:
            bit_a = a & 0b1
            bit_b = b & 0b1
            bit_c, s = full_adder(bit_a, bit_b, bit_c)
            ret = ret | (s << count)
            a = a >> 1
            b = b >> 1
            count += 1
        if bit_c:
            ret = ret | (bit_c << count)
        return ret

    def getSum(self, a, b):
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

if __name__ == "__main__":
    # import ipdb; ipdb.set_trace()
    s = Solution().getSum(-11,999)
    print(s)


