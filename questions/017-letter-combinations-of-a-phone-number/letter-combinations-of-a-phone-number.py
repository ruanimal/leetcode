# -*- coding:utf-8 -*-

# <SUBID:291721413,UPDATE:20230205>
# English:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Example 1:
# Input: digits = "23" Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = "" Output: []
# Example 3:
# Input: digits = "2" Output: ["a","b","c"]
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
# 中文:
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 示例 1：
# 输入：digits = "23" 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：
# 输入：digits = "" 输出：[]
# 示例 3：
# 输入：digits = "2" 输出：["a","b","c"]
# 提示：
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。


#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (49.92%)
# Likes:    434
# Dislikes: 0
# Total Accepted:    42.2K
# Total Submissions: 82.9K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#
class Solution_A(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        from itertools import product
        return [''.join(j) for j in product(*[digits_map[i] for i in digits])]

class Solution(object):
    def letterCombinations(self, digits):
        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        data = [digits_map[i] for i in digits]
        def helper(data):
            if len(data) == 0:
                return []
            if len(data) == 1:
                return list(data[0])
            return [i + j for i in data[0] for j in helper(data[1:])]
        return helper(data)

if __name__ == "__main__":
    s = Solution().letterCombinations('23')
    print(s)
    s = Solution().letterCombinations('2')
    print(s)
    s = Solution().letterCombinations('234')
    print(s)



