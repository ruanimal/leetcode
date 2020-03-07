# -*- coding:utf-8 -*-


# English:
# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
# Example 1:
#
# Input: nums = [1,2,2,4] Output: [2,3]
# Note:
#
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
#
# 中文:
# 集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
# 示例 1:
# 输入: nums = [1,2,2,4] 输出: [2,3]
# 注意:
# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。


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


