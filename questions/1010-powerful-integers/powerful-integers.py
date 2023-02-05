# -*- coding:utf-8 -*-

# <SUBID:20890010,UPDATE:20230205>
# English:
# Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.
# An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.
# You may return the answer in any order. In your answer, each value should occur at most once.
# Example 1:
# Input: x = 2, y = 3, bound = 10 Output: [2,3,4,5,7,9,10] Explanation: 2 = 20 + 30 3 = 21 + 30 4 = 20 + 31 5 = 21 + 31 7 = 22 + 31 9 = 23 + 30 10 = 20 + 32
# Example 2:
# Input: x = 3, y = 5, bound = 15 Output: [2,4,6,8,10,14]
# Constraints:
# 1 <= x, y <= 100
# 0 <= bound <= 106
#
# 中文:
# 给定三个整数 x 、 y 和 bound ，返回 值小于或等于 bound 的所有 强整数 组成的列表 。
# 如果某一整数可以表示为 xi + yj ，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个 强整数 。
# 你可以按 任何顺序 返回答案。在你的回答中，每个值 最多 出现一次。
# 示例 1：
# 输入：x = 2, y = 3, bound = 10 输出：[2,3,4,5,7,9,10] 解释： 2 = 20 + 30 3 = 21 + 30 4 = 20 + 31 5 = 21 + 31 7 = 22 + 31 9 = 23 + 30 10 = 20 + 32
# 示例 2：
# 输入：x = 3, y = 5, bound = 15 输出：[2,4,6,8,10,14]
# 提示：
# 1 <= x, y <= 100
# 0 <= bound <= 106


#
# @lc app=leetcode.cn id=970 lang=python
#
# [970] 强整数
#
# https://leetcode-cn.com/problems/powerful-integers/description/
#
# algorithms
# Easy (36.86%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 6K
# Testcase Example:  '2\n3\n10'
#
# 给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
#
# 返回值小于或等于 bound 的所有强整数组成的列表。
#
# 你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。
#
#
#
# 示例 1：
#
# 输入：x = 2, y = 3, bound = 10
# 输出：[2,3,4,5,7,9,10]
# 解释：
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
#
#
# 示例 2：
#
# 输入：x = 3, y = 5, bound = 15
# 输出：[2,4,6,8,10,14]
#
#
#
#
# 提示：
#
#
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6
#
#
#
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        import math

        if x==1 and y==1:
            return [x+y] if x+y <= bound else []
        elif x==1 or y==1:
            x, y = sorted([x, y])
            b = math.log(bound-x, y)
            return [y**i+x for i in range(int(b)+1)]

        a = 0
        tmp = 1
        ans = []
        while tmp < bound:
            b = math.log(bound-tmp, y)
            for i in range(int(b)+1):
                ans.append(x**a+y**i)
            a += 1
            tmp *= x
        return list(set(ans))

if __name__ == "__main__":
    s = Solution().powerfulIntegers(x = 3, y = 5, bound = 15)
    print(s)
    s = Solution().powerfulIntegers(x = 2, y = 1, bound = 10)
    print(s)

