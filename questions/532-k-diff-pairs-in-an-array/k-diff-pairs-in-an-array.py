# -*- coding:utf-8 -*-

# <SUBID:317770201,UPDATE:20230205>
# English:
# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k
# Notice that |val| denotes the absolute value of val.
# Example 1:
# Input: nums = [3,1,4,1,5], k = 2 Output: 2 Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5). Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
# Input: nums = [1,2,3,4,5], k = 1 Output: 4 Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
# Input: nums = [1,3,1,5,4], k = 0 Output: 1 Explanation: There is one 0-diff pair in the array, (1, 1).
# Constraints:
# 1 <= nums.length <= 104
# -107 <= nums[i] <= 107
# 0 <= k <= 107
#
# 中文:
# 给你一个整数数组 nums 和一个整数 k，请你在数组中找出 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。
# k-diff 数对定义为一个整数对 (nums[i], nums[j]) ，并满足下述全部条件：
# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k
# 注意，|val| 表示 val 的绝对值。
# 示例 1：
# 输入：nums = [3, 1, 4, 1, 5], k = 2 输出：2 解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。 尽管数组中有两个 1 ，但我们只应返回不同的数对的数量。
# 示例 2：
# 输入：nums = [1, 2, 3, 4, 5], k = 1 输出：4 解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5) 。
# 示例 3：
# 输入：nums = [1, 3, 1, 5, 4], k = 0 输出：1 解释：数组中只有一个 0-diff 数对，(1, 1) 。
# 提示：
# 1 <= nums.length <= 104
# -107 <= nums[i] <= 107
# 0 <= k <= 107



from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """hash计数法
        """
        if k < 0:
            return 0

        nums_set = Counter(nums)

        if k == 0:
            return sum(1 for _, v in nums_set.items() if v >= 2)

        ans = 0
        for i in nums_set:
            if (i - k) in nums_set:
                ans += 1
        return ans

