# -*- coding:utf-8 -*-


# English:
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.
# Note:
# Assume the length of given string will not exceed 1,010.
# Example:
# Input: "abccccdd" Output: 7 Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
#
# 中文:
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 注意:
# 假设字符串的长度不会超过 1010。
# 示例 1:
# 输入: "abccccdd" 输出: 7 解释: 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。


#
# @lc app=leetcode.cn id=409 lang=python
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (46.75%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 12.2K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#
# 注意:
# 假设字符串的长度不会超过 1010。
#
# 示例 1:
#
#
# 输入:
# "abccccdd"
#
# 输出:
# 7
#
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#
#
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        count_s = Counter(s)
        ret = 0
        odd = 0
        for k, v in count_s.items():
            if (v & 1) == 0:
                ret += v
            else:
                ret += (v-1)
                odd = 1
        return ret + odd

if __name__ == "__main__":
    s = Solution().longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth')
    print(s)


