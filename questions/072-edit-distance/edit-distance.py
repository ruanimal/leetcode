# -*- coding:utf-8 -*-

# <SUBID:20329713,UPDATE:20220325>
# English:
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character
# Example 1:
# Input: word1 = "horse", word2 = "ros" Output: 3 Explanation: horse -> rorse (replace 'h' with 'r') rorse -> rose (remove 'r') rose -> ros (remove 'e')
# Example 2:
# Input: word1 = "intention", word2 = "execution" Output: 5 Explanation: intention -> inention (remove 't') inention -> enention (replace 'i' with 'e') enention -> exention (replace 'n' with 'x') exention -> exection (replace 'n' with 'c') exection -> execution (insert 'u')
# Constraints:
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
#
# 中文:
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
# 你可以对一个单词进行如下三种操作：
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 示例 1：
# 输入：word1 = "horse", word2 = "ros" 输出：3 解释： horse -> rorse (将 'h' 替换为 'r') rorse -> rose (删除 'r') rose -> ros (删除 'e')
# 示例 2：
# 输入：word1 = "intention", word2 = "execution" 输出：5 解释： intention -> inention (删除 't') inention -> enention (将 'i' 替换为 'e') enention -> exention (将 'n' 替换为 'x') exention -> exection (将 'n' 替换为 'c') exection -> execution (插入 'u')
# 提示：
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成


#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (49.68%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 14K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2:
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        f[i][j] word1前i个字符变成word2的前j个字符需要的最小步数
        word1[i] == word2[j]:
            f[i][j]: f[i-1][j-1]
        word1[i] != word2[j]:
            min(f[i-1][j], f[i+1][j], f[i-1][j-1]) + 1
        """
        m, n = len(word1), len(word2)
        f = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            f[i][0] = i
        for j in range(n+1):
            f[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
        return f[m][n]


if __name__ == "__main__":
    s = Solution().minDistance(word1 = "horse", word2 = "ros")
    print(s)



