# -*- coding:utf-8 -*-

# <SUBID:18775636,UPDATE:20220325>
# English:
# Given a string licensePlate and an array of strings words, find the shortest completing word in words.
# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".
# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.
# Example 1:
# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"] Output: "steps" Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'. "step" contains 't' and 'p', but only contains 1 's'. "steps" contains 't', 'p', and both 's' characters. "stripe" is missing an 's'. "stepple" is missing an 's'. Since "steps" is the only word containing all the letters, that is the answer.
# Example 2:
# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"] Output: "pest" Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
# Constraints:
# 1 <= licensePlate.length <= 7
# licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 15
# words[i] consists of lower case English letters.
#
# 中文:
# 给你一个字符串 licensePlate 和一个字符串数组 words ，请你找出 words 中的 最短补全词 。
# 补全词 是一个包含 licensePlate 中所有字母的单词。忽略 licensePlate 中的 数字和空格 。不区分大小写。如果某个字母在 licensePlate 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。
# 例如：licensePlate = "aBc 12c"，那么它的补全词应当包含字母 'a'、'b' （忽略大写）和两个 'c' 。可能的 补全词 有 "abccdef"、"caaacab" 以及 "cbca" 。
# 请返回 words 中的 最短补全词 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 words 中 第一个 出现的那个。
# 示例 1：
# 输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"] 输出："steps" 解释：最短补全词应该包括 "s"、"p"、"s"（忽略大小写） 以及 "t"。 "step" 包含 "t"、"p"，但只包含一个 "s"，所以它不符合条件。 "steps" 包含 "t"、"p" 和两个 "s"。 "stripe" 缺一个 "s"。 "stepple" 缺一个 "s"。 因此，"steps" 是唯一一个包含所有字母的单词，也是本例的答案。
# 示例 2：
# 输入：licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"] 输出："pest" 解释：licensePlate 只包含字母 "s" 。所有的单词都包含字母 "s" ，其中 "pest"、"stew"、和 "show" 三者最短。答案是 "pest" ，因为它是三个单词中在 words 里最靠前的那个。
# 提示：
# 1 <= licensePlate.length <= 7
# licensePlate 由数字、大小写字母或空格 ' ' 组成
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 15
# words[i] 由小写英文字母组成


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


