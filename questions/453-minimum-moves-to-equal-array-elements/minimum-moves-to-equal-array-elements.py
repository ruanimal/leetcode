# -*- coding:utf-8 -*-

# <SUBID:315986624,UPDATE:20230205>
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


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        已知：长度为n的数组nums， 每次移动有n-1个元素增加1
        求：数组元素都相等时，最小移动次数x

        假设所有元素都相等时数字为k, 如果最小数字经过x次移动能够等于k, 则此时所有元素也能等于k, 此时移动次数为k-min(nums).
        则有方程: 数组元素总和增加量 = 终止时数组元素总和 - 开始时数组元素总和
        即方程: (k-min(nums)) * (n-1) = k * n - sum(nums)
        求解后: k = sum(nums) - min(nums) * (n-1)
        则可以得到最小移动次数  k-min(nums)
        """
        min_val = min(nums)
        n = len(nums)
        k = sum(nums) - min_val * (n-1)
        return k - min_val
