# -*- coding:utf-8 -*-


# English:
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.
# Example 1:
# Input: word = "USA" Output: true
# Example 2:
# Input: word = "FlaG" Output: false
# Constraints:
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.
#
# 中文:
# 我们定义，在以下情况时，单词的大写用法是正确的：
# 全部字母都是大写，比如 "USA" 。
# 单词中所有字母都不是大写，比如 "leetcode" 。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
# 给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：word = "USA" 输出：true
# 示例 2：
# 输入：word = "FlaG" 输出：false
# 提示：
# 1 <= word.length <= 100
# word 由小写和大写英文字母组成


#
# @lc app=leetcode.cn id=520 lang=python
#
# [520] 检测大写字母
#
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if word[0].islower():
            return word[1:].islower()
        if word[1:].isupper() or word[1:].islower():
            return True
        return False

if __name__ == "__main__":
    s = Solution().detectCapitalUse('USA')
    print(s)
    s = Solution().detectCapitalUse('Leetcode')
    print(s)

