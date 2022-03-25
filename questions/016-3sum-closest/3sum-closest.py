# -*- coding:utf-8 -*-

# <SUBID:21372919,UPDATE:20220325>
# English:
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1 Output: 2 Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:
# Input: nums = [0,0,0], target = 1 Output: 0
# Constraints:
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104
#
# 中文:
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。
# 示例 1：
# 输入：nums = [-1,2,1,-4], target = 1 输出：2 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 示例 2：
# 输入：nums = [0,0,0], target = 1 输出：0
# 提示：
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104


#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (40.04%)
# Likes:    203
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 71K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # v1 暴力法 超时
        # from itertools import combinations
        # ans = 2 ** 31
        # ret = None
        # for a, b, c in combinations(nums, 3):
        #     tmp = abs(a+b+c-target)
        #     if tmp < ans:
        #         ret = a + b + c
        #         ans = tmp
        # return ret

        nums.sort()
        gap = 2 ** 31
        ans = None
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp > target:
                    k -= 1
                else:
                    j += 1
                tmp2 = abs(tmp - target)
                if tmp2 < gap:
                    gap = tmp2
                    ans = tmp
        return ans

if __name__ == "__main__":
    s = Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1)
    print(s)


