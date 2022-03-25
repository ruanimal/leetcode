# -*- coding:utf-8 -*-

# <SUBID:17422477,UPDATE:20220325>
# English:
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Example 1:
# Input: n = 2 Output: [0,1,1] Explanation: 0 --> 0 1 --> 1 2 --> 10
# Example 2:
# Input: n = 5 Output: [0,1,1,2,1,2] Explanation: 0 --> 0 1 --> 1 2 --> 10 3 --> 11 4 --> 100 5 --> 101
# Constraints:
# 0 <= n <= 105
# Follow up:
# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
#
# 中文:
# 给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。
# 示例 1：
# 输入：n = 2 输出：[0,1,1] 解释： 0 --> 0 1 --> 1 2 --> 10
# 示例 2：
# 输入：n = 5 输出：[0,1,1,2,1,2] 解释： 0 --> 0 1 --> 1 2 --> 10 3 --> 11 4 --> 100 5 --> 101
# 提示：
# 0 <= n <= 105
# 进阶：
# 很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
# 你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）


#
# @lc app=leetcode.cn id=338 lang=python
#
# [338] 比特位计数
#
# https://leetcode-cn.com/problems/counting-bits/description/
#
# algorithms
# Medium (70.63%)
# Total Accepted:    7.2K
# Total Submissions: 10.2K
# Testcase Example:  '2'
#
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,1]
#
# 示例 2:
#
# 输入: 5
# 输出: [0,1,1,2,1,2]
#
# 进阶:
#
#
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
#
#
#
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        1. f[x]: 数字x的1的个数; 数字x一共有n位,最后一位是0和不是0
        2. f[x] = f[x>>1] if (i&1 == 0) else f[x>>1]; 也就是 f[x] = f[x>>1] + (x&1)
        """
        f = [0, 1]
        for x in range(2, num+1):
            f.append(None)
            f[x] = f[x>>1] + (x&1)
        return f[:num+1]

if __name__ == "__main__":
    s = Solution().countBits(5)
    print(s)

