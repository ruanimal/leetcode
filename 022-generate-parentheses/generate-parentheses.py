# -*- coding:utf-8 -*-


# English:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [ "((()))", "(()())", "(())()", "()(())", "()()()" ]
#
# 中文:
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 例如，给出 n = 3，生成结果为：
# [ "((()))", "(()())", "(())()", "()(())", "()()()" ]


#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (69.88%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 39.9K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []

        ans = []
        def dfs(level, left, right, path):
            if level >= 2 * n:
                ans.append(''.join(path))
                return

            if left < n:
                path.append('(')
                dfs(level+1, left+1, right, path)
                path.pop()

            if left - 1 >= right:
                path.append(')')
                dfs(level+1, left, right+1, path)
                path.pop()

        dfs(0, 0, 0, [])
        return ans

if __name__ == "__main__":
    s = Solution().generateParenthesis(3)
    print(s)
    s = Solution().generateParenthesis(4)
    print(s)



