# -*- coding:utf-8 -*-

# <SUBID:23465091,UPDATE:20220325>
# English:
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,1] Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2] Output: 4
# Example 3:
# Input: nums = [1] Output: 1
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.
#
# 中文:
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 示例 1:
# 输入: [2,2,1] 输出: 1
# 示例 2:
# 输入: [4,1,2,1,2] 输出: 4


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans ^= i 
        return ans 
