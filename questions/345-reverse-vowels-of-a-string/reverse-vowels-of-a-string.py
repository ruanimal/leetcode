# -*- coding:utf-8 -*-

# <SUBID:314438336,UPDATE:20230205>
# English:
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# Example 1:
# Input: s = "hello" Output: "holle"
# Example 2:
# Input: s = "leetcode" Output: "leotcede"
# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.
#
# 中文:
# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。
# 示例 1：
# 输入：s = "hello" 输出："holle"
# 示例 2：
# 输入：s = "leetcode" 输出："leotcede"
# 提示：
# 1 <= s.length <= 3 * 105
# s 由 可打印的 ASCII 字符组成


#
# @lc app=leetcode.cn id=345 lang=python3
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


class SolutionA(object):
    def reverseVowels(self, s: str) -> str:
        """
        先找到元音的位置然后逐个交互
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

class Solution(object):
    vowels = set('aeiouAEIOU')

    def reverseVowels(self, s: str) -> str:
        """
        双指针
        """

        if len(s) < 2:
            return s
        tmp = list(s)
        i = 0
        j = len(tmp) - 1
        while i < j:
            if tmp[i] in self.vowels and tmp[j] in self.vowels:
                tmp[i], tmp[j] = tmp[j], tmp[i]
                i += 1
                j -= 1
            elif tmp[i] not in self.vowels:
                i += 1
            elif tmp[j] not in self.vowels:
                j -= 1
            else:
                i += 1
                j -= 1
        return ''.join(tmp)

s = Solution().reverseVowels('leetcode')
print(s)

