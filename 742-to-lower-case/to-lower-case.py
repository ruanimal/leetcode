# -*- coding:utf-8 -*-


# English:
# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
# Example 1:
# Input: "Hello" Output: "hello"
# Example 2:
# Input: "here" Output: "here"
# Example 3:
# Input: "LOVELY" Output: "lovely"
#
# 中文:
# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
# 示例 1：
# 输入: "Hello" 输出: "hello"
# 示例 2：
# 输入: "here" 输出: "here"
# 示例 3：
# 输入: "LOVELY" 输出: "lovely"


#
# @lc app=leetcode.cn id=709 lang=python
#
# [709] To Lower Case
#
# https://leetcode-cn.com/problems/to-lower-case/description/
#
# algorithms
# Easy (73.23%)
# Total Accepted:    18.3K
# Total Submissions: 25K
# Testcase Example:  '"Hello"'
#
# 实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
#
#
#
# 示例 1：
#
#
# 输入: "Hello"
# 输出: "hello"
#
# 示例 2：
#
#
# 输入: "here"
# 输出: "here"
#
# 示例 3：
#
#
# 输入: "LOVELY"
# 输出: "lovely"
#
#
#
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        ret = []
        for i in str:
            if 65 <= ord(i) <= 90:
                ret.append(chr(ord(i)+32))
            else:
                ret.append(i)
        return ''.join(ret)

if __name__ == "__main__":
    s = Solution().toLowerCase("LOVELY")
    print(s)
    s = Solution().toLowerCase("Hello")
    print(s)


