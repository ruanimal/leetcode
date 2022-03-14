# -*- coding:utf-8 -*-


# English:
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4 Output: 12.75000 Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:
# Input: nums = [5], k = 1 Output: 5.00000
# Constraints:
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104
#
# 中文:
# 给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
# 请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。
# 任何误差小于 10-5 的答案都将被视为正确答案。
# 示例 1：
# 输入：nums = [1,12,-5,-6,50,3], k = 4 输出：12.75 解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 示例 2：
# 输入：nums = [5], k = 1 输出：5.00000
# 提示：
# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104


#
# @lc app=leetcode.cn id=643 lang=python
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (33.37%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 14.4K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1:
#
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
#
# 注意:
#
#
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
#
#
#

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # v1 用一个队列, 占用额外的空间, 速度比较慢, 1468 ms 17.31 %
        # from collections import deque
        # if len(nums) == 0:
        #     return

        # k = float(k)
        # que = deque()
        # total = 0
        # ans = None
        # for i in nums:
        #     if len(que) < k:
        #         que.append(i)
        #         total += i
        #         ans = total / k
        #         continue
        #     if ans is None:
        #         ans = total / k
        #     que.append(i)
        #     total += i
        #     total -= que[0]
        #     que.popleft()
        #     ans = max(ans, total / k)
        # return ans

        if len(nums) == 0:
            return
        tmp = 0
        k = float(k)
        ans = None
        total = 0
        for idx, i in enumerate(nums):
            # print(total)
            if tmp < k:
                tmp += 1
                total += i
                ans = total / k
                continue
            if ans is None:
                ans = total / k
            total += i
            total -= nums[idx-tmp]
            ans = max(ans, total / k)
        return ans

if __name__ == "__main__":
    s = Solution().findMaxAverage([1,12,-5,-6,50,3], k = 4)
    print(s)
    s = Solution().findMaxAverage([1,12,-5,-6,50,3], k = 1)
    print(s)
    s = Solution().findMaxAverage([5], k = 1)
    print(s)
    s = Solution().findMaxAverage([4,0,4,3,3], 5)
    print(s)


