# -*- coding:utf-8 -*-

# <SUBID:311872563,UPDATE:20230205>
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
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
# 示例 1 ：
# 输入：nums = [2,2,1] 输出：1
# 示例 2 ：
# 输入：nums = [4,1,2,1,2] 输出：4
# 示例 3 ：
# 输入：nums = [1] 输出：1
# 提示：
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# 除了某个元素只出现一次以外，其余每个元素均出现两次。



class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for i in nums:
            ret ^= i
        return ret

