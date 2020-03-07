# -*- coding:utf-8 -*-


# English:
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
# 中文:
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 注意：
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。


#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (44.83%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 17.2K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
#
#
#
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = []
        length = max(len(num1), len(num2))
        tmp = 0
        for i in range(1, length+1):
            if i > len(num1):
                a = 0
            else:
                a = int(num1[-i])
            if i > len(num2):
                b = 0
            else:
                b = int(num2[-i])
            tmp, a = divmod(a+b+tmp, 10)
            ret.append(str(a))
        if tmp:
            ret.append(str(tmp))
        return ''.join(ret[::-1])

if __name__ == "__main__":
    s = Solution().addStrings('1234', '66666')
    print(s)


