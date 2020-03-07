# -*- coding:utf-8 -*-


# English:
# We are given an array A of N lowercase letter strings, all of the same length.
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)
# Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.
# Return the minimum possible value of D.length.
# Example 1:
# Input: ["cba","daf","ghi"] Output: 1 Explanation: After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order. If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
# Example 2:
# Input: ["a","b"] Output: 0 Explanation: D = {}
# Example 3:
# Input: ["zyx","wvu","tsr"] Output: 3 Explanation: D = {0, 1, 2}
# Note:
# 1 <= A.length <= 100
# 1 <= A[i].length <= 1000
#
# 中文:
# 给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。
# 删除 操作的定义是：选出一组要删掉的列，删去 A 中对应列中的所有字符，形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。
# 比如，有 A = ["abcdef", "uvwxyz"]，
# 要删掉的列为 {0, 2, 3}，删除后 A 为["bef", "vyz"]， A 的列分别为["b","v"], ["e","y"], ["f","z"]。
# 你需要选出一组要删掉的列 D，对 A 执行删除操作，使 A 中剩余的每一列都是 非降序 排列的，然后请你返回 D.length 的最小可能值。
# 示例 1：
# 输入：["cba", "daf", "ghi"] 输出：1 解释： 当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。 若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。
# 示例 2：
# 输入：["a", "b"] 输出：0 解释：D = {}
# 示例 3：
# 输入：["zyx", "wvu", "tsr"] 输出：3 解释：D = {0, 1, 2}
# 提示：
# 1 <= A.length <= 100
# 1 <= A[i].length <= 1000


#
# @lc app=leetcode.cn id=944 lang=python
#
# [944] 最小差值 I
#
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        D = []
        for y in range(len(A[0])):
            pre = A[0][y]
            for x in range(1, len(A)):
                if A[x][y] < pre:
                    D.append(y)
                    break
                pre = A[x][y]
        # print(D)
        return len(D)

if __name__ == "__main__":
    s = Solution().minDeletionSize(["cba", "daf", "ghi"])
    print(s)
    s = Solution().minDeletionSize(["abcdef", "uvwxyz"])
    print(s)
    s = Solution().minDeletionSize(["rrjk",
                                    "furt",
                                    "guzm"])
    print(s)


