# -*- coding:utf-8 -*-


# English:
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:
# Input: [1, 5, 11, 5] Output: true Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
# Input: [1, 2, 3, 5] Output: false Explanation: The array cannot be partitioned into equal sum subsets.
#
# 中文:
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 注意:
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 示例 1:
# 输入: [1, 5, 11, 5] 输出: true 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 示例 2:
# 输入: [1, 2, 3, 5] 输出: false 解释: 数组不能分割成两个元素和相等的子集.


#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (38.15%)
# Total Accepted:    3.3K
# Total Submissions: 8.3K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
#
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
#
#
# 示例 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#
#
#
#
# 示例 2:
#
# 输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
#
#
#
#
#
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        1. f[x], 使用给定长度为n的数组nums里的元素能不能拼出x；
            最后一步有2种情况,
                前面已经拼出x了， nums[:n] 能拼出 f[x]
                前面没有拼出x,  nums[n] == x 则能拼出， 或者看nums[:n]能不能拼出(f[x-nums[n]])
        2. f[x] = (nums[n] == x ) or f[x-nums[n]]
        3. x < 0 则false
        """
        if len(nums) <= 1:
            return False

        sum_nums = sum(nums)
        if (sum_nums & 1) == 1:
            return False
        target = sum_nums // 2
        f = [{} for _ in range(len(nums))]
        f[0] = {i:(nums[0] == i) for i in range(target+1)}

        # print(f)
        for n in range(1, len(nums)):
            for x in range(target+1):
                if (nums[n] == x):
                    f[n][x] = True
                else:
                    f[n][x] = f[n-1][x] or f[n-1].get(x-nums[n], False)
            # print(f)
        return f[len(nums)-1][target]

if __name__ == "__main__":
    s = Solution().canPartition([1, 5, 11, 5])
    print(s)
    s = Solution().canPartition([1, 2, 3, 5])
    print(s)
    s = Solution().canPartition([1, 2, 5])
    print(s)
    s = Solution().canPartition([2, 2, 3, 5])
    print(s)

