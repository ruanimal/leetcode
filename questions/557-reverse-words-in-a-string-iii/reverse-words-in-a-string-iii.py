# -*- coding:utf-8 -*-


# English:
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:
# Input: s = "Let's take LeetCode contest" Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "God Ding" Output: "doG gniD"
# Constraints:
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.
#
# 中文:
# 给定一个字符串
# s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 示例 1：
# 输入：s = "Let's take LeetCode contest" 输出："s'teL ekat edoCteeL tsetnoc"
# 示例 2:
# 输入： s = "God Ding" 输出："doG gniD"
# 提示：
# 1 <= s.length <= 5 * 104
# s 包含可打印的 ASCII 字符。
# s 不包含任何开头或结尾空格。
# s 里 至少 有一个词。
# s 中的所有单词都用一个空格隔开。


#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ret = []
        # pre_i = i = 0
        # while i < len(s):
        #     if s[i] == ' ':
        #         ret.append(s[pre_i:i][::-1])
        #         pre_i = i+1
        #     i += 1
        # ret.append(s[pre_i:i][::-1])
        # return ' '.join(ret)
        return ' '.join(i[::-1] for i in s.split())

if __name__ == "__main__":
    s = Solution().reverseWords("Let's take LeetCode contest")
    print(s)


