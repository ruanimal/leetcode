# -*- coding:utf-8 -*-

# <SUBID:17978521,UPDATE:20220325>
# English:
# Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If the longest uncommon subsequence does not exist, return -1.
# An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "a
# e
# b
# d
# c" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
# Example 1:
# Input: a = "aba", b = "cdc" Output: 3 Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc". Note that "cdc" is also a longest uncommon subsequence.
# Example 2:
# Input: a = "aaa", b = "bbb" Output: 3 Explanation: The longest uncommon subsequences are "aaa" and "bbb".
# Example 3:
# Input: a = "aaa", b = "aaa" Output: -1 Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a.
# Constraints:
# 1 <= a.length, b.length <= 100
# a and b consist of lower-case English letters.
#
# 中文:
# 给你两个字符串 a 和 b，请返回 这两个字符串中 最长的特殊序列  的长度。如果不存在，则返回 -1 。
# 「最长特殊序列」 定义如下：该序列为 某字符串独有的最长子序列（即不能是其他字符串的子序列） 。
# 字符串 s 的子序列是在从 s 中删除任意数量的字符后可以获得的字符串。
# 例如，"abc" 是 "aebdc" 的子序列，因为删除 "aebdc" 中斜体加粗的字符可以得到 "abc" 。 "aebdc" 的子序列还包括 "aebdc" 、 "aeb" 和 "" (空字符串)。
# 示例 1：
# 输入: a = "aba", b = "cdc" 输出: 3 解释: 最长特殊序列可为 "aba" (或 "cdc")，两者均为自身的子序列且不是对方的子序列。
# 示例 2：
# 输入：a = "aaa", b = "bbb" 输出：3 解释: 最长特殊序列是 "aaa" 和 "bbb" 。
# 示例 3：
# 输入：a = "aaa", b = "aaa" 输出：-1 解释: 字符串 a 的每个子序列也是字符串 b 的每个子序列。同样，字符串 b 的每个子序列也是字符串 a 的子序列。
# 提示：
# 1 <= a.length, b.length <= 100
# a 和 b 由小写英文字母组成


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


