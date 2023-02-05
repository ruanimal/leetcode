# -*- coding:utf-8 -*-

# <SUBID:307730366,UPDATE:20230205>
# English:
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8 Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6 Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0 Output: [-1,-1]
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109
#
# 中文:
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8 输出：[3,4]
# 示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6 输出：[-1,-1]
# 示例 3：
# 输入：nums = [], target = 0 输出：[-1,-1]
# 提示：
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums 是一个非递减数组
# -109 <= target <= 109


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        first = self.findFirst(nums, target)
        if first == -1:
            return [-1, -1]
        last = self.findLast(nums, target)
        return [first, last]

    @staticmethod
    def findLast(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right == -1:
            return -1
        if nums[right] != target:
            return -1
        return right

    @staticmethod
    def findFirst(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left == len(nums):
            return -1
        if nums[left] != target:
            return -1
        return left

