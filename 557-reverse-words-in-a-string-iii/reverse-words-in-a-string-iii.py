# -*- coding:utf-8 -*-


# English:
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
# Example 1:
#
# Input: "Let's take LeetCode contest" Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
#
# 中文:
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# 示例 1:
# 输入: "Let's take LeetCode contest" 输出: "s'teL ekat edoCteeL tsetnoc"
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。


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


