# -*- coding:utf-8 -*-

# <SUBID:319964896,UPDATE:20230205>
# English:
# Given an integer array nums and an integer k, modify the array in the following way:
# choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the same index i multiple times.
# Return the largest possible sum of the array after modifying it in this way.
# Example 1:
# Input: nums = [4,2,3], k = 1 Output: 5 Explanation: Choose index 1 and nums becomes [4,-2,3].
# Example 2:
# Input: nums = [3,-1,0,2], k = 3 Output: 6 Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
# Example 3:
# Input: nums = [2,-3,-1,5,-4], k = 2 Output: 13 Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
# Constraints:
# 1 <= nums.length <= 104
# -100 <= nums[i] <= 100
# 1 <= k <= 104
#
# 中文:
# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
# 以这种方式修改数组后，返回数组 可能的最大和 。
# 示例 1：
# 输入：nums = [4,2,3], k = 1 输出：5 解释：选择下标 1 ，nums 变为 [4,-2,3] 。
# 示例 2：
# 输入：nums = [3,-1,0,2], k = 3 输出：6 解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
# 示例 3：
# 输入：nums = [2,-3,-1,5,-4], k = 2 输出：13 解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
# 提示：
# 1 <= nums.length <= 104
# -100 <= nums[i] <= 100
# 1 <= k <= 104


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if not nums or not k:
            return 0

        neg_nums = [i for i in nums if i < 0]
        pos_nums = [i for i in nums if i >= 0]
        neg_nums.sort()
        pos_nums.sort()
        if k <= len(neg_nums):
            return -sum(neg_nums[:k]) + sum(neg_nums[k:]) + sum(pos_nums)
        k -= len(neg_nums)
        if k % 2 == 1:   # 奇数
            # 负数的最大值和正数的最小值二选一
            if pos_nums and neg_nums:
                return -sum(neg_nums[:-1]) + sum(pos_nums[1:]) + max(neg_nums[-1]+pos_nums[0], -neg_nums[-1]-pos_nums[0])
            elif pos_nums:  # 只有正数
                return -pos_nums[0] + sum(pos_nums[1:])
            else:
                return -sum(neg_nums[:-1]) + neg_nums[-1]
        return -sum(neg_nums) + sum(pos_nums)

