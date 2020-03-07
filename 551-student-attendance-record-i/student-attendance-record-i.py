# -*- coding:utf-8 -*-


# English:
# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
# You need to return whether the student could be rewarded according to his attendance record.
# Example 1:
#
# Input: "PPALLP" Output: True
# Example 2:
#
# Input: "PPALLL" Output: False
#
# 中文:
# 给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
# 'A' : Absent，缺勤
# 'L' : Late，迟到
# 'P' : Present，到场
# 如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
# 你需要根据这个学生的出勤记录判断他是否会被奖赏。
# 示例 1:
# 输入: "PPALLP" 输出: True
# 示例 2:
# 输入: "PPALLL" 输出: False


#
# @lc app=leetcode.cn id=551 lang=python
#
# [551] 学生出勤记录 I
#
# https://leetcode-cn.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (46.98%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 10.8K
# Testcase Example:  '"PPALLP"'
#
# 给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：
#
#
# 'A' : Absent，缺勤
# 'L' : Late，迟到
# 'P' : Present，到场
#
#
# 如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
#
# 你需要根据这个学生的出勤记录判断他是否会被奖赏。
#
# 示例 1:
#
# 输入: "PPALLP"
# 输出: True
#
#
# 示例 2:
#
# 输入: "PPALLL"
# 输出: False
#
#
#
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return

        a = 0
        l = 0
        for i in range(len(s)):
            if s[i] == 'A':
                a += 1
                l = 0
            elif s[i] == 'L':
                l += 1
            else:
                l = 0
            if a > 1 or l > 2:
                return False
        return True

if __name__ == "__main__":
    s = Solution().checkRecord("PPALLAPL")
    print(s)


