# -*- coding:utf-8 -*-


# English:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama" Output: true Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car" Output: false Explanation: "raceacar" is not a palindrome.
# Example 3:
# Input: s = " " Output: true Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
#
# 中文:
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 示例 1:
# 输入: "A man, a plan, a canal: Panama" 输出: true 解释："amanaplanacanalpanama" 是回文串
# 示例 2:
# 输入: "race a car" 输出: false 解释："raceacar" 不是回文串
# 提示：
# 1 <= s.length <= 2 * 105
# 字符串 s 由 ASCII 字符组成


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


