# -*- coding:utf-8 -*-

# <SUBID:16353294,UPDATE:20220325>
# English:
# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.
# Example 1:
# Input: num = 5 Output: 2 Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
# Example 2:
# Input: num = 1 Output: 0 Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
# Constraints:
# 1 <= num < 231
# Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
#
# 中文:
# 对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。
# 例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
# 给你一个整数 num ，输出它的补数。
# 示例 1：
# 输入：num = 5 输出：2 解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
# 示例 2：
# 输入：num = 1 输出：0 解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
# 提示：
# 1 <= num < 231
# 注意：本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/ 相同


#
# @lc app=leetcode.cn id=476 lang=python
#
# [476] 数字的补数
#
# https://leetcode-cn.com/problems/number-complement/description/
#
# algorithms
# Easy (66.55%)
# Total Accepted:    8K
# Total Submissions: 12K
# Testcase Example:  '5'
#
# 给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。
#
# 注意:
#
#
# 给定的整数保证在32位带符号整数的范围内。
# 你可以假定二进制数不包含前导零位。
#
#
# 示例 1:
#
#
# 输入: 5
# 输出: 2
# 解释: 5的二进制表示为101（没有前导零位），其补数为010。所以你需要输出2。
#
#
# 示例 2:
#
#
# 输入: 1
# 输出: 0
# 解释: 1的二进制表示为1（没有前导零位），其补数为0。所以你需要输出0。
#
#
#
class Solution(object):
    bits = [2**i for i in range(32)]
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 0
        for i in Solution.bits:
            if i > num:
                break
            if (num & i) == i:
                continue
            else:
                # print(bin(ret))
                ret = ret | i
        return ret


if __name__ == "__main__":
    s = Solution().findComplement(5)
    print(s)


