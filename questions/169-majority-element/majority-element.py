# -*- coding:utf-8 -*-

# <SUBID:311896817,UPDATE:20230205>
# English:
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example 1:
# Input: nums = [3,2,3] Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2] Output: 2
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#
# 中文:
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例 1：
# 输入：nums = [3,2,3] 输出：3
# 示例 2：
# 输入：nums = [2,2,1,1,1,2,2] 输出：2
# 提示：
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。


#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (56.58%)
# Total Accepted:    32K
# Total Submissions: 54.7K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#
#


class Solution(object):
    def majorityElement(self, nums: list) -> int:
        """
        哈希计数法
        """
        n = len(nums)
        if n == 1 or (n == 2 and nums[0] == nums[1]):
            return nums[0]

        count_map = {}
        for i in nums:
            v = count_map.get(i, 0) + 1
            if v > (n // 2):
                return i
            count_map[i] = v


