# -*- coding:utf-8 -*-


# English:
# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4 Output: 12.75 Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
#
# 中文:
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
# 示例 1:
# 输入: [1,12,-5,-6,50,3], k = 4 输出: 12.75 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 注意:
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。


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


