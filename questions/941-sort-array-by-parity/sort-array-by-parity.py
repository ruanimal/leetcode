# -*- coding:utf-8 -*-


# English:
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
# Example 1:
# Input: nums = [3,1,2,4] Output: [2,4,3,1] Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:
# Input: nums = [0] Output: [0]
# Constraints:
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
#
# 中文:
# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
# 你可以返回满足此条件的任何数组作为答案。
# 示例：
# 输入：[3,1,2,4] 输出：[2,4,3,1] 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
# 提示：
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000


#
# @lc app=leetcode.cn id=905 lang=python
#
# [905] 最长的斐波那契子序列的长度
#
# https://leetcode-cn.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (69.51%)
# Total Accepted:    14.4K
# Total Submissions: 21K
# Testcase Example:  '[3,1,2,4]'
#
# 给定一个非负整数数组 A，返回一个由 A 的所有偶数元素组成的数组，后面跟 A 的所有奇数元素。
#
# 你可以返回满足此条件的任何数组作为答案。
#
#
#
# 示例：
#
# 输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
#
#
#
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(A) - 1
        is_even = lambda i: (i & 1) == 0
        while i < j:
            if is_even(A[i]):
                i += 1
                continue
            if not is_even(A[j]):
                j -= 1
                continue
            A[i], A[j] = A[j], A[i]
        return A

if __name__ == "__main__":
    d = [3,1,2,4,7,9]
    s = Solution().sortArrayByParity(d)
    print(s)


