# -*- coding:utf-8 -*-


# English:
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"] Output: ["Alaska","Dad"]
# Example 2:
# Input: words = ["omk"] Output: []
# Example 3:
# Input: words = ["adsdf","sfd"] Output: ["adsdf","sfd"]
# Constraints:
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase).
#
# 中文:
# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。
# 美式键盘 中：
# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。
# 示例 1：
# 输入：words = ["Hello","Alaska","Dad","Peace"] 输出：["Alaska","Dad"]
# 示例 2：
# 输入：words = ["omk"] 输出：[]
# 示例 3：
# 输入：words = ["adsdf","sfd"] 输出：["adsdf","sfd"]
# 提示：
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] 由英文字母（小写和大写字母）组成


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

