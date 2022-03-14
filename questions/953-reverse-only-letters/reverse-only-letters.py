# -*- coding:utf-8 -*-


# English:
# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.
# Example 1:
# Input: s = "ab-cd" Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj" Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!" Output: "Qedo1ct-eeLg=ntse-T!"
# Constraints:
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
#
# 中文:
# 给你一个字符串 s ，根据下述规则反转字符串：
# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
# 返回反转后的 s 。
# 示例 1：
# 输入：s = "ab-cd" 输出："dc-ba"
# 示例 2：
# 输入：s = "a-bC-dEf-ghIj" 输出："j-Ih-gfE-dCba"
# 示例 3：
# 输入：s = "Test1ng-Leet=code-Q!" 输出："Qedo1ct-eeLg=ntse-T!"
# 提示
# 1 <= s.length <= 100
# s 仅由 ASCII 值在范围 [33, 122] 的字符组成
# s 不含 '\"' 或 '\\'


#
# @lc app=leetcode.cn id=917 lang=python
#
# [917] 救生艇
#
# https://leetcode-cn.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (45.64%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 7.4K
# Testcase Example:  '"ab-cd"'
#
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
#
#
#
#
#
# 示例 1：
#
# 输入："ab-cd"
# 输出："dc-ba"
#
#
# 示例 2：
#
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#
#
# 示例 3：
#
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#
#
#
#
# 提示：
#
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S 中不包含 \ or "
#
#
#
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        index_que = []
        ret = []
        for idx, i in enumerate(S):
            if i.isalpha():
                stack.append(i)
                ret.append(None)
                index_que.append(idx)
            else:
                ret.append(i)
        for i in index_que:
            ret[i] = stack.pop()
        return ''.join(ret)

if __name__ == "__main__":
    s = Solution().reverseOnlyLetters("a-bC-dEf-ghIj")
    print(s)


