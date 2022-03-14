# -*- coding:utf-8 -*-


# English:
# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
# For example:
# A -> 1 B -> 2 C -> 3 ... Z -> 26 AA -> 27 AB -> 28 ...
# Example 1:
# Input: columnTitle = "A" Output: 1
# Example 2:
# Input: columnTitle = "AB" Output: 28
# Example 3:
# Input: columnTitle = "ZY" Output: 701
# Constraints:
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].
#
# 中文:
# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。
# 例如：
# A -> 1 B -> 2 C -> 3 ... Z -> 26 AA -> 27 AB -> 28 ...
# 示例 1:
# 输入: columnTitle = "A" 输出: 1
# 示例 2:
# 输入: columnTitle = "AB" 输出: 28
# 示例 3:
# 输入: columnTitle = "ZY" 输出: 701
# 提示：
# 1 <= columnTitle.length <= 7
# columnTitle 仅由大写英文组成
# columnTitle 在范围 ["A", "FXSHRXW"] 内


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

