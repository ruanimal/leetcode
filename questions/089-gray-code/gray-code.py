# -*- coding:utf-8 -*-

# <SUBID:21364462,UPDATE:20220325>
# English:
# An n-bit gray code sequence is a sequence of 2n integers where:
# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.
# Example 1:
# Input: n = 2 Output: [0,1,3,2] Explanation: The binary representation of [0,1,3,2] is [00,01,11,10]. - 0
# 0
# and 0
# 1
# differ by one bit -
# 0
# 1 and
# 1
# 1 differ by one bit - 1
# 1
# and 1
# 0
# differ by one bit -
# 1
# 0 and
# 0
# 0 differ by one bit [0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01]. -
# 0
# 0 and
# 1
# 0 differ by one bit - 1
# 0
# and 1
# 1
# differ by one bit -
# 1
# 1 and
# 0
# 1 differ by one bit - 0
# 1
# and 0
# 0
# differ by one bit
# Example 2:
# Input: n = 1 Output: [0,1]
# Constraints:
# 1 <= n <= 16
#
# 中文:
# n 位格雷码序列 是一个由 2n 个整数组成的序列，其中：
# 每个整数都在范围 [0, 2n - 1] 内（含 0 和 2n - 1）
# 第一个整数是 0
# 一个整数在序列中出现 不超过一次
# 每对 相邻 整数的二进制表示 恰好一位不同 ，且
# 第一个 和 最后一个 整数的二进制表示 恰好一位不同
# 给你一个整数 n ，返回任一有效的 n 位格雷码序列 。
# 示例 1：
# 输入：n = 2 输出：[0,1,3,2] 解释： [0,1,3,2] 的二进制表示是 [00,01,11,10] 。 - 00 和 01 有一位不同 - 01 和 11 有一位不同 - 11 和 10 有一位不同 - 10 和 00 有一位不同 [0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。 - 00 和 10 有一位不同 - 10 和 11 有一位不同 - 11 和 01 有一位不同 - 01 和 00 有一位不同
# 示例 2：
# 输入：n = 1 输出：[0,1]
# 提示：
# 1 <= n <= 16


#
# @lc app=leetcode.cn id=89 lang=python
#
# [89] 格雷编码
#
# https://leetcode-cn.com/problems/gray-code/description/
#
# algorithms
# Medium (64.25%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    7.7K
# Total Submissions: 11.9K
# Testcase Example:  '2'
#
# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
#
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
# 示例 2:
#
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
# 给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
# 因此，当 n = 0 时，其格雷编码序列为 [0]。
#
#
#
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        ans = [0, 1]
        for i in range(2, n+1):
            tmp = 2 ** (i-1)
            ans = ans + [(x | tmp) for x in ans[::-1]]
        # print([bin(i) for i in ans])
        return ans

if __name__ == "__main__":
    s = Solution().grayCode(2)
    print(s)
    s = Solution().grayCode(3)
    print(s)


