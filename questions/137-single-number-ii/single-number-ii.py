# -*- coding:utf-8 -*-


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
# 示例 1：
# 输入：nums = [2,2,3,2] 输出：3
# 示例 2：
# 输入：nums = [0,1,0,1,0,1,99] 输出：99
# 提示：
# 1 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
# 进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？


#
# @lc app=leetcode.cn id=137 lang=python
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (64.42%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 16K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,3,2]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
#
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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


if __name__ == "__main__":
    s = Solution().singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
    print(s)


