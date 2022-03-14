# -*- coding:utf-8 -*-


# English:
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
# Input: s = "cbaebabacd", p = "abc" Output: [0,6] Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc". The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
# Input: s = "abab", p = "ab" Output: [0,1,2] Explanation: The substring with start index = 0 is "ab", which is an anagram of "ab". The substring with start index = 1 is "ba", which is an anagram of "ab". The substring with start index = 2 is "ab", which is an anagram of "ab".
# Constraints:
# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.
#
# 中文:
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
# 示例 1:
# 输入: s = "cbaebabacd", p = "abc" 输出: [0,6] 解释: 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 示例 2:
# 输入: s = "abab", p = "ab" 输出: [0,1,2] 解释: 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
# 提示:
# 1 <= s.length, p.length <= 3 * 104
# s 和 p 仅包含小写字母


#
# @lc app=leetcode.cn id=438 lang=python
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (36.76%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 15K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
#
#
# 示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
# 示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#
#
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 动态规划的思想, 记录每个状态, 但是状态很多冗余的, 而且判断相等的效率低
        # from collections import Counter

        # def check(idx):
        #     if idx < len(p)-1:
        #         return False
        #     a, b = f[idx-len(p)], f[idx]
        #     for k, v in cnt.items():
        #         if v != (b.get(k, 0)-a.get(k, 0)):
        #             return False
        #     return True

        # ans = []
        # f = {-1:{}}
        # cnt = Counter(p)
        # for idx, i in enumerate(s):
        #     f[idx] = f[idx-1].copy()
        #     f[idx][i] = f[idx].get(i, 0) + 1
        #     if check(idx):
        #         ans.append(idx-len(p)+1)
        # return ans

        ans = []
        s_status = [0 for _ in range(26)]
        p_status = [0 for _ in range(26)]

        for i in p:
            p_status[ord(i)-97] += 1
        for i in s[:len(p)]:
            s_status[ord(i)-97] += 1
        if s_status == p_status:
            ans.append(0)
        for idx, i in enumerate(s[len(p):]):
            s_status[ord(s[idx])-97] -= 1
            s_status[ord(i)-97] += 1
            if s_status == p_status:
                ans.append(idx+1)
        return ans

if __name__ == "__main__":
    s = Solution().findAnagrams("cbaebabacd", "abc")
    print(s)
    s = Solution().findAnagrams("cba", "abc")
    print(s)
    s = Solution().findAnagrams("abab", "ab")
    print(s)


