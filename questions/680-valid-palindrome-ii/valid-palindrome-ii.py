# -*- coding:utf-8 -*-

# <SUBID:319202918,UPDATE:20230205>
# English:
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
# Example 1:
# Input: s = "aba" Output: true
# Example 2:
# Input: s = "abca" Output: true Explanation: You could delete the character 'c'.
# Example 3:
# Input: s = "abc" Output: false
# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
#
# 中文:
# 给你一个字符串 s，最多 可以从中删除一个字符。
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：s = "aba" 输出：true
# 示例 2：
# 输入：s = "abca" 输出：true 解释：你可以删除字符 'c' 。
# 示例 3：
# 输入：s = "abc" 输出：false
# 提示：
# 1 <= s.length <= 105
# s 由小写英文字母组成


#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (30.11%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 16.4K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
#
#
# 输入: "aba"
# 输出: True
#
#
# 示例 2:
#
#
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#
#
# 注意:
#
#
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
#
#
#
class SolutionA(object):
    def validPalindrome(self, s: str) -> bool:
        """暴力法, 超时
        """
        for i in range(len(s)):
            tmp = s[:i] + s[i+1:]
            if tmp == tmp[::-1]:
                return True
        return False

class SolutionB:
    def validPalindrome(self, s: str) -> bool:
        """不够简洁"""

        return self.validPalindromeRemoveLeft(s) or self.validPalindromeRemoveRight(s)

    def validPalindromeRemoveLeft(self, s: str) -> bool:
        """双指针, 删除左边"""
        count = 0
        i = 0
        j = len(s)-1
        while i < j and count <= 1:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i+1] == s[j]:
                i += 1
                count += 1
            elif s[i] == s[j-1]:
                j -= 1
                count += 1
            else:
                return False
        return count < 2

    def validPalindromeRemoveRight(self, s: str) -> bool:
        """双指针, 删除右边"""
        count = 0
        i = 0
        j = len(s)-1
        while i < j and count <= 1:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] == s[j-1]:
                j -= 1
                count += 1
            elif s[i+1] == s[j]:
                i += 1
                count += 1
            else:
                return False
        return count < 2

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return self.check(s, i+1, j) or self.check(s, i, j-1)
            i += 1
            j -= 1
        return True

    def check(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    s = Solution().validPalindrome('abca')
    print(s)
    s = Solution().validPalindrome(
        'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga')
      # 'aguokepatgbnvfqmgmlucupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuclmgmqfvnbgtapekouga'
    print(s)

