# -*- coding:utf-8 -*-


# English:
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
# Example:
# Input: ["Hello", "Alaska", "Dad", "Peace"] Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
#
# 中文:
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
# 示例：
# 输入: ["Hello", "Alaska", "Dad", "Peace"] 输出: ["Alaska", "Dad"]
# 注意：
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。


#
# @lc app=leetcode.cn id=500 lang=python
#
# [500] 键盘行
#
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letters_map = {}
        for i in 'qwertyuiopQWERTYUIOP':
            letters_map[i] = 1
        for i in 'asdfghjklASDFGHJKL':
            letters_map[i] = 2
        for i in 'zxcvbnmZXCVBNM':
            letters_map[i] = 3
        ret = []
        for word in words:
            if len(set(letters_map[i] for i in word)) == 1:
                ret.append(word)
        return ret

if __name__ == "__main__":
    s = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(s)

