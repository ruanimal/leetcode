# -*- coding:utf-8 -*-


# English:
# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
# For example, with A = "abcd" and B = "cdabcdab".
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
# Note:
# The length of A and B will be between 1 and 10000.
#
# 中文:
# 给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
# 举个例子，A = "abcd"，B = "cdabcdab"。
# 答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
# 注意:
# A 与 B 字符串的长度在1和10000区间范围内。


#
# @lc app=leetcode.cn id=686 lang=python
#
# [686] 重复叠加字符串匹配
#
# https://leetcode-cn.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (28.92%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 10.8K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# 给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
#
# 举个例子，A = "abcd"，B = "cdabcdab"。
#
# 答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
#
# 注意:
#
# A 与 B 字符串的长度在1和10000区间范围内。
#
#
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # # 有bug
        # idx = B.find(A)

        # if len(A) > len(B):
        #     if B in A:
        #         return 1
        #     elif B in A*2:
        #         return 2
        #     else:
        #         return -1
        # if not A or not B:
        #     return -1
        # if idx == -1:
        #     return -1
        # if idx != 0 and B[:idx] not in A:
        #     return -1
        # cnt = 0 if idx == 0 else 1
        # for i in range(idx, len(B), len(A)):
        #     print(B[i:i+len(A)])
        #     if A.find(B[i:i+len(A)]) != 0:
        #         return -1
        #     else:
        #         cnt += 1
        # return cnt

        if not A or not B:
            return -1
        i = 1
        a = A
        maxLen = len(A + A + B)
        while len(a) < maxLen:
            if (B in a):
                return i
            else:
                i = i + 1
                a += A
        return -1

if __name__ == "__main__":
    s = Solution().repeatedStringMatch('abcd', 'cdabcdab')
    print(s)
    s = Solution().repeatedStringMatch('abcd', '')
    print(s)
    s = Solution().repeatedStringMatch('', 'abc')
    print(s)
    s = Solution().repeatedStringMatch('aaaaaaaaaaaaaaaaaaaaaab', 'ba')
    print(s)
    s = Solution().repeatedStringMatch("abcd", "cdabcdab")
    print(s)


