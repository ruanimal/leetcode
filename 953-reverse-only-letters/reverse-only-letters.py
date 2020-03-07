# -*- coding:utf-8 -*-


# English:
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
# Example 1:
# Input: "ab-cd" Output: "dc-ba"
# Example 2:
# Input: "a-bC-dEf-ghIj" Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: "Test1ng-Leet=code-Q!" Output: "Qedo1ct-eeLg=ntse-T!"
# Note:
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "
#
# 中文:
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
# 示例 1：
# 输入："ab-cd" 输出："dc-ba"
# 示例 2：
# 输入："a-bC-dEf-ghIj" 输出："j-Ih-gfE-dCba"
# 示例 3：
# 输入："Test1ng-Leet=code-Q!" 输出："Qedo1ct-eeLg=ntse-T!"
# 提示：
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S 中不包含 \ or "


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


