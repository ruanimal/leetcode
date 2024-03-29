# -*- coding:utf-8 -*-

# <SUBID:305505234,UPDATE:20230205>
# English:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()" Output: true
# Example 2:
# Input: s = "()[]{}" Output: true
# Example 3:
# Input: s = "(]" Output: false
# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
#
# 中文:
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
# 示例 1：
# 输入：s = "()" 输出：true
# 示例 2：
# 输入：s = "()[]{}" 输出：true
# 示例 3：
# 输入：s = "(]" 输出：false
# 提示：
# 1 <= s.length <= 104
# s 仅由括号 '()[]{}' 组成


#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.31%)
# Total Accepted:    57.1K
# Total Submissions: 154.2K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        通过stack和括号配对map来实现
        """
        d = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        left_parts = set('[{(')
        right_parts = set(']})')
        stack = []
        for i in s:
            if i in left_parts:
                stack.append(i)
            elif i in right_parts:
                if not stack:
                    return False
                elif stack.pop() != d[i]:
                    return False
        return False if stack else True



