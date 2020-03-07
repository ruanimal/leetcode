# -*- coding:utf-8 -*-


# English:
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# Example 1:
# Input: [3,2,3] Output: 3
# Example 2:
# Input: [2,2,1,1,1,2,2] Output: 2
#
# 中文:
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例 1:
# 输入: [3,2,3] 输出: 3
# 示例 2:
# 输入: [2,2,1,1,1,2,2] 输出: 2


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
        
