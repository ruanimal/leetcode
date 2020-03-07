# -*- coding:utf-8 -*-


# English:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# Example 1:
# Input: "A man, a plan, a canal: Panama" Output: true
# Example 2:
# Input: "race a car" Output: false
#
# 中文:
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 示例 1:
# 输入: "A man, a plan, a canal: Panama" 输出: true
# 示例 2:
# 输入: "race a car" 输出: false


#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (39.27%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    38.8K
# Total Submissions: 97.2K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
#
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        alpha_set = set('abcdefghijklmnopqrstuvwxyz'+'0123456789')
        i = 0
        j = len(s)-1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            fa = a not in alpha_set
            fb = b not in alpha_set
            if fa:
                i += 1
            if fb:
                j -= 1
            if fa or fb:
                continue
            if a != b:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    # s = Solution().isPalindrome('aabdbaa')
    # print(s)
    # s = Solution().isPalindrome('')
    # print(s)
    s = Solution().isPalindrome("A man, a plan, a canal: Panama")
    print(s)


