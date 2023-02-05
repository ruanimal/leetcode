# -*- coding:utf-8 -*-

# <SUBID:307944581,UPDATE:20230205>
# English:
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.
# Example 1:
# Input: nums = [1,2,3,1] Output: 2 Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
# Input: nums = [1,2,1,3,5,6,4] Output: 5 Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
# Constraints:
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.
#
# 中文:
# 峰值元素是指其值严格大于左右相邻值的元素。
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞ 。
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
# 示例 1：
# 输入：nums = [1,2,3,1] 输出：2 解释：3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2：
# 输入：nums = [1,2,1,3,5,6,4] 输出：1 或 5 解释：你的函数可以返回索引 1，其峰值元素为 2；   或者返回索引 5， 其峰值元素为 6。
# 提示：
# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# 对于所有有效的 i 都有 nums[i] != nums[i + 1]


class SolutionA:
    def findPeakElement(self, nums: List[int]) -> int:
        """暴力法, 求上升段的终点
        如果开始就是下降, 则起点就是峰值
        """

        if len(nums) == 1:
            return 0

        i = 0
        while i < len(nums)-1 and nums[i] < nums[i+1]:
            i += 1
        return i

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """二分法
        """

        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:   # 以下降开头
            return 0
        if nums[-2] < nums[-1]:  # 以上升结尾
            return len(nums)-1

        left = 0
        right = len(nums)-1-1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
