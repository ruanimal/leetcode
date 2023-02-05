# -*- coding:utf-8 -*-

# <SUBID:314281776,UPDATE:20230205>
# English:
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
# Example 1:
# Input: nums = [0,1,0,3,12] Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0] Output: [0]
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
# Follow up: Could you minimize the total number of operations done?
#
# 中文:
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 示例 1:
# 输入: nums = [0,1,0,3,12] 输出: [1,3,12,0,0]
# 示例 2:
# 输入: nums = [0] 输出: [0]
# 提示:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
# 进阶：你能尽量减少完成的操作次数吗？




class SolutionA(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        暴力法
        """
        end = len(nums) - 1
        x = 0
        while x < end:
            if nums[x] == 0:
                del nums[x]
                nums.append(0)
                x -= 1
                end -= 1
            x += 1

class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        双指针法
        """

        p1 = 0   # 非0区间末尾
        p2 = 0   # 未判断区间开头
        while p2 < len(nums):
            if (nums[p2] != 0):
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1

