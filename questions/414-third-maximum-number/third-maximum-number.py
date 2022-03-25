# -*- coding:utf-8 -*-

# <SUBID:15988115,UPDATE:20220325>
# English:
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
# Example 1:
# Input: nums = [3,2,1] Output: 1 Explanation: The first distinct maximum is 3. The second distinct maximum is 2. The third distinct maximum is 1.
# Example 2:
# Input: nums = [1,2] Output: 2 Explanation: The first distinct maximum is 2. The second distinct maximum is 1. The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: nums = [2,2,3,1] Output: 1 Explanation: The first distinct maximum is 3. The second distinct maximum is 2 (both 2's are counted together since they have the same value). The third distinct maximum is 1.
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
# Follow up: Can you find an O(n) solution?
#
# 中文:
# 给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
# 示例 1：
# 输入：[3, 2, 1] 输出：1 解释：第三大的数是 1 。
# 示例 2：
# 输入：[1, 2] 输出：2 解释：第三大的数不存在, 所以返回最大的数 2 。
# 示例 3：
# 输入：[2, 2, 3, 1] 输出：1 解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。 此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
# 提示：
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
# 进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？


#
# @lc app=leetcode.cn id=414 lang=python
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (30.60%)
# Total Accepted:    6.4K
# Total Submissions: 20.7K
# Testcase Example:  '[3,2,1]'
#
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
#
# 示例 1:
#
#
# 输入: [3, 2, 1]
#
# 输出: 1
#
# 解释: 第三大的数是 1.
#
#
# 示例 2:
#
#
# 输入: [1, 2]
#
# 输出: 2
#
# 解释: 第三大的数不存在, 所以返回最大的数 2 .
#
#
# 示例 3:
#
#
# 输入: [2, 2, 3, 1]
#
# 输出: 1
#
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。
#
#
#
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None
        for i in nums:
            if i in (first, second, third): continue
            if first == None or i >= first:
                first, second, third = i, first, second
            elif second == None or i >= second:
                second, third = i, second
            elif third == None or i >= third:
                third = i
        return third if third is not None else first


