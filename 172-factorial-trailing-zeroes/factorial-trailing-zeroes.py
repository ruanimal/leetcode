# -*- coding:utf-8 -*-


# English:
# Given an integer n, return the number of trailing zeroes in n!.
# Example 1:
# Input: 3 Output: 0 Explanation: 3! = 6, no trailing zero.
# Example 2:
# Input: 5 Output: 1 Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.
#
# 中文:
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
# 示例 1:
# 输入: 3 输出: 0 解释: 3! = 6, 尾数中没有零。
# 示例 2:
# 输入: 5 输出: 1 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为 O(log n) 。


#
# @lc app=leetcode.cn id=172 lang=python
#
# [172] 阶乘后的零
#
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.93%)
# Likes:    127
# Dislikes: 0
# Total Accepted:    13K
# Total Submissions: 33.8K
# Testcase Example:  '3'
#
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例 1:
#
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
# 示例 2:
#
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
#
# 说明: 你算法的时间复杂度应为 O(log n) 。
#
#
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 太慢
        # ans = 0
        # for i in range(1, n+1):
        #     if i % 5 == 0:
        #         ans += 1
        # return ans
        '''
        >>> 2 * 5 * 10 * 12 * 15 * 20 * 22 * 25
        198000000
        # 2*5, 还有0本身, 构成了末尾的0
        # 就是看2和5有多少对, 因为2一定会在5之前出现, 有5肯定会有对应的2
        # 0 又肯定可以由2*5构成, 所以只要计算5的个数就够了
        '''
        ans = 0
        while n >= 5:
            ans += n // 5
            n //= 5
        return ans

