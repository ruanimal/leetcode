# -*- coding:utf-8 -*-


# English:
# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
# Example 1:
# Input: nums = [1,3,5,4,7] Output: 3 Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3. Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element 4.
# Example 2:
# Input: nums = [2,2,2,2,2] Output: 1 Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly increasing.
# Constraints:
# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109
#
# 中文:
# 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
# 连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。
# 示例 1：
# 输入：nums = [1,3,5,4,7] 输出：3 解释：最长连续递增序列是 [1,3,5], 长度为3。 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。
# 示例 2：
# 输入：nums = [2,2,2,2,2] 输出：1 解释：最长连续递增序列是 [2], 长度为1。
# 提示：
# 1 <= nums.length <= 104
# -109 <= nums[i] <= 109


#
# @lc app=leetcode.cn id=674 lang=python
#
# [674] 最长连续递增序列
#
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (40.07%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 18.7K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
#
# 示例 1:
#
#
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
#
#
# 示例 2:
#
#
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
#
#
# 注意：数组长度不会超过10000。
#
#
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_count = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += 1
            else:
                # print(max_count, count)
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        return max_count

if __name__ == "__main__":
    # s = Solution().findLengthOfLCIS([3,1,2,3,4,2,5])
    # print(s)
    # s = Solution().findLengthOfLCIS([])
    # print(s)
    s = Solution().findLengthOfLCIS([1,1,1,1])
    print(s)



