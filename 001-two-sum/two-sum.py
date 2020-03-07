# -*- coding:utf-8 -*-


# English:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
#
# 中文:
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9 因为 nums[0] + nums[1] = 2 + 7 = 9 所以返回 [0, 1]


#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (44.50%)
# Total Accepted:    309.9K
# Total Submissions: 680.5K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#
#
class Solution:
    def twoSum_v1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        构建hash, 一次遍历
        """
        tmp_dict = {e: index for index, e in enumerate(nums)}
        for index, e in enumerate(nums):
            t = target - e
            if t in tmp_dict and tmp_dict[t] != index:
                return [index, tmp_dict[t]]

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        遍历的同时构建hash
        """
        tmp_dict = {}
        for index, e in enumerate(nums):
            t = target - e
            if t in tmp_dict:
                return [index, tmp_dict[t]]
            tmp_dict[e] = index

