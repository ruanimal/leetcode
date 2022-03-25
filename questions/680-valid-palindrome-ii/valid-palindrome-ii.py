# -*- coding:utf-8 -*-

# <SUBID:21031221,UPDATE:20220325>
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
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 示例 1:
# 输入: s = "aba" 输出: true
# 示例 2:
# 输入: s = "abca" 输出: true 解释: 你可以删除c字符。
# 示例 3:
# 输入: s = "abc" 输出: false
# 提示:
# 1 <= s.length <= 105
# s 由小写英文字母组成


#
# @lc app=leetcode.cn id=680 lang=python
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
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 暴力解法, 超时
        if not s:
            return False

        count = 0
        i, j = 0, len(s)-1
        while i < j:
            # print(i, j)
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            elif count > 0:
                # print('--')
                return False
            elif (i+2>=j-1 and s[i+1] == s[j]) or (i+2<j-1 and s[i+1] == s[j] and s[i+2] == s[j-1]):
                count += 1
                i += 1
            elif (i+1>=j-2 and s[i] == s[j-1]) or (i+1<j-2 and s[i] == s[j-1] and s[i+1] == s[j-2]):
                count += 1
                j -= 1
            else:
                # print('++')
                return False
        return True

if __name__ == "__main__":
    s = Solution().validPalindrome('aydmda')
    print(s)
    # s = Solution().validPalindrome('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga')
    # print(s)

