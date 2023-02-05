# -*- coding:utf-8 -*-

# <SUBID:318210156,UPDATE:20230205>
# English:
# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7] Output: 5 Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Example 2:
# Input: nums = [1,2,3,4] Output: 2
# Example 3:
# Input: nums = [1,1,1,1] Output: 0
# Constraints:
# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109
#
# 中文:
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
# 现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
# 数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。
# 示例 1：
# 输入：nums = [1,3,2,2,5,2,3,7] 输出：5 解释：最长的和谐子序列是 [3,2,2,2,3]
# 示例 2：
# 输入：nums = [1,2,3,4] 输出：2
# 示例 3：
# 输入：nums = [1,1,1,1] 输出：0
# 提示：
# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109



class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """计数排序法

        如果排序后相邻的数字之差为1, 则长度就是这两个数字个数之和
        """
        from collections import Counter

        if not nums:
            return 0
        counter = Counter(nums)
        counter_list = sorted(counter.items(), key=lambda i: i[0])
        max_val = 0
        for i in range(1, len(counter_list)):
            a, b = counter_list[i-1], counter_list[i]
            if (b[0]-a[0]) != 1:
                continue
            max_val = max(max_val, a[1] + b[1])
        return max_val

