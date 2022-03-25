# -*- coding:utf-8 -*-

# <SUBID:16857753,UPDATE:20220325>
# English:
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Example 1:
# Input: nums = [-4,-1,0,3,10] Output: [0,1,9,16,100] Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].
# Example 2:
# Input: nums = [-7,-3,2,3,11] Output: [4,9,9,49,121]
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
#
# 中文:
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 示例 1：
# 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100] 解释：平方后，数组变为 [16,1,0,9,100] 排序后，数组变为 [0,1,9,16,100]
# 示例 2：
# 输入：nums = [-7,-3,2,3,11] 输出：[4,9,9,49,121]
# 提示：
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums 已按 非递减顺序 排序
# 进阶：
# 请你设计时间复杂度为 O(n) 的算法解决本问题


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


