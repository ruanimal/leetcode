# -*- coding:utf-8 -*-


# English:
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
# Example 1:
# Input: s = "(()())(())" Output: "()()()" Explanation: The input string is "(()())(())", with primitive decomposition "(()())" + "(())". After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:
# Input: s = "(()())(())(()(()))" Output: "()()()()(())" Explanation: The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))". After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:
# Input: s = "()()" Output: "" Explanation: The input string is "()()", with primitive decomposition "()" + "()". After removing outer parentheses of each part, this is "" + "" = "".
# Constraints:
# 1 <= s.length <= 105
# s[i] is either '(' or ')'.
# s is a valid parentheses string.
#
# 中文:
# 有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。
# 例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
# 如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
# 给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
# 对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。
# 示例 1：
# 输入：s = "(()())(())" 输出："()()()" 解释： 输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"， 删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
# 示例 2：
# 输入：s = "(()())(())(()(()))" 输出："()()()()(())" 解释： 输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"， 删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
# 示例 3：
# 输入：s = "()()" 输出："" 解释： 输入字符串为 "()()"，原语化分解得到 "()" + "()"， 删除每个部分中的最外层括号后得到 "" + "" = ""。
# 提示：
# 1 <= s.length <= 105
# s[i] 为 '(' 或 ')'
# s 是一个有效括号字符串


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        start_index = 0
        res = ''
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(S[i])
            else:
                stack.pop()
            if not stack:
                res += S[start_index+1:i]
                start_index = i+1
        return res
        