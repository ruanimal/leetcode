# -*- coding:utf-8 -*-


# English:
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Example:
# Input: [1,2,3,4] Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
# Note: Please solve it without division and in O(n).
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
#
# 中文:
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
# 示例:
# 输入: [1,2,3,4] 输出: [24,12,8,6]
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）


#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除自身以外数组的乘积
#
# https://leetcode-cn.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (60.29%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 18.5K
# Testcase Example:  '[1,2,3,4]'
#
# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
# 之外其余各元素的乘积。
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
#
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                total *= i
            elif zero_count > 1:
                total = 0
                break
            else:
                zero_count += 1
        if zero_count > 1:
            return [0 for _ in nums]
        elif zero_count == 1:
            return [total if i == 0 else 0 for i in nums]
        return [int(total * i ** -1) for i in nums]

if __name__ == "__main__":
    s = Solution().productExceptSelf([1,2,3,4])
    print(s)
    s = Solution().productExceptSelf([1,0,3,0])
    print(s)
    s = Solution().productExceptSelf([1, 0])
    print(s)
    s = Solution().productExceptSelf([1, -1])
    print(s)

