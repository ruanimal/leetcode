# -*- coding:utf-8 -*-


# English:
# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Example 1:
# Input: arr = [2,1] Output: false
# Example 2:
# Input: arr = [3,5,5] Output: false
# Example 3:
# Input: arr = [0,3,2,1] Output: true
# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104
#
# 中文:
# 给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。
# 让我们回顾一下，如果 arr 满足下述条件，那么它是一个山脉数组：
# arr.length >= 3
# 在 0 < i < arr.length - 1 条件下，存在 i 使得：
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# 示例 1：
# 输入：arr = [2,1] 输出：false
# 示例 2：
# 输入：arr = [3,5,5] 输出：false
# 示例 3：
# 输入：arr = [0,3,2,1] 输出：true
# 提示：
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104


#
# @lc app=leetcode.cn id=941 lang=python
#
# [941] 有效的山脉数组
#
# https://leetcode-cn.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (33.00%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 9.7K
# Testcase Example:  '[2,1]'
#
# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
#
# 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
#
#
# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在 i 使得：
#
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]
#
#
#
#
#
#
# 示例 1：
#
# 输入：[2,1]
# 输出：false
#
#
# 示例 2：
#
# 输入：[3,5,5]
# 输出：false
#
#
# 示例 3：
#
# 输入：[0,3,2,1]
# 输出：true
#
#
#
# 提示：
#
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 
#
#
#
#
#
#
#
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3:
            return False
        peak_cnt = 0
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                peak_cnt += 1
            elif A[i-1] < A[i] < A[i+1] or A[i-1] > A[i] > A[i+1]:
                continue
            else:
                return False
        return peak_cnt == 1

if __name__ == "__main__":
    s = Solution().validMountainArray([1,1,1])
    print(s)
    s = Solution().validMountainArray([1,2,1])
    print(s)
    s = Solution().validMountainArray([1,2,1,1,1])
    print(s)
    s = Solution().validMountainArray([0,1,2,1,2])
    print(s)
    s = Solution().validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3])
    print(s)


