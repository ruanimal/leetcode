# -*- coding:utf-8 -*-


# English:
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
# Example 1:
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]. Output: [-1,3,-1] Explanation: For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1. For number 1 in the first array, the next greater number for it in the second array is 3. For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
# Example 2:
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]. Output: [3,-1] Explanation: For number 2 in the first array, the next greater number for it in the second array is 3. For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
# Note:
#
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
#
# 中文:
# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
# 示例 1:
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2]. 输出: [-1,3,-1] 解释: 对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。 对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。 对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
# 示例 2:
# 输入: nums1 = [2,4], nums2 = [1,2,3,4]. 输出: [3,-1] 解释:   对于num1中的数字2，第二个数组中的下一个较大数字是3。 对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
# 注意:
# nums1和nums2中所有元素是唯一的。
# nums1和nums2 的数组大小都不超过1000。


#
# @lc app=leetcode.cn id=496 lang=python
#
# [496] 下一个更大元素 I
#
# https://leetcode-cn.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (57.06%)
# Total Accepted:    6.7K
# Total Submissions: 11.6K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# 给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2
# 中的下一个比其大的值。
#
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
#
# 示例 1:
#
#
# 输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
# 输出: [-1,3,-1]
# 解释:
# ⁠   对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
# ⁠   对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
# ⁠   对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
#
# 示例 2:
#
#
# 输入: nums1 = [2,4], nums2 = [1,2,3,4].
# 输出: [3,-1]
# 解释:
# 对于num1中的数字2，第二个数组中的下一个较大数字是3。
# ⁠   对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
#
#
# 注意:
#
#
# nums1和nums2中所有元素是唯一的。
# nums1和nums2 的数组大小都不超过1000。
#
#
#
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums2 or not nums1:
            return

        stack = []
        next_max_map = {}
        stack.append(nums2[0])
        for i in nums2[1:]:
            while stack and (i > stack[-1]):
                next_max_map[stack.pop()] = i
            stack.append(i)
        return [next_max_map.get(i, -1) for i in nums1]

if __name__ == "__main__":
    print(Solution().nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
    print(Solution().nextGreaterElement([2,4], [1,2,3,4]))

