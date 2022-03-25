# -*- coding:utf-8 -*-

# <SUBID:21414966,UPDATE:20220325>
# English:
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1
# Example 3:
# Input: nums = [1], target = 0 Output: -1
# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104
#
# 中文:
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
# 示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0 输出：4
# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3 输出：-1
# 示例 3：
# 输入：nums = [1], target = 0 输出：-1
# 提示：
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
# 进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？


#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.49%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 77.3K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i+j) // 2
            if nums[i] < nums[mid]:
                i = mid
            else:
                j = mid
        if nums[i] > nums[i+1]:   # 处理不旋转的情况
            offset = i + 1
            nums = nums[offset:] + nums[:offset]
        else:
            offset = 0
        # print(nums, offset)
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif target < nums[mid]:
                j = mid - 1
            else:
                return (mid + offset) % len(nums)   # 处理偏移后数值过大
        return -1

if __name__ == "__main__":
    s = Solution().search([4,5,6,7,0,1,2], target=3)
    print(s)
    s = Solution().search([4,5,6,7,8,0,1,2], target=0)
    print(s)
    s = Solution().search([1,2,4,5,6,7,8,0,], target=0)
    print(s)
    s = Solution().search([1,0,], target=0)
    print(s)
    s = Solution().search([3, 1], target=3)
    print(s)


