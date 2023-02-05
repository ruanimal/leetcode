# -*- coding:utf-8 -*-

# <SUBID:311873342,UPDATE:20230205>
# English:
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,3,2] Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99] Output: 99
# Constraints:
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each element in nums appears exactly three times except for one element which appears once.
#
# 中文:
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法且不使用额外空间来解决此问题。
# 示例 1：
# 输入：nums = [2,2,3,2] 输出：3
# 示例 2：
# 输入：nums = [0,1,0,1,0,1,99] 输出：99
# 提示：
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次



class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        """
        统计二进制位, 只出现一次的数二进制位取余3不等于0
        """
        bits = [0 for _ in range(32)]
        flags = 0
        for num in nums:
            if num < 0:
                flags += 1
                num = abs(num)
            i = 31
            while num > 0:
                if num & 1 == 1:
                    bits[i] += 1
                num >>= 1
                i -= 1
        ans = 0
        for i in range(32):
            ans <<= 1
            if (bits[i] % 3) != 0:
                ans |= 1
        return ans if (flags % 3 == 0) else -ans

