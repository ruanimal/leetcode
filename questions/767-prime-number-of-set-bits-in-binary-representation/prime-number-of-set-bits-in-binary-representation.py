# -*- coding:utf-8 -*-

# <SUBID:319410045,UPDATE:20230205>
# English:
# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.
# Recall that the number of set bits an integer has is the number of 1's present when written in binary.
# For example, 21 written in binary is 10101, which has 3 set bits.
# Example 1:
# Input: left = 6, right = 10 Output: 4 Explanation: 6 -> 110 (2 set bits, 2 is prime) 7 -> 111 (3 set bits, 3 is prime) 8 -> 1000 (1 set bit, 1 is not prime) 9 -> 1001 (2 set bits, 2 is prime) 10 -> 1010 (2 set bits, 2 is prime) 4 numbers have a prime number of set bits.
# Example 2:
# Input: left = 10, right = 15 Output: 5 Explanation: 10 -> 1010 (2 set bits, 2 is prime) 11 -> 1011 (3 set bits, 3 is prime) 12 -> 1100 (2 set bits, 2 is prime) 13 -> 1101 (3 set bits, 3 is prime) 14 -> 1110 (3 set bits, 3 is prime) 15 -> 1111 (4 set bits, 4 is not prime) 5 numbers have a prime number of set bits.
# Constraints:
# 1 <= left <= right <= 106
# 0 <= right - left <= 104
#
# 中文:
# 给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。
# 计算置位位数 就是二进制表示中 1 的个数。
# 例如， 21 的二进制表示 10101 有 3 个计算置位。
# 示例 1：
# 输入：left = 6, right = 10 输出：4 解释： 6 -> 110 (2 个计算置位，2 是质数) 7 -> 111 (3 个计算置位，3 是质数) 9 -> 1001 (2 个计算置位，2 是质数) 10-> 1010 (2 个计算置位，2 是质数) 共计 4 个计算置位为质数的数字。
# 示例 2：
# 输入：left = 10, right = 15 输出：5 解释： 10 -> 1010 (2 个计算置位, 2 是质数) 11 -> 1011 (3 个计算置位, 3 是质数) 12 -> 1100 (2 个计算置位, 2 是质数) 13 -> 1101 (3 个计算置位, 3 是质数) 14 -> 1110 (3 个计算置位, 3 是质数) 15 -> 1111 (4 个计算置位, 4 不是质数) 共计 5 个计算置位为质数的数字。
# 提示：
# 1 <= left <= right <= 106
# 0 <= right - left <= 104


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        nums = {2,3,5,7,11,13,17,19}
        ret = 0
        for i in range(left, right+1):
            if self.swar(i) in nums:
                ret += 1
        return ret

    def swar(self, num):
        num = (num & 0x55555555) + ((num>>1) & 0x55555555)
        num = (num & 0x33333333) + ((num>>2) & 0x33333333)
        num = (num & 0x0f0f0f0f) + ((num>>4) & 0x0f0f0f0f)
        return ((num * 0x01010101) & 0xffffffff) >> 24
