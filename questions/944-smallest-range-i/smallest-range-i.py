# -*- coding:utf-8 -*-


# English:
# You are given an integer array nums and an integer k.
# In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.
# The score of nums is the difference between the maximum and minimum elements in nums.
# Return the minimum score of nums after applying the mentioned operation at most once for each index in it.
# Example 1:
# Input: nums = [1], k = 0 Output: 0 Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
# Example 2:
# Input: nums = [0,10], k = 2 Output: 6 Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
# Example 3:
# Input: nums = [1,3,6], k = 3 Output: 0 Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 104
# 0 <= k <= 104
#
# 中文:
# 给你一个整数数组 nums，和一个整数 k 。
# 在一个操作中，您可以选择 0 <= i < nums 的任何索引 i 。将 nums[i] 改为 nums[i] + x ，其中 x 是一个范围为 [-k, k] 的整数。对于每个索引 i ，最多 只能 应用 一次 此操作。
# nums 的 分数 是 nums 中最大和最小元素的差值。
# 在对nums中的每个索引最多应用一次上述操作后，返回 nums 的最低 分数 。
# 示例 1：
# 输入：nums = [1], k = 0 输出：0 解释：分数是 max(nums) - min(nums) = 1 - 1 = 0。
# 示例 2：
# 输入：nums = [0,10], k = 2 输出：6 解释：将 nums 改为 [2,8]。分数是 max(nums) - min(nums) = 8 - 2 = 6。
# 示例 3：
# 输入：nums = [1,3,6], k = 3 输出：0 解释：将 nums 改为 [4,4,4]。分数是 max(nums) - min(nums) = 4 - 4 = 0。
# 提示：
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 104
# 0 <= k <= 104


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


