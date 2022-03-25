# -*- coding:utf-8 -*-

# <SUBID:16146378,UPDATE:20220325>
# English:
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2] Output: [-1,3,-1] Explanation: The next greater element for each value of nums1 is as follows: - 4 is underlined in nums2 = [1,3,
# 4
# ,2]. There is no next greater element, so the answer is -1. - 1 is underlined in nums2 = [
# 1
# ,3,4,2]. The next greater element is 3. - 2 is underlined in nums2 = [1,3,4,
# 2
# ]. There is no next greater element, so the answer is -1.
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4] Output: [3,-1] Explanation: The next greater element for each value of nums1 is as follows: - 2 is underlined in nums2 = [1,
# 2
# ,3,4]. The next greater element is 3. - 4 is underlined in nums2 = [1,2,3,
# 4
# ]. There is no next greater element, so the answer is -1.
# Constraints:
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 104
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.
# Follow up: Could you find an O(nums1.length + nums2.length) solution?
#
# 中文:
# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
# 示例 1：
# 输入：nums1 = [4,1,2], nums2 = [1,3,4,2]. 输出：[-1,3,-1] 解释：nums1 中每个值的下一个更大元素如下所述： - 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。 - 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。 - 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
# 示例 2：
# 输入：nums1 = [2,4], nums2 = [1,2,3,4]. 输出：[3,-1] 解释：nums1 中每个值的下一个更大元素如下所述： - 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。 - 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。
# 提示：
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 104
# nums1和nums2中所有整数 互不相同
# nums1 中的所有整数同样出现在 nums2 中
# 进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？


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

