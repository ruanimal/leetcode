# -*- coding:utf-8 -*-


# English:
# Given an array of 4 digits, return the largest 24 hour time that can be made.
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
# Example 1:
# Input: [1,2,3,4] Output: "23:41"
# Example 2:
# Input: [5,5,5,5] Output: ""
# Note:
# A.length == 4
# 0 <= A[i] <= 9
#
# 中文:
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
# 最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
# 以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
# 示例 1：
# 输入：[1,2,3,4] 输出："23:41"
# 示例 2：
# 输入：[5,5,5,5] 输出：""
# 提示：
# A.length == 4
# 0 <= A[i] <= 9


#
# @lc app=leetcode.cn id=949 lang=python
#
# [949] 给定数字能组成的最大时间
#
# https://leetcode-cn.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (29.26%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 5.1K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
#
# 最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
#
# 以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,4]
# 输出："23:41"
#
#
# 示例 2：
#
# 输入：[5,5,5,5]
# 输出：""
#
#
#
#
# 提示：
#
#
# A.length == 4
# 0 <= A[i] <= 9
#
#
#
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        import itertools
        tmp = []
        max_val = -1
        ans = ''
        for (a, b, c, d) in itertools.permutations(A):
            hour = a * 10 + b
            minute = c * 10 + d
            total_minute = hour * 60 + minute
            if hour < 24 and minute < 60 and total_minute > max_val:
                max_val = total_minute
                ans = '{}{}:{}{}'.format(a, b, c, d)
        return ans

if __name__ == "__main__":
    s = Solution().largestTimeFromDigits([1,2,3,4])
    print(s)
    s = Solution().largestTimeFromDigits([0, 0, 0, 0])
    print(s)

