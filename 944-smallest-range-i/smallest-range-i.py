# -*- coding:utf-8 -*-


# English:
# Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].
# After this process, we have some array B.
# Return the smallest possible difference between the maximum value of B and the minimum value of B.
# Example 1:
# Input: A = [1], K = 0 Output: 0 Explanation: B = [1]
# Example 2:
# Input: A = [0,10], K = 2 Output: 6 Explanation: B = [2,8]
# Example 3:
# Input: A = [1,3,6], K = 3 Output: 0 Explanation: B = [3,3,3] or B = [4,4,4]
# Note:
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000
#
# 中文:
# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。
# 在此过程之后，我们得到一些数组 B。
# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
# 示例 1：
# 输入：A = [1], K = 0 输出：0 解释：B = [1]
# 示例 2：
# 输入：A = [0,10], K = 2 输出：6 解释：B = [2,8]
# 示例 3：
# 输入：A = [1,3,6], K = 3 输出：0 解释：B = [3,3,3] 或 B = [4,4,4]
# 提示：
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000


#
# @lc app=leetcode.cn id=908 lang=python
#
# [908] 链表的中间结点
#
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # max_i = 0
        # min_i = 2 ** 31 - 1
        # for i in A:
        #     if i > max_i:
        #         max_i = i
        #     if i < min_i:
        #         min_i = i
        # if (max_i-min_i) <= 2*K:
        #     return 0
        # else:
        #     return max_i - min_i - 2*K
        max_i = max(A)
        min_i = min(A)
        if (max_i-min_i) <= 2*K:
            return 0
        else:
            return max_i - min_i - 2*K

if __name__ == "__main__":
    s = Solution().smallestRangeI(A = [1,3,6], K = 3)
    print(s)
    s = Solution().smallestRangeI(A = [0,10], K = 2)
    print(s)
    s = Solution().smallestRangeI(A = [1], K = 0)
    print(s)
    s = Solution().smallestRangeI(A = [3,1,10], K = 4)
    print(s)


