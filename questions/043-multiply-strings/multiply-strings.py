# -*- coding:utf-8 -*-


# English:
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
# Example 1:
# Input: num1 = "2", num2 = "3" Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456" Output: "56088"
# Constraints:
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
#
# 中文:
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
# 示例 1:
# 输入: num1 = "2", num2 = "3" 输出: "6"
# 示例 2:
# 输入: num1 = "123", num2 = "456" 输出: "56088"
# 提示：
# 1 <= num1.length, num2.length <= 200
# num1 和 num2 只能由数字组成。
# num1 和 num2 都不包含任何前导零，除了数字0本身。


#
# @lc app=leetcode.cn id=43 lang=python
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (38.46%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 46.2K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
#
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
# 说明：
#
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#
#
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        from collections import deque
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = [int(i) for i in num1]
        num2 = [int(i) for i in num2]
        L1 = len(num1)
        L2 = len(num2)
        ans = deque()
        for i in range(L1-1, -1, -1):
            tmp = deque([0 for _ in range(L1-1-i)])
            extra = 0
            for j in range(L2-1, -1, -1):
                extra, ret = divmod(extra+num1[i]*num2[j], 10)
                tmp.appendleft(ret)
            if extra:
                tmp.appendleft(extra)
            ans = self.big_number_add(ans, tmp)
        return ''.join(str(i) for i in ans).lstrip('0')

    def big_number_add(self, num1, num2):
        L1 = len(num1)
        L2 = len(num2)
        ans = []
        extra = 0
        for i in range(max(L1, L2)):
            a = num1[-1-i] if 0 <= i < L1 else 0
            b = num2[-1-i] if 0 <= i < L2 else 0
            extra, ret = divmod(a+b+extra, 10)
            ans.append(ret)
        if extra:
            ans.append(extra)
        return ans[::-1]

def test_(a, b):
    l = Solution().multiply(a, b)
    r = str(int(a) * int(b))
    print(repr(l), repr(r))
    assert l == r

if __name__ == "__main__":
    test_('123', '123')
    test_('123', '0')
    test_('0', '0')
    test_('1231231012312', '213123123')

