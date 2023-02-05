# -*- coding:utf-8 -*-

# <SUBID:20060630,UPDATE:20230205>
# English:
# The array-form of an integer num is an array representing its digits in left to right order.
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
# Example 1:
# Input: num = [1,2,0,0], k = 34 Output: [1,2,3,4] Explanation: 1200 + 34 = 1234
# Example 2:
# Input: num = [2,7,4], k = 181 Output: [4,5,5] Explanation: 274 + 181 = 455
# Example 3:
# Input: num = [2,1,5], k = 806 Output: [1,0,2,1] Explanation: 215 + 806 = 1021
# Constraints:
# 1 <= num.length <= 104
# 0 <= num[i] <= 9
# num does not contain any leading zeros except for the zero itself.
# 1 <= k <= 104
#
# 中文:
# 整数的 数组形式  num 是按照从左到右的顺序表示其数字的数组。
# 例如，对于 num = 1321 ，数组形式是 [1,3,2,1] 。
# 给定 num ，整数的 数组形式 ，和整数 k ，返回 整数 num + k 的 数组形式 。
# 示例 1：
# 输入：num = [1,2,0,0], k = 34 输出：[1,2,3,4] 解释：1200 + 34 = 1234
# 示例 2：
# 输入：num = [2,7,4], k = 181 输出：[4,5,5] 解释：274 + 181 = 455
# 示例 3：
# 输入：num = [2,1,5], k = 806 输出：[1,0,2,1] 解释：215 + 806 = 1021
# 提示：
# 1 <= num.length <= 104
# 0 <= num[i] <= 9
# num 不包含任何前导零，除了零本身
# 1 <= k <= 104


#
# @lc app=leetcode.cn id=989 lang=python
#
# [989] 按公因数计算最大组件大小
#
# https://leetcode-cn.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (41.05%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 7.7K
# Testcase Example:  '[1,2,0,0]\n34'
#
# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
#
# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
#
#
#
#
#
#
# 示例 1：
#
# 输入：A = [1,2,0,0], K = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
#
#
# 解释 2：
#
# 输入：A = [2,7,4], K = 181
# 输出：[4,5,5]
# 解释：274 + 181 = 455
#
#
# 示例 3：
#
# 输入：A = [2,1,5], K = 806
# 输出：[1,0,2,1]
# 解释：215 + 806 = 1021
#
#
# 示例 4：
#
# 输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
# 输出：[1,0,0,0,0,0,0,0,0,0,0]
# 解释：9999999999 + 1 = 10000000000
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# 如果 A.length > 1，那么 A[0] != 0
#
#
#
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        B = [int(i) for i in str(K)]
        ans = []
        tmp = 0
        for i in range(-1, -max(len(A), len(B))-1, -1):
            if i >= -len(A):
                a = A[i]
            else:
                a = 0
            if i >= -len(B):
                b = B[i]
            else:
                b = 0
            tmp, a = divmod(a+b+tmp, 10)
            ans.append(a)
        if tmp:
            ans.append(tmp)
        return ans[::-1]

if __name__ == "__main__":
    s = Solution().addToArrayForm([1,2,0,0], 34)
    print(s)

