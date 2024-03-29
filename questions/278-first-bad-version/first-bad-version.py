# -*- coding:utf-8 -*-

# <SUBID:16923995,UPDATE:20230205>
# English:
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
# Example 1:
# Input: n = 5, bad = 4 Output: 4 Explanation: call isBadVersion(3) -> false call isBadVersion(5) -> true call isBadVersion(4) -> true Then 4 is the first bad version.
# Example 2:
# Input: n = 1, bad = 1 Output: 1
# Constraints:
# 1 <= bad <= n <= 231 - 1
#
# 中文:
# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
# 示例 1：
# 输入：n = 5, bad = 4 输出：4 解释： 调用 isBadVersion(3) -> false 调用 isBadVersion(5) -> true 调用 isBadVersion(4) -> true 所以，4 是第一个错误的版本。
# 示例 2：
# 输入：n = 1, bad = 1 输出：1
# 提示：
# 1 <= bad <= n <= 231 - 1


#
# @lc app=leetcode.cn id=278 lang=python
#
# [278] 第一个错误的版本
#
# https://leetcode-cn.com/problems/first-bad-version/description/
#
# algorithms
# Easy (28.29%)
# Total Accepted:    15K
# Total Submissions: 49.8K
# Testcase Example:  '5\n4'
#
#
# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
#
# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
#
# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version
# 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
#
# 示例:
#
# 给定 n = 5，并且 version = 4 是第一个错误的版本。
#
# 调用 isBadVersion(3) -> false
# 调用 isBadVersion(5) -> true
# 调用 isBadVersion(4) -> true
#
# 所以，4 是第一个错误的版本。 
#
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left+right) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        if isBadVersion(0):
            return 0
        if not isBadVersion(n):
            return
        return left


