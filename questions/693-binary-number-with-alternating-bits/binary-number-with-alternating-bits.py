# -*- coding:utf-8 -*-

# <SUBID:319261497,UPDATE:20230205>
# English:
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
# Example 1:
# Input: n = 5 Output: true Explanation: The binary representation of 5 is: 101
# Example 2:
# Input: n = 7 Output: false Explanation: The binary representation of 7 is: 111.
# Example 3:
# Input: n = 11 Output: false Explanation: The binary representation of 11 is: 1011.
# Constraints:
# 1 <= n <= 231 - 1
#
# 中文:
# 给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。
# 示例 1：
# 输入：n = 5 输出：true 解释：5 的二进制表示是：101
# 示例 2：
# 输入：n = 7 输出：false 解释：7 的二进制表示是：111.
# 示例 3：
# 输入：n = 11 输出：false 解释：11 的二进制表示是：1011.
# 提示：
# 1 <= n <= 231 - 1


#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#
# https://leetcode-cn.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (59.63%)
# Total Accepted:    5.1K
# Total Submissions: 8.6K
# Testcase Example:  '5'
#
# 给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
#
# 示例 1:
#
#
# 输入: 5
# 输出: True
# 解释:
# 5的二进制数是: 101
#
#
# 示例 2:
#
#
# 输入: 7
# 输出: False
# 解释:
# 7的二进制数是: 111
#
#
# 示例 3:
#
#
# 输入: 11
# 输出: False
# 解释:
# 11的二进制数是: 1011
#
#
# 示例 4:
#
#
# 输入: 10
# 输出: True
# 解释:
# 10的二进制数是: 1010
#
#
#
class SolutionA:
    bits = [2**i for i in range(32)]
    def hasAlternatingBits(self, n: int) -> bool:
        """模拟法
        """
        pre = None
        for i in self.bits:
            if i > n:
                break
            if (n & i) == i:
                bit = 1
            else:
                bit = 0
            if pre is None:
                pre = bit
                continue
            else:
                if not (bit ^ pre):
                    return False
            pre = bit
        return True

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre = None
        while n > 0:
            bit = n & 1
            if bit == pre:
                return False
            n >>= 1
            pre = bit
        return True

if __name__ == "__main__":
    s = Solution().hasAlternatingBits(5)
    print(s)
    s = Solution().hasAlternatingBits(4)
    print(s)

