# -*- coding:utf-8 -*-

# <SUBID:319123708,UPDATE:20230205>
# English:
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4 Output: 12.75000 Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:
# Input: nums = [5], k = 1 Output: 5.00000
# Constraints:
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104
#
# 中文:
# 给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
# 请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
# 任何误差小于 10-5 的答案都将被视为正确答案。
# 示例 1：
# 输入：nums = [1,12,-5,-6,50,3], k = 4 输出：12.75 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 示例 2：
# 输入：nums = [5], k = 1 输出：5.00000
# 提示：
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


class Solution(object):
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """模拟队列, 用一个字段模拟队列总和, 模拟入队出队操作
        """
        if len(nums) == 0:
            return
        tmp = 0
        k = float(k)
        ans = float('-inf')
        total = 0
        for idx, i in enumerate(nums):
            if tmp < k:
                tmp += 1
                total += i
                ans = total
            else:
                total += i   # 模拟入队和出队
                total -= nums[idx-tmp]
                ans = max(ans, total)
        return ans / k

