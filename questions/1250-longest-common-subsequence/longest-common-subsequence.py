# -*- coding:utf-8 -*-

# <SUBID:334087224,UPDATE:20230205>
# English:
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
# Example 1:
# Input: text1 = "abcde", text2 = "ace" Output: 3 Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:
# Input: text1 = "abc", text2 = "abc" Output: 3 Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
# Input: text1 = "abc", text2 = "def" Output: 0 Explanation: There is no such common subsequence, so the result is 0.
# Constraints:
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
#
# 中文:
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
# 示例 1：
# 输入：text1 = "abcde", text2 = "ace" 输出：3 解释：最长公共子序列是 "ace" ，它的长度为 3 。
# 示例 2：
# 输入：text1 = "abc", text2 = "abc" 输出：3 解释：最长公共子序列是 "abc" ，它的长度为 3 。
# 示例 3：
# 输入：text1 = "abc", text2 = "def" 输出：0 解释：两个字符串没有公共子序列，返回 0 。
# 提示：
# 1 <= text1.length, text2.length <= 1000
# text1 和 text2 仅由小写英文字符组成。


from collections import deque
class SolutionA:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """转化成最长递增只序列
        从text2中找出text1中的每个字符出现的索引, 求索引数组的递增子序列
        不能存在多个字符串时, 有多种选择的问题
        """

        if len(text1) > len(text2):
            text1, text2 = text2, text1

        index_map = {}
        for idx, e in enumerate(text2):
            index_map.setdefault(e, deque()).append(idx)

        found = []
        for i in text1:
            if len(index_map.get(i, [])) > 0:
                print(i)
                found.append(index_map[i].popleft())
        print(found)
        if len(found) == 0:  # 防止没有重复元素的情况
            return 0

        dp = [1 for _ in found]
        for i in range(1, len(found)):
            for j in range(i):
                if found[i] > found[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """转化成求编辑距离
        """

        m, n = len(text1), len(text2)
        f = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1])
        return f[m][n]

