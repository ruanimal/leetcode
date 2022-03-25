# -*- coding:utf-8 -*-

# <SUBID:19088805,UPDATE:20220325>
# English:
# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
# In one move, you can increment n - 1 elements of the array by 1.
# Example 1:
# Input: nums = [1,2,3] Output: 3 Explanation: Only three moves are needed (remember each move increments two elements): [1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]
# Example 2:
# Input: nums = [1,1,1] Output: 0
# Constraints:
# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# The answer is guaranteed to fit in a 32-bit integer.
#
# 中文:
# 给你一个长度为 n 的整数数组，每次操作将会使 n - 1 个元素增加 1 。返回让数组所有元素相等的最小操作次数。
# 示例 1：
# 输入：nums = [1,2,3] 输出：3 解释： 只需要3次操作（注意每次操作会增加两个元素的值）： [1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]
# 示例 2：
# 输入：nums = [1,1,1] 输出：0
# 提示：
# n == nums.length
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 答案保证符合 32-bit 整数


#
# @lc app=leetcode.cn id=453 lang=python
#
# [453] 最小移动次数使数组元素相等
#
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        相等时数字为k, 则移动次数为k-min(nums), 每次移动数组和增加(n-1).
        以数组和增加量 = 终止时总和 - 开始时总和
        (k-min(nums)) * (len(nums)-1) = k * len(nums) - sum(nums)
        (len(nums)-1) * k - min(nums) * (len(nums)-1) = k * len(nums) - sum(nums)
        -k = min(nums) * (len(nums)-1) - sum(nums)
        k = sum(nums) - min(nums) * (len(nums)-1)
        """
        min_val = min(nums)
        k = sum(nums) - min_val * (len(nums)-1)
        return k - min_val

if __name__ == "__main__":
    s = Solution().minMoves([1,2,3])
    print(s)


