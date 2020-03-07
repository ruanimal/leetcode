# -*- coding:utf-8 -*-


# English:
# Given an array A of integers, we must modify the array in the following way: we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  (We may choose the same index i multiple times.)
# Return the largest possible sum of the array after modifying it in this way.
# Example 1:
# Input: A = [4,2,3], K = 1 Output: 5 Explanation: Choose indices (1,) and A becomes [4,-2,3].
# Example 2:
# Input: A = [3,-1,0,2], K = 3 Output: 6 Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
# Example 3:
# Input: A = [2,-3,-1,5,-4], K = 2 Output: 13 Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
# Note:
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100
#
# 中文:
# 给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）
# 以这种方式修改数组后，返回数组可能的最大和。
# 示例 1：
# 输入：A = [4,2,3], K = 1 输出：5 解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
# 示例 2：
# 输入：A = [3,-1,0,2], K = 3 输出：6 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
# 示例 3：
# 输入：A = [2,-3,-1,5,-4], K = 2 输出：13 解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
# 提示：
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100


#
# @lc app=leetcode.cn id=1005 lang=python
#
# [1005] K 次取反后最大化的数组和
#
# https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (43.81%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 4.6K
# Testcase Example:  '[4,2,3]\n1'
#
# 给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K
# 次。（我们可以多次选择同一个索引 i。）
#
# 以这种方式修改数组后，返回数组可能的最大和。
#
#
#
# 示例 1：
#
# 输入：A = [4,2,3], K = 1
# 输出：5
# 解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
#
#
# 示例 2：
#
# 输入：A = [3,-1,0,2], K = 3
# 输出：6
# 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
#
#
# 示例 3：
#
# 输入：A = [2,-3,-1,5,-4], K = 2
# 输出：13
# 解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100
#
#
#
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A or not K:
            return 0

        A.sort()
        tmp = 0
        i = -1
        ans = 0
        while i < K-1:
            if A[i+1] >= 0:
                break
            else:
                tmp += A[i+1]
                A[i+1] = -A[i+1]
            i += 1
        ans += sum(A)
        print(i, K, ans)
        if K-1-i>0 and (K-1-i) % 2 == 1:
            if i < len(A)-1:
                ans -= 2 * min(A[i], A[i+1])
            else:
                ans -= 2 * A[i]
        return ans

if __name__ == "__main__":
    s = Solution().largestSumAfterKNegations([4,2,3], 1)
    print(s)
    s = Solution().largestSumAfterKNegations([2,-3,-1,5,-4], 2)
    print(s)
    s = Solution().largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6)
    print(s)

