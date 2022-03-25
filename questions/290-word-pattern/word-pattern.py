# -*- coding:utf-8 -*-

# <SUBID:15987083,UPDATE:20220325>
# English:
# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog" Output: true
# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish" Output: false
# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog" Output: false
# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
# 中文:
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 示例1:
# 输入: pattern = "abba", str = "dog cat cat dog" 输出: true
# 示例 2:
# 输入:pattern = "abba", str = "dog cat cat fish" 输出: false
# 示例 3:
# 输入: pattern = "aaaa", str = "dog cat cat dog" 输出: false
# 提示:
# 1 <= pattern.length <= 300
# pattern 只包含小写英文字母
# 1 <= s.length <= 3000
# s 只包含小写英文字母和 ' '
# s 不包含 任何前导或尾随对空格
# s 中每个单词都被 单个空格 分隔


#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词模式
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (36.97%)
# Total Accepted:    5.7K
# Total Submissions: 15K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
#
# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
#
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
#
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 示例 4:
#
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
#
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
#
#


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(set(pattern)) != len(set(words)):
            return False
        p_len = len(pattern)
        w_len = len(words)
        if p_len < 1 or w_len < 1 or p_len != w_len:
            return False
        for i in range(p_len-1):
            for j in range(i+1, p_len):
                if (pattern[j] == pattern[i] and words[j] != words[i]):
                    return False
        return True



