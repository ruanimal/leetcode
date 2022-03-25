# -*- coding:utf-8 -*-

# <SUBID:28654634,UPDATE:20220325>
# English:
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
# Example 1:
# Input: num = 3 Output: "III" Explanation: 3 is represented as 3 ones.
# Example 2:
# Input: num = 58 Output: "LVIII" Explanation: L = 50, V = 5, III = 3.
# Example 3:
# Input: num = 1994 Output: "MCMXCIV" Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# Constraints:
# 1 <= num <= 3999
#
# 中文:
# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
# 字符 数值 I 1 V 5 X 10 L 50 C 100 D 500 M 1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给你一个整数，将其转为罗马数字。
# 示例 1:
# 输入: num = 3 输出: "III"
# 示例 2:
# 输入: num = 4 输出: "IV"
# 示例 3:
# 输入: num = 9 输出: "IX"
# 示例 4:
# 输入: num = 58 输出: "LVIII" 解释: L = 50, V = 5, III = 3.
# 示例 5:
# 输入: num = 1994 输出: "MCMXCIV" 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# 提示：
# 1 <= num <= 3999


#
# @lc app=leetcode.cn id=12 lang=python
#
# [12] 整数转罗马数字
#
# https://leetcode-cn.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (59.94%)
# Likes:    197
# Dislikes: 0
# Total Accepted:    37.3K
# Total Submissions: 61.4K
# Testcase Example:  '3'
#
# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
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
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: 3
# 输出: "III"
#
# 示例 2:
#
# 输入: 4
# 输出: "IV"
#
# 示例 3:
#
# 输入: 9
# 输出: "IX"
#
# 示例 4:
#
# 输入: 58
# 输出: "LVIII"
# 解释: L = 50, V = 5, III = 3.
#
#
# 示例 5:
#
# 输入: 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
#
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

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


