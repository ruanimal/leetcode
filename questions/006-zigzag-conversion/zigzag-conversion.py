# -*- coding:utf-8 -*-


# English:
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P A H N A P L S I I G Y I R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3 Output: "PAHNAPLSIIGYIR"
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4 Output: "PINALSIGYAHRPI" Explanation: P I N A L S I G Y A H R P I
# Example 3:
# Input: s = "A", numRows = 1 Output: "A"
# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
# 中文:
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# P A H N A P L S I I G Y I R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);
# 示例 1：
# 输入：s = "PAYPALISHIRING", numRows = 3 输出："PAHNAPLSIIGYIR"
# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4 输出："PINALSIGYAHRPI" 解释： P I N A L S I G Y A H R P I
# 示例 3：
# 输入：s = "A", numRows = 1 输出："A"
# 提示：
# 1 <= s.length <= 1000
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1 <= numRows <= 1000


#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#
# https://leetcode-cn.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (44.51%)
# Likes:    373
# Dislikes: 0
# Total Accepted:    53.1K
# Total Submissions: 119.4K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# 
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 
# 
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 
# 请你实现这个将字符串进行指定行数变换的函数：
# 
# string convert(string s, int numRows);
# 
# 示例 1:
# 
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 
# 
# 示例 2:
# 
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
# 
#

'''
[
[L   C   I   R]
[E T O E S I I G]
[E   D   H   N]
]

'''

class Solution(object):
    def convert(self, s, numRows):
        if not s:
            return ''

        if len(s) <= numRows or numRows==1:
            return s 

        row = 0
        grid = [[] for _ in range(numRows)]
        going_down = 1
        for i in s:
            # print(row)
            grid[row].append(i)
            row += going_down 
            if (row == 0) or (row == numRows - 1):
                going_down = -1 * going_down
        # print(grid)
        return ''.join(''.join(i) for i in grid)

    def convert_v1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        numRows * list_length * (numRows-2/numRows-1) * (numRows-1/numRows) + letter_count = numRows * list_length
        list_length * (numRows-2) + letter_count = numRows * list_length
        list_length = letter_count / ( numRows - numRows + 2)
        """
        if not s:
            return ''

        if len(s) <= numRows or numRows==1:
            return s 

        x = 0
        y = 0
        z_flag = False
        count = numRows - 1
        # route = []
        list_length =  len(s) // 2 + 1
        # print(list_length)
        grid = [['' for _ in range(int(list_length))] for _ in range(numRows)]
        # print(grid)
        for idx, i in enumerate(s):
            grid[x][y] = i
            z_flag = (idx // count) & 1 
            x, y = self.next_point(x, y, z_flag, count)
        # print(grid)
        return ''.join(''.join(i) for i in grid)

    def next_point(self, x, y, z_flag, count):
        if z_flag:
            if x > 1:
                return x-1, y+1
            else:
                return 0, y+1
        else:
            return x+1, y

if __name__ == "__main__":
    s = Solution().convert("LEETCODEISHIRING", 3)
    print(s)
    s = Solution().convert("czawtmojhtslcnfdpffakysphqssrwfvyhsttgcacvngkvkzarbmpvby", 45)
    print(s)
    # import timeit 
    # costs = timeit.Timer('Solution().convert("czawtmojhtslcnfdpffakysphqssrwfvyhsttgcacvngkvkzarbmpvby", 45)', setup='from __main__ import Solution').repeat(7, 1000) 
    # print(sum(costs) / len(costs))
    # costs = timeit.Timer('Solution().convert_v1("czawtmojhtslcnfdpffakysphqssrwfvyhsttgcacvngkvkzarbmpvby", 45)', setup='from __main__ import Solution').repeat(7, 1000) 
    # print(sum(costs) / len(costs))
