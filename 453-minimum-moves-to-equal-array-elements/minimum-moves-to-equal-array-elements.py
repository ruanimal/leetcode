# -*- coding:utf-8 -*-


# English:
# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
# Example:
# Input: [1,2,3] Output: 3 Explanation: Only three moves are needed (remember each move increments two elements): [1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]
#
# 中文:
# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。
# 示例:
# 输入: [1,2,3] 输出: 3 解释: 只需要3次移动（注意每次移动会增加两个元素的值）： [1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]


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


