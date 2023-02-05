# -*- coding:utf-8 -*-

# <SUBID:16920636,UPDATE:20230205>
# English:
# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.
# Example 1:
# Input: num = 16 Output: true Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:
# Input: num = 14 Output: false Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
# Constraints:
# 1 <= num <= 231 - 1
#
# 中文:
# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。
# 不能使用任何内置的库函数，如  sqrt 。
# 示例 1：
# 输入：num = 16 输出：true 解释：返回 true ，因为 4 * 4 = 16 且 4 是一个整数。
# 示例 2：
# 输入：num = 14 输出：false 解释：返回 false ，因为 3.742 * 3.742 = 14 但 3.742 不是一个整数。
# 提示：
# 1 <= num <= 231 - 1


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

