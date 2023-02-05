# -*- coding:utf-8 -*-

# <SUBID:314830424,UPDATE:20230205>
# English:
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
# Example 1:
# Input: num1 = "11", num2 = "123" Output: "134"
# Example 2:
# Input: num1 = "456", num2 = "77" Output: "533"
# Example 3:
# Input: num1 = "0", num2 = "0" Output: "0"
# Constraints:
# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
#
# 中文:
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
# 示例 1：
# 输入：num1 = "11", num2 = "123" 输出："134"
# 示例 2：
# 输入：num1 = "456", num2 = "77" 输出："533"
# 示例 3：
# 输入：num1 = "0", num2 = "0" 输出："0"
# 提示：
# 1 <= num1.length, num2.length <= 104
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        按每个字符计算, 并注意进位
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

