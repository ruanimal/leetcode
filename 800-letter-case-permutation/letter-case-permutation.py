# -*- coding:utf-8 -*-


# English:
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
# Examples: Input: S = "a1b2" Output: ["a1b2", "a1B2", "A1b2", "A1B2"] Input: S = "3z4" Output: ["3z4", "3Z4"] Input: S = "12345" Output: ["12345"]
# Note:
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
#
# 中文:
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
# 示例: 输入: S = "a1b2" 输出: ["a1b2", "a1B2", "A1b2", "A1B2"] 输入: S = "3z4" 输出: ["3z4", "3Z4"] 输入: S = "12345" 输出: ["12345"]
# 注意：
# S 的长度不超过12。
# S 仅由数字和字母组成。


#
# @lc app=leetcode.cn id=784 lang=python
#
# [784] 二叉搜索树中的插入操作
#
# https://leetcode-cn.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (50.66%)
# Total Accepted:    3.8K
# Total Submissions: 7.2K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
#
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
#
# 输入: S = "12345"
# 输出: ["12345"]
#
#
# 注意：
#
#
# S 的长度不超过12。
# S 仅由数字和字母组成。
#
#
#

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ret = []
        tmp = []
        def dfs(pos):
            if pos == len(S):
                ret.append(''.join(tmp))
                return
            if S[pos].isdigit():
                tmp.append(S[pos])
                dfs(pos+1)
                tmp.pop()
            elif S[pos].islower():
                tmp.append(S[pos])
                dfs(pos+1)
                tmp.pop()
                tmp.append(S[pos].upper())
                dfs(pos+1)
                tmp.pop()
            else:
                tmp.append(S[pos])
                dfs(pos+1)
                tmp.pop()
                tmp.append(S[pos].lower())
                dfs(pos+1)
                tmp.pop()
        dfs(0)
        return ret
if __name__ == "__main__":
    s = Solution().letterCasePermutation('a1b2')
    print(s)

