# -*- coding:utf-8 -*-

# <SUBID:319940010,UPDATE:20230205>
# English:
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
# Example 1:
# Input: nums = [2,1,2] Output: 5 Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
# Example 2:
# Input: nums = [1,2,1,10] Output: 0 Explanation: You cannot use the side lengths 1, 1, and 2 to form a triangle. You cannot use the side lengths 1, 1, and 10 to form a triangle. You cannot use the side lengths 1, 2, and 10 to form a triangle. As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
# Constraints:
# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106
#
# 中文:
# 给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回 0。
# 示例 1：
# 输入：nums = [2,1,2] 输出：5 解释：你可以用三个边长组成一个三角形:1 2 2。
# 示例 2：
# 输入：nums = [1,2,1,10] 输出：0 解释： 你不能用边长 1,1,2 来组成三角形。 不能用边长 1,1,10 来构成三角形。 不能用边长 1、2 和 10 来构成三角形。 因为我们不能用任何三条边长来构成一个非零面积的三角形，所以我们返回 0。
# 提示：
# 3 <= nums.length <= 104
# 1 <= nums[i] <= 106


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """两边之和大于第三边, 两边只差小于第三边"""

        if len(nums) < 3:
            return

        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if (nums[i] - nums[i+2] < nums[i+1] ) and (nums[i+1] + nums[i+2] > nums[i]):
                return nums[i] + nums[i+2] + nums[i+1]
        return 0
