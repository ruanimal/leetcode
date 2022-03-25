# -*- coding:utf-8 -*-

# <SUBID:17656952,UPDATE:20220325>
# English:
# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
# Example 1:
# Input: s = "IDID" Output: [0,4,1,3,2]
# Example 2:
# Input: s = "III" Output: [0,1,2,3]
# Example 3:
# Input: s = "DDI" Output: [3,2,0,1]
# Constraints:
# 1 <= s.length <= 105
# s[i] is either 'I' or 'D'.
#
# 中文:
# 由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:
# 如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I'
# 如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D'
# 给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。
# 示例 1：
# 输入：s = "IDID" 输出：[0,4,1,3,2]
# 示例 2：
# 输入：s = "III" 输出：[0,1,2,3]
# 示例 3：
# 输入：s = "DDI" 输出：[3,2,0,1]
# 提示：
# 1 <= s.length <= 105
# s
# 只包含字符 "I" 或 "D"


#
# @lc app=leetcode.cn id=942 lang=python
#
# [942] 超级回文数
"""
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]


示例 1：

输出："IDID"
输出：[0,4,1,3,2]
示例 2：

输出："III"
输出：[0,1,2,3]
示例 3：

输出："DDI"
输出：[3,2,0,1]


提示：

1 <= S.length <= 1000
S 只包含字符 "I" 或 "D"。
"""

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return
        ret = []
        a = 0
        b = len(S)
        i = None
        for i in S:
            if i == 'I':
                ret.append(a)
                a += 1
            else:
                ret.append(b)
                b -= 1
        if i == 'I':
            ret.append(a)
            a += 1
        else:
            ret.append(b)
            b -= 1
        return ret

if __name__ == "__main__":
    s = Solution().diStringMatch("IDID")
    print(s)
    s = Solution().diStringMatch("III")
    print(s)
    s = Solution().diStringMatch("DDI")
    print(s)
    s = Solution().diStringMatch("DDD")
    print(s)


