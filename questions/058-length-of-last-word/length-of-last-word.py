# -*- coding:utf-8 -*-

# <SUBID:15955682,UPDATE:20230205>
# English:
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Example 1:
# Input: s = "Hello World" Output: 5 Explanation: The last word is "World" with length 5.
# Example 2:
# Input: s = " fly me to the moon " Output: 4 Explanation: The last word is "moon" with length 4.
# Example 3:
# Input: s = "luffy is still joyboy" Output: 6 Explanation: The last word is "joyboy" with length 6.
# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.
#
# 中文:
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
# 示例 1：
# 输入：s = "Hello World" 输出：5 解释：最后一个单词是“World”，长度为5。
# 示例 2：
# 输入：s = " fly me to the moon " 输出：4 解释：最后一个单词是“moon”，长度为4。
# 示例 3：
# 输入：s = "luffy is still joyboy" 输出：6 解释：最后一个单词是长度为6的“joyboy”。
# 提示：
# 1 <= s.length <= 104
# s 仅有英文字母和空格 ' ' 组成
# s 中至少存在一个单词


#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (28.67%)
# Total Accepted:    21.7K
# Total Submissions: 74.2K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
#
#
#
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        """
        # 解法一: 遍历字符串, 记录每个子字符串的长度
        # if not s:
        #     return 0

        # last = 0
        # tmp = 0
        # in_space = False
        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         in_space = False
        #         tmp += 1
        #     else:
        #         if in_space == False:
        #             last = tmp
        #             tmp = 0
        #         in_space = True
        # # print(last, tmp, in_space)
        # if tmp != 0:
        #     return tmp
        # return last



        if not s:
            return 0

        count = 0
        in_word = False if (s[-1] == ' ') else True
        is_space = False
        for i in range(len(s)-1, -1, -1):
            is_space = (s[i] == ' ')
            if in_word and is_space:
                in_word = False
                break
            elif in_word and not is_space:
                count += 1
            elif not in_word and is_space:
                continue
            else:
                count = 1  # 第一个字符
                in_word = True
        return count


if __name__ == "__main__":
    print(Solution().lengthOfLastWord('  hello  world   '))

