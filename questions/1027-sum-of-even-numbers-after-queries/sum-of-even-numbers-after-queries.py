# -*- coding:utf-8 -*-


# English:
# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].
# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.
# Return an integer array answer where answer[i] is the answer to the ith query.
# Example 1:
# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]] Output: [8,6,2,4] Explanation: At the beginning, the array is [1,2,3,4]. After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8. After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6. After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2. After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
# Example 2:
# Input: nums = [1], queries = [[4,0]] Output: [0]
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# 1 <= queries.length <= 104
# -104 <= vali <= 104
# 0 <= indexi < nums.length
#
# 中文:
# 给出一个整数数组 A 和一个查询数组 queries。
# 对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index] 上。然后，第 i 次查询的答案是 A 中偶数值的和。
# （此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）
# 返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。
# 示例：
# 输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]] 输出：[8,6,2,4] 解释： 开始时，数组为 [1,2,3,4]。 将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。 将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。 将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。 将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
# 提示：
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# 1 <= queries.length <= 10000
# -10000 <= queries[i][0] <= 10000
# 0 <= queries[i][1] < A.length


#
# @lc app=leetcode.cn id=985 lang=python
#
# [985] 查询后的偶数和
#
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        total_even = sum(x for x in A if x % 2 == 0)
        for i, (val, index) in zip(A, queries):
            if A[index] % 2 == 0:
                total_even -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                total_even += A[index]
            ret.append(total_even)
        return ret

if __name__ == "__main__":
    s = Solution().sumEvenAfterQueries(A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]])
    print(s)

