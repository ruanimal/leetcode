# -*- coding:utf-8 -*-

# <SUBID:16920636,UPDATE:20220325>
# English:
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.
# Example 1:
# Input: num = 16 Output: true
# Example 2:
# Input: num = 14 Output: false
# Constraints:
# 1 <= num <= 2^31 - 1
#
# 中文:
# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 进阶：不要 使用任何内置的库函数，如  sqrt 。
# 示例 1：
# 输入：num = 16 输出：true
# 示例 2：
# 输入：num = 14 输出：false
# 提示：
# 1 <= num <= 2^31 - 1


#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.64%)
# Total Accepted:    8K
# Total Submissions: 20K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 示例 1：
#
# 输入：16
# 输出：True
#
# 示例 2：
#
# 输入：14
# 输出：False
#
#
#
class Solution(object):
    all_nums = {i**2: i for i in range(65536)}

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 二分查找比较慢
        # all_nums = [i for i in range(65536)]

        # def binary_search(target):
        #     left = 0
        #     right = len(all_nums) - 1
        #     while left <= right:
        #         mid = (left+right) // 2
        #         if all_nums[mid] ** 2 < target:
        #             left = mid + 1
        #         elif target < all_nums[mid] ** 2:
        #             right = mid - 1
        #         else:
        #             return mid
        #     return -1
        # ret = binary_search(num)
        return num in Solution.all_nums

if __name__ == "__main__":
    s = Solution().isPerfectSquare(9)
    print(s)

