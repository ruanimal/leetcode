# -*- coding:utf-8 -*-

# <SUBID:319665522,UPDATE:20230205>
# English:
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.
# Example 1:
# Input: nums = [4,2,5,7] Output: [4,5,2,7] Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:
# Input: nums = [2,3] Output: [2,3]
# Constraints:
# 2 <= nums.length <= 2 * 104
# nums.length is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000
# Follow Up: Could you solve it in-place?
#
# 中文:
# 给定一个非负整数数组 nums，  nums 中一半整数是 奇数 ，一半整数是 偶数 。
# 对数组进行排序，以便当 nums[i] 为奇数时，i 也是 奇数 ；当 nums[i] 为偶数时， i 也是 偶数 。
# 你可以返回 任何满足上述条件的数组作为答案 。
# 示例 1：
# 输入：nums = [4,2,5,7] 输出：[4,5,2,7] 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
# 示例 2：
# 输入：nums = [2,3] 输出：[2,3]
# 提示：
# 2 <= nums.length <= 2 * 104
# nums.length 是偶数
# nums 中一半是偶数
# 0 <= nums[i] <= 1000
# 进阶：可以不使用额外空间解决问题吗？


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            while (nums[i] % 2) == 0:
                i += 2
                if i >= len(nums):
                    return nums
            while (nums[j] % 2) == 1:
                j += 2
                if j >= len(nums):
                    return nums
            # print(i, j)
            nums[i], nums[j] = nums[j], nums[i]
        return nums
