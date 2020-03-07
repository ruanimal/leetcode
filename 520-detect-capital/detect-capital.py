# -*- coding:utf-8 -*-


# English:
# Given a word, you need to judge whether the usage of capitals in it is right or not.
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
# Example 1:
# Input: "USA" Output: True
# Example 2:
# Input: "FlaG" Output: False
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
#
# 中文:
# 给定一个单词，你需要判断单词的大写使用是否正确。
# 我们定义，在以下情况时，单词的大写用法是正确的：
# 全部字母都是大写，比如"USA"。
# 单词中所有字母都不是大写，比如"leetcode"。
# 如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
# 否则，我们定义这个单词没有正确使用大写字母。
# 示例 1:
# 输入: "USA" 输出: True
# 示例 2:
# 输入: "FlaG" 输出: False
# 注意: 输入是由大写和小写拉丁字母组成的非空单词。


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

