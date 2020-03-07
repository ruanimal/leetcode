# -*- coding:utf-8 -*-


# English:
# Given two strings s and t , write a function to determine if t is an anagram of s.
# Example 1:
# Input: s = "anagram", t = "nagaram" Output: true
# Example 2:
# Input: s = "rat", t = "car" Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#
# 中文:
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 示例 1:
# 输入: s = "anagram", t = "nagaram" 输出: true
# 示例 2:
# 输入: s = "rat", t = "car" 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？


#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (50.01%)
# Total Accepted:    24.5K
# Total Submissions: 47.9K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl = [x for x in s]
        tl = [x for x in t]
        sl.sort()
        tl.sort()
        if sl == tl:
            return True
        else:
            return False

