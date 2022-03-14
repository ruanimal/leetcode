# -*- coding:utf-8 -*-


# English:
# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
# Example 1:
# Input: words = ["w","wo","wor","worl","world"] Output: "world" Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input: words = ["a","banana","app","appl","ap","apply","apple"] Output: "apple" Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 30
# words[i] consists of lowercase English letters.
#
# 中文:
# 给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。
# 若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。
# 示例 1：
# 输入：words = ["w","wo","wor","worl", "world"] 输出："world" 解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。
# 示例 2：
# 输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"] 输出："apple" 解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply"
# 提示：
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 30
# 所有输入的字符串 words[i] 都只包含小写字母。


#
# @lc app=leetcode.cn id=720 lang=python
#
# [720] 词典中最长的单词
#
# https://leetcode-cn.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (39.28%)
# Total Accepted:    1.8K
# Total Submissions: 4.5K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
#
# 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
#
# 若无答案，则返回空字符串。
#
# 示例 1:
#
#
# 输入:
# words = ["w","wo","wor","worl", "world"]
# 输出: "world"
# 解释:
# 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
#
#
# 示例 2:
#
#
# 输入:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出: "apple"
# 解释:
# "apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
#
#
# 注意:
#
#
# 所有输入的字符串都只包含小写字母。
# words数组长度范围为[1,1000]。
# words[i]的长度范围为[1,30]。
#
#
#

class node:
    def __init__(self,key, hasKey = False):
        self.key = key
        self.children = {}
        self.hasKey = hasKey

    def __repr__(self):
        return 'Node(%r, %r) -> %r' % (self.key, self.hasKey, self.children)

class trie:
    def __init__(self):
        self.root = node('')
        self.root.hasKey = True

    def insert(self,word):
        nd = self.root  # 树节点
        for c in word:
            if c not in nd.children:
                nd.children[c] = node(c)
            nd = nd.children[c]
        nd.hasKey = True   # 这个节点有单词

    def __repr__(self):
        return repr(self.root)

class Solution:
    def getWord(self, nd):
        if not nd.hasKey:
            return []  # 这个节点本身没有单词, 只是在路径上
        if not nd.children:
            return [nd.key]  # 只有一个字母, 没有只节点
        li = [self.getWord(n) for n in nd.children.values()]  # 把某个节点往下的所有单词取出来
        n = len(max(li,key=len))  # 求最长的单词的长度
        li = [i for i in li if len(i)==n]
        li.sort()
        return [nd.key]+li[0]

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        tr = trie()
        for word in words:
            tr.insert(word)
        return ''.join(self.getWord(tr.root))


if __name__ == "__main__":
    # from pprint import pprint as print
    # data = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    data = ["a", "ba", "app"]
    s = Solution().longestWord(data)
    print(s)
    # tr = trie()
    # for word in data:
    #     tr.insert(word)
    # print(tr)

