# -*- coding:utf-8 -*-

# <SUBID:19961574,UPDATE:20220325>
# English:
# Given an integer num, return a string of its base 7 representation.
# Example 1:
# Input: num = 100 Output: "202"
# Example 2:
# Input: num = -7 Output: "-10"
# Constraints:
# -107 <= num <= 107
#
# 中文:
# 给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
# 示例 1:
# 输入: num = 100 输出: "202"
# 示例 2:
# 输入: num = -7 输出: "-10"
# 提示：
# -107 <= num <= 107


#
# @lc app=leetcode.cn id=504 lang=python
#
# [504] 七进制数
#
# https://leetcode-cn.com/problems/base-7/description/
#
# algorithms
# Easy (43.27%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 8.6K
# Testcase Example:  '100'
#
# 给定一个整数，将其转化为7进制，并以字符串形式输出。
#
# 示例 1:
#
#
# 输入: 100
# 输出: "202"
#
#
# 示例 2:
#
#
# 输入: -7
# 输出: "-10"
#
#
# 注意: 输入范围是 [-1e7, 1e7] 。
#
#
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return '0'

        tmp = []
        flag = ''
        if num < 0:
            flag = '-'
            num = abs(num)
        while num > 0:
            num, ret = divmod(num, 7)
            tmp.append(str(ret))
        return flag + ''.join(tmp[::-1])

if __name__ == "__main__":
    s = Solution().convertToBase7(101)
    print(s)
    s = Solution().convertToBase7(-7)
    print(s)
    s = Solution().convertToBase7(0)
    print(s)


