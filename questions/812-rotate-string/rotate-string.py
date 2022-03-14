# -*- coding:utf-8 -*-


# English:
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.
# Example 1:
# Input: s = "abcde", goal = "cdeab" Output: true
# Example 2:
# Input: s = "abcde", goal = "abced" Output: false
# Constraints:
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.
#
# 中文:
# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
# s 的 旋转操作 就是将 s 最左边的字符移动到最右边。
# 例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
# 示例 1:
# 输入: s = "abcde", goal = "cdeab" 输出: true
# 示例 2:
# 输入: s = "abcde", goal = "abced" 输出: false
# 提示:
# 1 <= s.length, goal.length <= 100
# s 和 goal 由小写英文字母组成


#
# @lc app=leetcode.cn id=796 lang=python
#
# [796] 到达终点
#
# https://leetcode-cn.com/problems/rotate-string/description/
#
# algorithms
# Easy (45.40%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 7.9K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# 给定两个字符串, A 和 B。
#
# A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea'
# 。如果在若干次旋转操作之后，A 能变成B，那么返回True。
#
#
# 示例 1:
# 输入: A = 'abcde', B = 'cdeab'
# 输出: true
#
# 示例 2:
# 输入: A = 'abcde', B = 'abced'
# 输出: false
#
# 注意：
#
#
# A 和 B 长度不超过 100。
#
#
#
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and not B:
            return True
        if len(A) != len(B):
            return False

        s = set()
        for i in range(len(A)):
            s.add(A[i+1:] + A[:i+1])
        return B in s

if __name__ == "__main__":
    s = Solution().rotateString(A = 'abcde', B = 'abced')
    print(s)
    s = Solution().rotateString(A = 'abcde', B = 'cdeab')
    print(s)

