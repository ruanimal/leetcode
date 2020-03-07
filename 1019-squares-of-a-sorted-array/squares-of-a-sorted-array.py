# -*- coding:utf-8 -*-


# English:
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
# Example 1:
# Input: [-4,-1,0,3,10] Output: [0,1,9,16,100]
# Example 2:
# Input: [-7,-3,2,3,11] Output: [4,9,9,49,121]
# Note:
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
#
# 中文:
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
# 示例 1：
# 输入：[-4,-1,0,3,10] 输出：[0,1,9,16,100]
# 示例 2：
# 输入：[-7,-3,2,3,11] 输出：[4,9,9,49,121]
# 提示：
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。


#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 不同的子序列 II
#
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (74.92%)
# Total Accepted:    10.4K
# Total Submissions: 14.5K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
#
#
# 示例 1：
#
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
#
#
# 示例 2：
#
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。
#
#
#
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        neg_stack = []
        res = []
        for i in range(len(A)):
            if A[i] < 0:
                neg_stack.append(-A[i])
            else:
                A = A[i:]
                break
        else:
            A = []

        j = 0
        # print(neg_stack, A)
        while neg_stack and j < len(A):
            if A[j] < neg_stack[-1]:
                res.append(A[j] ** 2)
                j += 1
            else:
                res.append(neg_stack.pop() ** 2)
        while neg_stack:
            res.append(neg_stack.pop() ** 2)
        while j < len(A):
            res.append(A[j] ** 2)
            j += 1
        return res


if __name__ == "__main__":
    d = [-4,-1,0,3,10]
    d = [-4,-1]
    s = Solution().sortedSquares(d)
    print(s)


