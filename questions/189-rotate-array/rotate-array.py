# -*- coding:utf-8 -*-


# English:
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3 Output: [5,6,7,1,2,3,4] Explanation: rotate 1 steps to the right: [7,1,2,3,4,5,6] rotate 2 steps to the right: [6,7,1,2,3,4,5] rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2 Output: [3,99,-1,-100] Explanation: rotate 1 steps to the right: [99,-1,-100,3] rotate 2 steps to the right: [3,99,-1,-100]
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
# Follow up:
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
# 中文:
# 给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: nums = [1,2,3,4,5,6,7], k = 3 输出: [5,6,7,1,2,3,4] 解释: 向右轮转 1 步: [7,1,2,3,4,5,6] 向右轮转 2 步: [6,7,1,2,3,4,5] 向右轮转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
# 输入：nums = [-1,-100,3,99], k = 2 输出：[3,99,-1,-100] 解释: 向右轮转 1 步: [99,-1,-100,3] 向右轮转 2 步: [3,99,-1,-100]
# 提示：
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
# 进阶：
# 尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？


#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (35.93%)
# Total Accepted:    42.1K
# Total Submissions: 114.3K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
#
# 说明:
#
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。
#
#
#


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(k):
            tmp = nums.pop()
            nums.insert(0, tmp)

