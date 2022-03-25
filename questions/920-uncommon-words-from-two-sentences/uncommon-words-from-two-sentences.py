# -*- coding:utf-8 -*-

# <SUBID:18591919,UPDATE:20220325>
# English:
# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour" Output: ["sweet","sour"]
# Example 2:
# Input: s1 = "apple apple", s2 = "banana" Output: ["banana"]
# Constraints:
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
#
# 中文:
# 句子 是一串由空格分隔的单词。每个 单词 仅由小写字母组成。
# 如果某个单词在其中一个句子中恰好出现一次，在另一个句子中却 没有出现 ，那么这个单词就是 不常见的 。
# 给你两个 句子 s1 和 s2 ，返回所有 不常用单词 的列表。返回列表中单词可以按 任意顺序 组织。
# 示例 1：
# 输入：s1 = "this apple is sweet", s2 = "this apple is sour" 输出：["sweet","sour"]
# 示例 2：
# 输入：s1 = "apple apple", s2 = "banana" 输出：["banana"]
# 提示：
# 1 <= s1.length, s2.length <= 200
# s1 和 s2 由小写英文字母和空格组成
# s1 和 s2 都不含前导或尾随空格
# s1 和 s2 中的所有单词间均由单个空格分隔


#
# @lc app=leetcode.cn id=884 lang=python
#
# [884] 两句话中的不常见单词
#
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counts_map = {}
        for i in A.split():
            counts_map[i] = counts_map.get(i, 0) + 1
        for i in B.split():
            counts_map[i] = counts_map.get(i, 0) + 1
        return [k for k, v in counts_map.items() if v==1]

if __name__ == "__main__":
    s = Solution().uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour")
    print(s)

