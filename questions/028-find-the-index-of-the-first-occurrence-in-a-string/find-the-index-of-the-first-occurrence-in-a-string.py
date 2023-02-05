# -*- coding:utf-8 -*-

# <SUBID:302674425,UPDATE:20230205>
# English:
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad" Output: 0 Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.
# Example 2:
# Input: haystack = "leetcode", needle = "leeto" Output: -1 Explanation: "leeto" did not occur in "leetcode", so we return -1.
# Constraints:
# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
#
# 中文:
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
# 示例 1：
# 输入：haystack = "sadbutsad", needle = "sad" 输出：0 解释："sad" 在下标 0 和 6 处匹配。 第一个匹配项的下标是 0 ，所以返回 0 。
# 示例 2：
# 输入：haystack = "leetcode", needle = "leeto" 输出：-1 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
# 提示：
# 1 <= haystack.length, needle.length <= 104
# haystack 和 needle 仅由小写英文字符组成


#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (37.60%)
# Total Accepted:    44.1K
# Total Submissions: 116.2K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
#
#
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
#
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        for i in range(0, len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

