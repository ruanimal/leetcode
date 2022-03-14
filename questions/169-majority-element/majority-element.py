# -*- coding:utf-8 -*-


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
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例 1：
# 输入：[3,2,3] 输出：3
# 示例 2：
# 输入：[2,2,1,1,1,2,2] 输出：2
# 进阶：
# 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        
        c = Counter(nums)
        max_count = 0
        ans = None 
        
        for num, count in c.items():
            if count > max_count:
                ans = num 
                max_count = count
                
        if max_count > len(nums) // 2:
            return ans 
        
