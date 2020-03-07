# -*- coding:utf-8 -*-


# English:
# Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
# The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
# Example 1:
#
# Input: "aba", "cdc" Output: 3 Explanation: The longest uncommon subsequence is "aba" (or "cdc"),
# because "aba" is a subsequence of "aba",
# but not a subsequence of any other strings in the group of two strings.
# Note:
# Both strings' lengths will not exceed 100.
# Only letters from a ~ z will appear in input strings.
#
# 中文:
# 给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
# 子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。
# 输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。
# 示例 :
# 输入: "aba", "cdc" 输出: 3 解析: 最长特殊序列可为 "aba" (或 "cdc")
# 说明:
# 两个字符串长度均小于100。
# 字符串中的字符仅含有 'a'~'z'。


#
# @lc app=leetcode.cn id=521 lang=python
#
# [521] 最长特殊序列 Ⅰ
#
# 给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

# 子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。

# 输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。

# 示例 :

# 输入: "aba", "cdc"
# 输出: 3
# 解析: 最长特殊序列可为 "aba" (或 "cdc")
# 说明:

# 两个字符串长度均小于100。
# 字符串中的字符仅含有 'a'~'z'。
# - 注意题目中的独有两个字，
# - s1 = 'ab',s2 = 'a',因为ab是s1独有，所以最长子序列为ab，
# - s1 = 'ab', s2 = 'ab', 因为ab是两个串都有，ab排除，a也是两个串都有，排除，b也是两个串都有，排除。所以最长特殊序列不存在，返回-1
# - 通过以上分析，我们可以得出结论，如果：两个串相等（不仅长度相等，内容也相等），那么他们的最长特殊序列不存在。返回-1
# - 如果两个串长度不一样，那么长的串   永远也不可能是   短串的子序列，即len(s1) > len(s2),则最长特殊序列为s1,返回长度大的数

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b :
            return -1
        return max(len(a),len(b))


