# -*- coding:utf-8 -*-


# English:
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
# Example 1:
# Input: nums = [1,2,2,4] Output: [2,3]
# Example 2:
# Input: nums = [1,1] Output: [1,2]
# Constraints:
# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104
#
# 中文:
# 集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
# 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
# 示例 1：
# 输入：nums = [1,2,2,4] 输出：[2,3]
# 示例 2：
# 输入：nums = [1,1] 输出：[1,2]
# 提示：
# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104


#
# @lc app=leetcode.cn id=645 lang=python
#
# [645] 错误的集合
#
# https://leetcode-cn.com/problems/set-mismatch/description/
#
# algorithms
# Easy (35.54%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 11.4K
# Testcase Example:  '[1,2,2,4]'
#
# 集合 S 包含从1到 n
# 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
#
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
#
# 示例 1:
#
#
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
#
#
# 注意:
#
#
# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。
#
#
#
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # v1  396 ms, beats 8.06 % of python submissions
        # tmp = set(range(1, len(nums)+1))
        # for i in nums:
        #     if i in tmp:
        #         tmp.remove(i)
        #     else:
        #         tmp.add(-i)
        # return [abs(i) for i in sorted(tmp)]

        n = len(nums)

        dup = lose = None
        tmp = {}
        for i in nums:
            tmp[i] = tmp.get(i, 0) + 1
            if tmp[i] > 1:
                dup = i
                break
        lose = n*(n+1)//2 + dup - sum(nums)
        return [dup, lose]


if __name__ == "__main__":
    s = Solution().findErrorNums(nums = [1,3,3,4])
    print(s)
    s = Solution().findErrorNums(nums = [1,2,2,4])
    print(s)
    s = Solution().findErrorNums(nums = [3,2,3,4,6,5])
    print(s)
    s = Solution().findErrorNums(nums = [1,5,3,2,2,7,6,4,8,9])
    print(s)


