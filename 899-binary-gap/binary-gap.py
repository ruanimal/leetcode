# -*- coding:utf-8 -*-


# English:
# Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.
# If there aren't two consecutive 1's, return
# 0
# .
# Example 1:
# Input: 22 Output: 2 Explanation: 22 in binary is 0b10110. In the binary representation of 22, there are three ones, and two consecutive pairs of 1's. The first consecutive pair of 1's have distance 2. The second consecutive pair of 1's have distance 1. The answer is the largest of these two distances, which is 2.
# Example 2:
# Input: 5 Output: 2 Explanation: 5 in binary is 0b101.
# Example 3:
# Input: 6 Output: 1 Explanation: 6 in binary is 0b110.
# Example 4:
# Input: 8 Output: 0 Explanation: 8 in binary is 0b1000. There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
# Note:
# 1 <= N <= 10^9
#
# 中文:
# 给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。
# 如果没有两个连续的 1，返回 0 。
# 示例 1：
# 输入：22 输出：2 解释： 22 的二进制是 0b10110 。 在 22 的二进制表示中，有三个 1，组成两对连续的 1 。 第一对连续的 1 中，两个 1 之间的距离为 2 。 第二对连续的 1 中，两个 1 之间的距离为 1 。 答案取两个距离之中最大的，也就是 2 。
# 示例 2：
# 输入：5 输出：2 解释： 5 的二进制是 0b101 。
# 示例 3：
# 输入：6 输出：1 解释： 6 的二进制是 0b110 。
# 示例 4：
# 输入：8 输出：0 解释： 8 的二进制是 0b1000 。 在 8 的二进制表示中没有连续的 1，所以返回 0 。
# 提示：
# 1 <= N <= 10^9


#
# @lc app=leetcode.cn id=868 lang=python
#
# [868] 二进制间距
#
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        pre1 = None
        index = 0
        while N:
            if N & 1 == 1:
                if pre1 is None:
                    pre1 = index
                ans = max(index-pre1, ans)
                pre1 = index
            index += 1
            N = N >> 1
        return ans

if __name__ == "__main__":
    s = Solution().binaryGap(22)
    print(s)

