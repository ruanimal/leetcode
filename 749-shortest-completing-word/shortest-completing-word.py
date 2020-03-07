# -*- coding:utf-8 -*-


# English:
# Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate
# Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.
# It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.
# The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.
# Example 1:
#
# Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"] Output: "steps" Explanation: The smallest length word that contains the letters "S", "P", "S", and "T". Note that the answer is not "step", because the letter "s" must occur in the word twice. Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
# Example 2:
#
# Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"] Output: "pest" Explanation: There are 3 smallest length words that contains the letters "s". We return the one that occurred first.
# Note:
#
# licensePlate will be a string with length in range [1, 7].
# licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
# words will have a length in the range [10, 1000].
# Every words[i] will consist of lowercase letters, and have length in range [1, 15].
#
# 中文:
# 如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，那么我们称之为完整词。在所有完整词中，最短的单词我们称之为最短完整词。
# 单词在匹配牌照中的字母时不区分大小写，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。
# 我们保证一定存在一个最短完整词。当有多个单词都符合最短完整词的匹配条件时取单词列表中最靠前的一个。
# 牌照中可能包含多个相同的字符，比如说：对于牌照 "PP"，单词 "pair" 无法匹配，但是 "supper" 可以匹配。
# 示例 1：
# 输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"] 输出："steps" 说明：最短完整词应该包括 "s"、"p"、"s" 以及 "t"。对于 "step" 它只包含一个 "s" 所以它不符合条件。同时在匹配过程中我们忽略牌照中的大小写。
# 示例 2：
# 输入：licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"] 输出："pest" 说明：存在 3 个包含字母 "s" 且有着最短长度的完整词，但我们返回最先出现的完整词。
# 注意:
# 牌照（licensePlate）的长度在区域[1, 7]中。
# 牌照（licensePlate）将会包含数字、空格、或者字母（大写和小写）。
# 单词列表（words）长度在区间 [10, 1000] 中。
# 每一个单词 words[i] 都是小写，并且长度在区间 [1, 15] 中。


#
# @lc app=leetcode.cn id=748 lang=python
#
# [748] 至少是其他数字两倍的最大数
#
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letter = {}
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()
                letter[i] = letter.get(i, 0) + 1
        letter_len = sum(letter.values())
        ans = None
        for word in words:
            tmp = {}
            for i in word:
                tmp[i] = tmp.get(i, 0) + 1
            for k, v in letter.items():
                if k not in tmp:
                    break
                if tmp[k] < v:
                    break
            else:
                if not ans:
                    ans = word
                if len(word) < len(ans):
                    ans = word
                if len(ans) == letter_len:
                    return ans
        return ans

if __name__ == "__main__":
    s = Solution().shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"])
    print(s)


