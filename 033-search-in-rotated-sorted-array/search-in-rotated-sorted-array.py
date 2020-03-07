# -*- coding:utf-8 -*-


# English:
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1
#
# 中文:
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。
# 示例 1:
# 输入: nums = [4,5,6,7,0,1,2], target = 0 输出: 4
# 示例 2:
# 输入: nums = [4,5,6,7,0,1,2], target = 3 输出: -1


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


