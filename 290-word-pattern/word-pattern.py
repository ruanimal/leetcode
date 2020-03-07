# -*- coding:utf-8 -*-


# English:
# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog" Output: true
# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish" Output: false
# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog" Output: false
# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog" Output: false
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
#
# 中文:
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 示例1:
# 输入: pattern = "abba", str = "dog cat cat dog" 输出: true
# 示例 2:
# 输入:pattern = "abba", str = "dog cat cat fish" 输出: false
# 示例 3:
# 输入: pattern = "aaaa", str = "dog cat cat dog" 输出: false
# 示例 4:
# 输入: pattern = "abba", str = "dog dog dog dog" 输出: false
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。


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



