# -*- coding:utf-8 -*-

# <SUBID:301781800,UPDATE:20230205>
# English:
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Example 1:
# Input: s = "III" Output: 3 Explanation: III = 3.
# Example 2:
# Input: s = "LVIII" Output: 58 Explanation: L = 50, V= 5, III = 3.
# Example 3:
# Input: s = "MCMXCIV" Output: 1994 Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].
#
# 中文:
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 字符 数值 I 1 V 5 X 10 L 50 C 100 D 500 M 1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个罗马数字，将其转换成整数。
# 示例 1:
# 输入: s = "III" 输出: 3
# 示例 2:
# 输入: s = "IV" 输出: 4
# 示例 3:
# 输入: s = "IX" 输出: 9
# 示例 4:
# 输入: s = "LVIII" 输出: 58 解释: L = 50, V= 5, III = 3.
# 示例 5:
# 输入: s = "MCMXCIV" 输出: 1994 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# 提示：
# 1 <= s.length <= 15
# s 仅含字符 ('I', 'V', 'X', 'L', 'C', 'D', 'M')
# 题目数据保证 s 是一个有效的罗马数字，且表示整数在范围 [1, 3999] 内
# 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
# IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
# 关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。


#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (56.62%)
# Total Accepted:    48.9K
# Total Submissions: 85.3K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#
#
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: "III"
# 输出: 3
#
# 示例 2:
#
# 输入: "IV"
# 输出: 4
#
# 示例 3:
#
# 输入: "IX"
# 输出: 9
#
# 示例 4:
#
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
#
#
# 示例 5:
#
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
#


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        从左到右将罗马字符转换为数字再相加, 遇到IV这种就减去两倍的I
        """
        num_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)-1):
            result += num_map[s[i]]
            if num_map[s[i]] < num_map[s[i+1]]:
                result -= 2*num_map[s[i]]
        result += num_map[s[-1]]
        return result

    def IntToroman(self, num):
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        num_map = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }

        ans = []
        for i in num_list:
            if i > num:
                continue
            if num == 0:
                break
            a, num = divmod(num, i)
            ans.append(a * num_map[i])
        return ''.join(ans)

if __name__ == "__main__":
    obj = Solution()
    for i in range(1,6000):
        a = obj.IntToroman(i)
        b = obj.romanToInt(a)
        print(a,b)
        assert i == b


