# -*- coding:utf-8 -*-


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


#
# @lc app=leetcode.cn id=922 lang=python
#
# [922] 可能的二分法
#
# https://leetcode-cn.com/problems/sort-array-by-parity-ii/description/
#
# algorithms
# Easy (66.96%)
# Total Accepted:    8.6K
# Total Submissions: 13K
# Testcase Example:  '[4,2,5,7]'
#
# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
#
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
#
# 你可以返回任何满足上述条件的数组作为答案。
#
#
#
# 示例：
#
# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#
#
#
#
# 提示：
#
#
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
#
#
#
#
#
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return
        i, j = 0, 1
        while i < len(A) and j < len(A):
            while (A[i] % 2) == 0:
                i += 2
                if i >= len(A):
                    return A
            while (A[j] % 2) == 1:
                j += 2
                if j >= len(A):
                    return A
            # print(i, j)
            A[i], A[j] = A[j], A[i]
        return A

if __name__ == "__main__":
    x = Solution().sortArrayByParityII([4,2,5,7])
    print(x)

