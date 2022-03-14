# -*- coding:utf-8 -*-


# English:
# Given two arrays, write a function to compute their intersection.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2] Output: [2,2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] Output: [4,9]
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
#
# 中文:
# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2] 输出: [2,2]
# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4] 输出: [4,9]
# 说明：
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
# 进阶:
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？


#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (38.62%)
# Total Accepted:    28.9K
# Total Submissions: 71.8K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
#
#
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
#
# 说明：
#
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
#
#
# 进阶:
#
#
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
#
#
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return

        nums1.sort()
        nums2.sort()

        ret = []
        begin_j = 0
        for i in range(len(nums1)):
            j = begin_j
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    break
                elif nums1[i] == nums2[j]:
                    ret.append(nums1[i])
                    begin_j = j+1
                    break
                else:
                    j += 1
        return ret

if __name__ == "__main__":
    t = Solution().intersect(nums1 = [4,4,4,9,5,8], nums2 = [9,4,9,8,4])
    print(t)



