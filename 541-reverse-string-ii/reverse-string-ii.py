# -*- coding:utf-8 -*-


# English:
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
#
# Input: s = "abcdefg", k = 2 Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]
#
# 中文:
# 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
# 示例:
# 输入: s = "abcdefg", k = 2 输出: "bacdfeg"
# 要求:
# 该字符串只包含小写的英文字母。
# 给定字符串的长度和 k 在[1, 10000]范围内。


#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#
# https://leetcode-cn.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (45.32%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 10.5K
# Testcase Example:  '"abcdefg"\n2'
#
# 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k
# 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
#
# 示例:
#
#
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#
#
# 要求:
#
#
# 该字符串只包含小写的英文字母。
# 给定字符串的长度和 k 在[1, 10000]范围内。
#
#
#
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = []
        for i in range(0, len(s), 2*k):
            tmp = s[i:i+k]
            ans.append(tmp[::-1])
            ans.append(s[i+k:i+2*k])
        return ''.join(ans)

if __name__ == "__main__":
    s = Solution().reverseStr('abcdefg', 8)
    print(s)


