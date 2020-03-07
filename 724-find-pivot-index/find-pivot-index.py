# -*- coding:utf-8 -*-


# English:
# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
# Example 1:
# Input: nums = [1, 7, 3, 6, 5, 6] Output: 3 Explanation: The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3. Also, 3 is the first index where this occurs.
# Example 2:
# Input: nums = [1, 2, 3] Output: -1 Explanation: There is no index that satisfies the conditions in the problem statement.
# Note:
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].
#
# 中文:
# 给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
# 我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
# 示例 1:
# 输入: nums = [1, 7, 3, 6, 5, 6] 输出: 3 解释: 索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。 同时, 3 也是第一个符合要求的中心索引。
# 示例 2:
# 输入: nums = [1, 2, 3] 输出: -1 解释: 数组中不存在满足此条件的中心索引。
# 说明:
# nums 的长度范围为 [0, 10000]。
# 任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。


#
# @lc app=leetcode.cn id=724 lang=python
#
# [724] 寻找数组的中心索引
#
# https://leetcode-cn.com/problems/find-pivot-index/description/
#
# algorithms
# Easy (34.76%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    11.1K
# Total Submissions: 31.6K
# Testcase Example:  '[1,7,3,6,5,6]'
#
# 给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
#
# 我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
#
# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
#
# 示例 1:
#
#
# 输入:
# nums = [1, 7, 3, 6, 5, 6]
# 输出: 3
# 解释:
# 索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
# 同时, 3 也是第一个符合要求的中心索引。
#
#
# 示例 2:
#
#
# 输入:
# nums = [1, 2, 3]
# 输出: -1
# 解释:
# 数组中不存在满足此条件的中心索引。
#
# 说明:
#
#
# nums 的长度范围为 [0, 10000]。
# 任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。
#
#
#
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # v1 用到了浮点数的比较, 不太好
        # s = sum(nums)
        # half = s / 2.0
        # tmp = 0
        # for idx, i in enumerate(nums):
        #     if tmp + i/2.0 == half:
        #         return idx
        #         break
        #     tmp += i
        # return -1

        s = sum(nums)
        tmp = 0
        for idx, i in enumerate(nums):
            if 2 * tmp + i == s:
                return idx
            tmp += i
        return -1

if __name__ == "__main__":
    s = Solution().pivotIndex([1, 7, 3, 6, 5, 6])
    print(s)
    s = Solution().pivotIndex([1,2,2])
    print(s)
    s = Solution().pivotIndex([1,2,1])
    print(s)
    s = Solution().pivotIndex([1])
    print(s)
    s = Solution().pivotIndex([])
    print(s)
    s = Solution().pivotIndex([-1,-1,-1,-1,-1,0])
    print(s)

