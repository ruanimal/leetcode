# -*- coding:utf-8 -*-


# English:
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# For example:
# A -> 1 B -> 2 C -> 3 ... Z -> 26 AA -> 27 AB -> 28 ...
# Example 1:
# Input: "A" Output: 1
# Example 2:
# Input: "AB" Output: 28
# Example 3:
# Input: "ZY" Output: 701
#
# 中文:
# 给定一个Excel表格中的列名称，返回其相应的列序号。
# 例如，
# A -> 1 B -> 2 C -> 3 ... Z -> 26 AA -> 27 AB -> 28 ...
# 示例 1:
# 输入: "A" 输出: 1
# 示例 2:
# 输入: "AB" 输出: 28
# 示例 3:
# 输入: "ZY" 输出: 701
# 致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。


#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans_map = {i:idx+1 for idx, i in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
        ret = 0
        for idx, i in enumerate(s):
            ret += trans_map[i] * (26 ** (len(s)-idx-1))
        return ret

if __name__ == "__main__":
    s = Solution().titleToNumber("AB")
    print(s)

