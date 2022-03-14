# -*- coding:utf-8 -*-


# English:
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
# Example 1:
# Input: s = "42" Output: 42 Explanation: The underlined characters are what is read in, the caret is the current reader position. Step 1: "42" (no characters read because there is no leading whitespace) ^ Step 2: "42" (no characters read because there is neither a '-' nor '+') ^ Step 3: "
# 42
# " ("42" is read in) ^ The parsed integer is 42. Since 42 is in the range [-231, 231 - 1], the final result is 42.
# Example 2:
# Input: s = " -42" Output: -42 Explanation: Step 1: "
# -42" (leading whitespace is read and ignored) ^ Step 2: "
# -
# 42" ('-' is read, so the result should be negative) ^ Step 3: " -
# 42
# " ("42" is read in) ^ The parsed integer is -42. Since -42 is in the range [-231, 231 - 1], the final result is -42.
# Example 3:
# Input: s = "4193 with words" Output: 4193 Explanation: Step 1: "4193 with words" (no characters read because there is no leading whitespace) ^ Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+') ^ Step 3: "
# 4193
# with words" ("4193" is read in; reading stops because the next character is a non-digit) ^ The parsed integer is 4193. Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
# Constraints:
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
#
# 中文:
# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
# 函数 myAtoi(string s) 的算法如下：
# 读入字符串并丢弃无用的前导空格
# 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
# 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
# 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
# 如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
# 返回整数作为最终结果。
# 注意：
# 本题中的空白字符只包括空格字符 ' ' 。
# 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
# 示例 1：
# 输入：s = "42" 输出：42 解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。 第 1 步："42"（当前没有读入字符，因为没有前导空格） ^ 第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'） ^ 第 3 步："
# 42
# "（读入 "42"） ^ 解析得到整数 42 。 由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。
# 示例 2：
# 输入：s = " -42" 输出：-42 解释： 第 1 步："
# -42"（读入前导空格，但忽视掉） ^ 第 2 步："
# -
# 42"（读入 '-' 字符，所以结果应该是负数） ^ 第 3 步："
# -42
# "（读入 "42"） ^ 解析得到整数 -42 。 由于 "-42" 在范围 [-231, 231 - 1] 内，最终结果为 -42 。
# 示例 3：
# 输入：s = "4193 with words" 输出：4193 解释： 第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格） ^ 第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'） ^ 第 3 步："
# 4193
# with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止） ^ 解析得到整数 4193 。 由于 "4193" 在范围 [-231, 231 - 1] 内，最终结果为 4193 。
# 提示：
# 0 <= s.length <= 200
# s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成


#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#
# https://leetcode-cn.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (16.40%)
# Total Accepted:    38.6K
# Total Submissions: 230.1K
# Testcase Example:  '"42"'
#
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
#
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
#
#
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
#
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
#
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
#
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
#
# 说明：
#
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，qing返回
# INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。
#
# 示例 1:
#
# 输入: "42"
# 输出: 42
#
#
# 示例 2:
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
# 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
#
#
# 示例 3:
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
#
#
# 示例 4:
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
# ⁠    因此无法执行有效的转换。
#
# 示例 5:
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
# 因此返回 INT_MIN (−2^31) 。
#
#
#
class Solution(object):
    def myAtoi(self, string):
        """
        :type string: string
        :rtype: int
        """
        string = string.strip()
        if not string:
            return 0

        num = 0
        num_map = {chr(i): i-48 for i in range(48, 58)}
        sign = 1
        if string[0] == '-':
            sign = -1
            string = string[1:]
        elif string[0] == '+':
            string = string[1:]

        for i in string:
            if i not in num_map:
                break
            num = num * 10 + num_map[i]
        num = num * sign
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        return num

if __name__ == "__main__":
    s = Solution().myAtoi('-3334234 . fsfsdfs')
    print(repr(s))


