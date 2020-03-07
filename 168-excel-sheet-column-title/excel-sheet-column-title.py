# -*- coding:utf-8 -*-


# English:
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
# 1 -> A 2 -> B 3 -> C ... 26 -> Z 27 -> AA 28 -> AB ...
# Example 1:
# Input: 1 Output: "A"
# Example 2:
# Input: 28 Output: "AB"
# Example 3:
# Input: 701 Output: "ZY"
#
# 中文:
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 例如，
# 1 -> A 2 -> B 3 -> C ... 26 -> Z 27 -> AA 28 -> AB ...
# 示例 1:
# 输入: 1 输出: "A"
# 示例 2:
# 输入: 28 输出: "AB"
# 示例 3:
# 输入: 701 输出: "ZY"


#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (31.68%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 27.2K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
# 例如，
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB
# ⁠   ...
#
#
# 示例 1:
#
# 输入: 1
# 输出: "A"
#
#
# 示例 2:
#
# 输入: 28
# 输出: "AB"
#
#
# 示例 3:
#
# 输入: 701
# 输出: "ZY"
#
#
#
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return

        trans_map = {idx+1: i for idx, i in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
        ans = []
        while n > 0:
            n, tmp = divmod(n, 26)
            if tmp == 0:
                n -= 1
                tmp = 26
            ans.append(trans_map[tmp])
        return ''.join(ans[::-1])

if __name__ == "__main__":
    s = Solution().convertToTitle(1)
    print(s)
    s = Solution().convertToTitle(25)
    print(s)
    s = Solution().convertToTitle(26)
    print(s)
    s = Solution().convertToTitle(27)
    print(s)
    s = Solution().convertToTitle(28)
    print(s)
    s = Solution().convertToTitle(52)
    print(s)
    s = Solution().convertToTitle(701)
    print(s)

