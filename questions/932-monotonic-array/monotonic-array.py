# -*- coding:utf-8 -*-

# <SUBID:19751427,UPDATE:20220325>
# English:
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
# Example 1:
# Input: nums = [1,2,2,3] Output: true
# Example 2:
# Input: nums = [6,5,4,4] Output: true
# Example 3:
# Input: nums = [1,3,2] Output: false
# Constraints:
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
#
# 中文:
# 如果数组是单调递增或单调递减的，那么它是 单调 的。
# 如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> = nums[j]，那么数组 nums 是单调递减的。
# 当给定的数组 nums 是单调数组时返回 true，否则返回 false。
# 示例 1：
# 输入：nums = [1,2,2,3] 输出：true
# 示例 2：
# 输入：nums = [6,5,4,4] 输出：true
# 示例 3：
# 输入：nums = [1,3,2] 输出：false
# 提示：
# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105


#
# @lc app=leetcode.cn id=896 lang=python
#
# [896] 具有所有最深结点的最小子树
#
# https://leetcode-cn.com/problems/monotonic-array/description/
#
# algorithms
# Easy (46.61%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 13.2K
# Testcase Example:  '[1,2,2,3]'
#
# 如果数组是单调递增或单调递减的，那么它是单调的。
#
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A
# 是单调递减的。
#
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。
#
#
#
#
#
#
# 示例 1：
#
# 输入：[1,2,2,3]
# 输出：true
#
#
# 示例 2：
#
# 输入：[6,5,4,4]
# 输出：true
#
#
# 示例 3：
#
# 输入：[1,3,2]
# 输出：false
#
#
# 示例 4：
#
# 输入：[1,2,4,5]
# 输出：true
#
#
# 示例 5：
#
# 输入：[1,1,1]
# 输出：true
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
#
#
#
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 0:
            return
        if len(A) == 1:
            return True
        pre_flag = None
        for i in range(0, len(A)-1):
            flag = A[i] - A[i+1]
            if flag != 0:
                flag = flag / abs(flag)
            if flag == 0:
                continue
            if pre_flag is None:
                pre_flag = flag
            elif pre_flag != flag:
                return False
        return True

if __name__ == "__main__":
    s = Solution().isMonotonic([1,2,2,3])
    print(s)
    s = Solution().isMonotonic([1, 3,2])
    print(s)


