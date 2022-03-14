# -*- coding:utf-8 -*-


# English:
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1] Output: [5,6]
# Example 2:
# Input: nums = [1,1] Output: [2]
# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# 中文:
# 给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
# 示例 1：
# 输入：nums = [4,3,2,7,8,2,3,1] 输出：[5,6]
# 示例 2：
# 输入：nums = [1,1] 输出：[2]
# 提示：
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
# 进阶：你能在不使用额外空间且时间复杂度为 O(n) 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。


#
# @lc app=leetcode.cn id=448 lang=python
#
# [448] 找到所有数组中消失的数字
#
# https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (45.59%)
# Total Accepted:    6K
# Total Submissions: 12.8K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
#
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
#
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
#
# 示例:
#
#
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [5,6]
#
#
#
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # # v1 计数法
        # tmp = {i:0 for i in xrange(1, len(nums)+1)}
        # for num in nums:
        #     tmp[num] = 1
        # return [key for key,val in tmp.iteritems() if val == 0]

        # v2 bitmap
        import array
        bitmap = array.array('B', [0 for i in range(len(nums))])
        for i in nums:
            bitmap[i-1] = 1
        ans = [idx+1 for idx, i in enumerate(bitmap) if not i]
        return ans

if __name__ == "__main__":
    s = Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
    print(s)


