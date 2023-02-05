# -*- coding:utf-8 -*-

# <SUBID:15544888,UPDATE:20230205>
# English:
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# Example 1:
# Input: nums1 = [1,3], nums2 = [2] Output: 2.00000 Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4] Output: 2.50000 Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106
#
# 中文:
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
# 算法的时间复杂度应该为 O(log (m+n)) 。
# 示例 1：
# 输入：nums1 = [1,3], nums2 = [2] 输出：2.00000 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：
# 输入：nums1 = [1,2], nums2 = [3,4] 输出：2.50000 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 提示：
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106


#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (33.41%)
# Total Accepted:    35.3K
# Total Submissions: 105.6K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        进行一次归并, 然后求中位数
        """
        result = []
        l = r = 0
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                result.append(nums1[l])
                l += 1
            else:
                result.append(nums2[r])
                r += 1
        result += nums1[l:]
        result += nums2[r:]
        if len(result) % 2 == 1:
            return result[len(result)//2]
        else:
            return (result[len(result)//2-1]+result[len(result)//2])/2.0

