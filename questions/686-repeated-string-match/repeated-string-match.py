# -*- coding:utf-8 -*-

# <SUBID:21034697,UPDATE:20220325>
# English:
# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b to be a substring of a after repeating it, return -1.
# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".
# Example 1:
# Input: a = "abcd", b = "cdabcdab" Output: 3 Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
# Example 2:
# Input: a = "a", b = "aa" Output: 2
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist of lowercase English letters.
#
# 中文:
# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
# 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
# 示例 1：
# 输入：a = "abcd", b = "cdabcdab" 输出：3 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
# 示例 2：
# 输入：a = "a", b = "aa" 输出：2
# 示例 3：
# 输入：a = "a", b = "a" 输出：1
# 示例 4：
# 输入：a = "abc", b = "wxyz" 输出：-1
# 提示：
# 1 <= a.length <= 104
# 1 <= b.length <= 104
# a 和 b 由小写英文字母组成


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


