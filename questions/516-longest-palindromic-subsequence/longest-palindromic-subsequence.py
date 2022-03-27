# -*- coding:utf-8 -*-

# <SUBID:290292196,UPDATE:20220328>
# English:
# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
# Example 1:
# Input: s = "bbbab" Output: 4 Explanation: One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input: s = "cbbd" Output: 2 Explanation: One possible longest palindromic subsequence is "bb".
# Constraints:
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
#
# 中文:
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
# 示例 1：
# 输入：s = "bbbab" 输出：4 解释：一个可能的最长回文子序列为 "bbbb" 。
# 示例 2：
# 输入：s = "cbbd" 输出：2 解释：一个可能的最长回文子序列为 "bb" 。
# 提示：
# 1 <= s.length <= 1000
# s 仅由小写英文字母组成


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        dp[i][j] s[i:j+1] 的最长子序列长度
        则
            s[i] == s[j] => dp[i+1][j-1] + 2
            s[i] != s[j] => max(dp[i+1][j], dp[i][j-1])
        """

        length = len(s)
        if length <= 1:
            return length

        dp = [[0] * length for _ in range(length)]
        for x in range(length-1, -1, -1):
            dp[x][x] = 1
            for y in range(x+1, length):
                if s[x] == s[y]:
                    dp[x][y] = dp[x+1][y-1] + 2
                else:
                    dp[x][y] = max(dp[x+1][y], dp[x][y-1])

        # print(dp)
        return dp[0][length-1]

