# -*- coding:utf-8 -*-


# English:
# Write a function that takes a string as input and reverse only the vowels of a string.
# Example 1:
# Input: "hello" Output: "holle"
# Example 2:
# Input: "leetcode" Output: "leotcede"
# Note:
# The vowels does not include the letter "y".
#
# 中文:
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 示例 1:
# 输入: "hello" 输出: "holle"
# 示例 2:
# 输入: "leetcode" 输出: "leotcede"
# 说明:
# 元音字母不包含字母"y"。


#
# @lc app=leetcode.cn id=345 lang=python
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (46.01%)
# Total Accepted:    7.7K
# Total Submissions: 16.6K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
#
#
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
#
# 说明:
# 元音字母不包含字母"y"。
#
#


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        string_list = list(s)
        vowels_list = [i for i, e in enumerate(s) if e in 'aeiouAEIOU']
        i = 0
        while i < len(vowels_list)/2:
            string_list[vowels_list[i]], string_list[vowels_list[-i-1]] = string_list[vowels_list[-i-1]], string_list[vowels_list[i]]
            i += 1
        return ''.join(string_list)

