# -*- coding:utf-8 -*-


# English:
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.
# Example 1:
# Input: s = "aab" Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a" Output: [["a"]]
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.
#
# 中文:
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。
# 示例 1：
# 输入：s = "aab" 输出：[["a","a","b"],["aa","b"]]
# 示例 2：
# 输入：s = "a" 输出：[["a"]]
# 提示：
# 1 <= s.length <= 16
# s 仅由小写英文字母组成


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def vaild(a, b):
            b = b-1
            while a < b:
                if s[a] != s[b]:
                    return False
                a += 1
                b -= 1
            return True

        def backtrack(res, path, level):
            if level == length:
                path.append(length)
                if len(path) > 1 and vaild(path[-2], path[-1]):
                    res.append([s[path[i]:path[i+1]] for i in range(len(path)-1)])
                path.pop()
                return

            for i in [0, 1]:
                if i == 1:
                    if vaild(path[-1], level):
                        path.append(level)
                        backtrack(res, path, level+1)
                        path.pop()
                else:
                    backtrack(res, path, level+1)

        length = len(s)
        if length == 0:
            return []
        res = []
        backtrack(res, [0], 1)
        return res

