# -*- coding:utf-8 -*-


# English:
# Let's call an array arr a mountain if the following properties hold:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# Example 1:
# Input: arr = [0,1,0] Output: 1
# Example 2:
# Input: arr = [0,2,1,0] Output: 1
# Example 3:
# Input: arr = [0,10,5,2] Output: 1
# Constraints:
# 3 <= arr.length <= 104
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.
# Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?
#
# 中文:
# 符合下列属性的数组 arr 称为 山脉数组 ：
# arr.length >= 3
# 存在 i（0 < i < arr.length - 1）使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。
# 示例 1：
# 输入：arr = [0,1,0] 输出：1
# 示例 2：
# 输入：arr = [0,2,1,0] 输出：1
# 示例 3：
# 输入：arr = [0,10,5,2] 输出：1
# 示例 4：
# 输入：arr = [3,4,5,1] 输出：2
# 示例 5：
# 输入：arr = [24,69,100,99,79,78,67,36,26,19] 输出：2
# 提示：
# 3 <= arr.length <= 104
# 0 <= arr[i] <= 106
# 题目数据保证 arr 是一个山脉数组
# 进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？


#
# @lc app=leetcode.cn id=852 lang=python
#
# [852] 适龄的朋友
#
# https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Easy (66.29%)
# Total Accepted:    9.5K
# Total Submissions: 14.2K
# Testcase Example:  '[0,1,0]'
#
# 我们把符合下列属性的数组 A 称作山脉：
#
#
# A.length >= 3
# 存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... >
# A[A.length - 1]
#
#
# 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... >
# A[A.length - 1] 的 i 的值。
#
#
#
# 示例 1：
#
# 输入：[0,1,0]
# 输出：1
#
#
# 示例 2：
#
# 输入：[0,2,1,0]
# 输出：1
#
#
#
# 提示：
#
#
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A 是如上定义的山脉
#
#
#
#
#
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        折半, 移动边界
        """
        left = 0
        right = len(A)-1
        while left <= right:
            mid = (left+right)//2
            if A[mid-1] < A[mid] < A[mid+1]:
                left = mid+1
            elif A[mid-1] > A[mid] > A[mid+1]:
                right = mid-1
            else:
                return mid
        return -1

if __name__ == "__main__":
    d = [0,2,1,0]
    s = Solution().peakIndexInMountainArray(d)
    print(s)

