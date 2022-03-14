# -*- coding:utf-8 -*-


# English:
# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Return true if the student is eligible for an attendance award, or false otherwise.
# Example 1:
# Input: s = "PPALLP" Output: true Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL" Output: false Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
# Constraints:
# 1 <= s.length <= 1000
# s[i] is either 'A', 'L', or 'P'.
#
# 中文:
# 给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
# 'A'：Absent，缺勤
# 'L'：Late，迟到
# 'P'：Present，到场
# 如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：
# 按 总出勤 计，学生缺勤（'A'）严格 少于两天。
# 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。
# 如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：s = "PPALLP" 输出：true 解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。
# 示例 2：
# 输入：s = "PPALLL" 输出：false 解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。
# 提示：
# 1 <= s.length <= 1000
# s[i] 为 'A'、'L' 或 'P'


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


