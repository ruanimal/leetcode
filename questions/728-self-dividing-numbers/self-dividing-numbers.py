# -*- coding:utf-8 -*-

# <SUBID:17658623,UPDATE:20220325>
# English:
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
# Example 1:
# Input: left = 1, right = 22 Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:
# Input: left = 47, right = 85 Output: [48,55,66,77]
# Constraints:
# 1 <= left <= right <= 104
#
# 中文:
# 自除数 是指可以被它包含的每一位数整除的数。
# 例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
# 自除数 不允许包含 0 。
# 给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数 。
# 示例 1：
# 输入：left = 1, right = 22 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# 示例 2:
# 输入：left = 47, right = 85 输出：[48,55,66,77]
# 提示：
# 1 <= left <= right <= 104


#
# @lc app=leetcode.cn id=728 lang=python
#
# [728] 自除数
#
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left, right+1):
            num_str = str(i)
            for j in num_str:
                if j == '0':
                    break
                if i % int(j) != 0:
                    break
            else:
                ret.append(i)
        return ret



