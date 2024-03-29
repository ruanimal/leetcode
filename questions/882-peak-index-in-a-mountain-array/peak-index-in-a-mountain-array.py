# -*- coding:utf-8 -*-

# <SUBID:319557503,UPDATE:20230205>
# English:
# An array arr a mountain if the following properties hold:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# You must solve it in O(log(arr.length)) time complexity.
# Example 1:
# Input: arr = [0,1,0] Output: 1
# Example 2:
# Input: arr = [0,2,1,0] Output: 1
# Example 3:
# Input: arr = [0,10,5,2] Output: 1
# Constraints:
# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.
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


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        二分查找, 移动边界
        """
        left = 1
        right = len(arr)-1
        while left <= right:
            mid = (left+right) >> 1
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                left = mid+1
            elif arr[mid-1] > arr[mid] > arr[mid+1]:
                right = mid-1
            else:
                return mid
        return -1
