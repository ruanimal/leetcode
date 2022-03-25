# -*- coding:utf-8 -*-

# <SUBID:15987017,UPDATE:20220325>
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


#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (52.38%)
# Total Accepted:    39.6K
# Total Submissions: 74.4K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明:
#
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
#
#


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
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



