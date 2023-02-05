# -*- coding:utf-8 -*-

# <SUBID:314329470,UPDATE:20230205>
# English:
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
# Example 1:
# Input: nums = [1,3,4,2,2] Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2] Output: 3
# Constraints:
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
# Follow up:
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
#
# 中文:
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
# 示例 1：
# 输入：nums = [1,3,4,2,2] 输出：2
# 示例 2：
# 输入：nums = [3,1,3,4,2] 输出：3
# 提示：
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
# 进阶：
# 如何证明 nums 中至少存在一个重复的数字?
# 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？



class SolutionB:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        原地排序法, 优化

        不对, 因为修改了原数组
        """

        i = 0
        while i < len(nums):
            if nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                if nums[i] != i+1:
                    break
                i += 1
        return nums[i]

class SolutionA:
    def findDuplicate(self, nums: List[int]) -> int:
        """数学法

        结果不对, 题目是至少存在一个重复, 而不是刚好存在一个重复"""
        total = len(nums) * (len(nums)-1) // 2
        return sum(nums) - total

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        快慢指针法
        """
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

