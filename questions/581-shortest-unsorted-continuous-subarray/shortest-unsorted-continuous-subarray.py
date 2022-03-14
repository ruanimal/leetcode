# -*- coding:utf-8 -*-


# English:
# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
# Return the shortest such subarray and output its length.
# Example 1:
# Input: nums = [2,6,4,8,10,9,15] Output: 5 Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:
# Input: nums = [1,2,3,4] Output: 0
# Example 3:
# Input: nums = [1] Output: 0
# Constraints:
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# Follow up: Can you solve it in O(n) time complexity?
#
# 中文:
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 请你找出符合题意的 最短 子数组，并输出它的长度。
# 示例 1：
# 输入：nums = [2,6,4,8,10,9,15] 输出：5 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 示例 2：
# 输入：nums = [1,2,3,4] 输出：0
# 示例 3：
# 输入：nums = [1] 输出：0
# 提示：
# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？


#
# @lc app=leetcode.cn id=581 lang=python
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (31.75%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 15.8K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
#
# 说明 :
#
#
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
#
#
#
class Solution:
    def findUnsortedSubarray(self, nums):
        # 排序法复杂度nlogn, 简洁
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return len(diff) and max(diff) - min(diff) + 1


if __name__ == "__main__":
    s = Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
    print(s)
    s = Solution().findUnsortedSubarray([2, 6])
    print(s)
    s = Solution().findUnsortedSubarray([2, 6, 1])
    print(s)
    # s = Solution().findUnsortedSubarray([2])
    # print(s)
    # s = Solution().findUnsortedSubarray([2, 1])
    # print(s)


