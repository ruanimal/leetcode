# -*- coding:utf-8 -*-

# <SUBID:19962513,UPDATE:20230205>
# English:
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# Example 1:
# Input: s = "egg", t = "add" Output: true
# Example 2:
# Input: s = "foo", t = "bar" Output: false
# Example 3:
# Input: s = "paper", t = "title" Output: true
# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.
#
# 中文:
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
# 示例 1:
# 输入：s = "egg", t = "add" 输出：true
# 示例 2：
# 输入：s = "foo", t = "bar" 输出：false
# 示例 3：
# 输入：s = "paper", t = "title" 输出：true
# 提示：
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成


#
# @lc app=leetcode.cn id=205 lang=python
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (43.13%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 25.5K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
#
# 输入: s = "egg", t = "add"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "foo", t = "bar"
# 输出: false
#
# 示例 3:
#
# 输入: s = "paper", t = "title"
# 输出: true
#
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
#
#
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tmp = {}
        for a, b in zip(s, t):
            tmp.setdefault(a, set()).add(b)
        tmp2 = []
        for k, i in tmp.items():
            if len(i) > 1:
                return False
            tmp2.extend(i)
        if len(tmp2) != len(set(tmp2)):
            return False
        return True

if __name__ == "__main__":
    s = Solution().isIsomorphic(s = "egg", t = "add")
    print(s)
    s = Solution().isIsomorphic(s = "ab", t = "aa")
    print(s)



