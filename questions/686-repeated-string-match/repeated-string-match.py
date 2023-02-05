# -*- coding:utf-8 -*-

# <SUBID:319233489,UPDATE:20230205>
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


class SolutionA:
    def repeatedStringMatch(self, A: str, B: str) -> int:
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

# TODO(rlj): KMP.
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """
        B = subfix(A) + A * n + prefix(A), 其中n>=0
        """
        if not A or not B:
            return -1
        if B in A:
            return 1
        if B in (A+A):  # n = 0 的情况
            return 2

        ans = 0
        head_index = B.find(A)
        if head_index < 0:
            return -1
        i = head_index
        while i < len(B):
            if B.find(A, i) == i:
                i += len(A)
                ans += 1
            else:
                break
        tail_index = head_index + ans * len(A)
        if head_index > 0:   # n > 0 且有subfix
            if A.endswith(B[:head_index]):
                ans += 1
            else:
                return -1
        if tail_index < len(B):   # n > 0 有subfix
            if A.startswith(B[tail_index:]):
                ans += 1
            else:
                return -1
        return ans

