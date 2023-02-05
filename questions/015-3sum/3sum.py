# -*- coding:utf-8 -*-

# <SUBID:21443275,UPDATE:20230205>
# English:
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4] Output: [[-1,-1,2],[-1,0,1]] Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0. nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0. nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0. The distinct triplets are [-1,0,1] and [-1,-1,2]. Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
# Input: nums = [0,1,1] Output: [] Explanation: The only possible triplet does not sum up to 0.
# Example 3:
# Input: nums = [0,0,0] Output: [[0,0,0]] Explanation: The only possible triplet sums up to 0.
# Constraints:
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
#
# 中文:
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
# 你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4] 输出：[[-1,-1,2],[-1,0,1]] 解释： nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。 nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。 nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：
# 输入：nums = [0,1,1] 输出：[] 解释：唯一可能的三元组和不为 0 。
# 示例 3：
# 输入：nums = [0,0,0] 输出：[[0,0,0]] 解释：唯一可能的三元组和为 0 。
# 提示：
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105


#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (22.02%)
# Likes:    1074
# Dislikes: 0
# Total Accepted:    63.6K
# Total Submissions: 278.1K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # # v1. 暴力
        # from itertools import combinations
        # ans_set = set()
        # for i in combinations(nums, 3):
        #     if sum(i) == 0:
        #         ans_set.add(tuple(sorted(i)))
        # return [list(i) for i in ans_set]


        # # v2. 暴力 + hash, n**2
        # from collections import Counter
        # if len(nums) < 3:
        #     return []

        # n = len(nums)
        # ans_set = set()
        # counter = Counter(nums)
        # for i in range(n-2):
        #     a = nums[i]
        #     counter[a] -= 1
        #     for j in range(i+1, n):
        #         b = nums[j]
        #         counter[b] -= 1
        #         target = 0-nums[i]-nums[j]
        #         if counter.get(target, 0) > 0:
        #             ans_set.add(tuple(sorted((nums[i], nums[j], target))))
        #         counter[b] += 1
        #     counter[a] += 1
        # return [list(i) for i in ans_set]

        # # v3 两边逼近 n ** 2
        # if len(nums) < 3:
        #     return []

        # ans = []
        # n = len(nums)
        # nums.sort()
        # if nums[0] > 0 or nums[-1] < 0:
        #     return []
        # if nums[0] == 0 or nums[-1] == 0:
        #     return [[0, 0, 0]] if sum(nums) == 0 else []
        # for i in range(n-2):
        #     if nums[i] > 0:
        #         break
        #     j = i + 1
        #     k = n - 1
        #     while j < k:
        #         s = sum([nums[i], nums[j], nums[k]])
        #         if s == 0:
        #             ans.append((nums[i], nums[j], nums[k]))
        #         if s >= 0:
        #             k -= 1
        #         elif s < 0:
        #             j += 1
        # return [list(i) for i in set(ans)]

        # # v4 分析法
        # if len(nums) < 3:
        #     return []

        # ans = []
        # pos = []
        # neg = []
        # counter = {0:0}
        # for i in nums:
        #     counter[i] = counter.get(i, 0) + 1
        #     if i > 0:
        #         pos.append(i)
        #     elif i < 0:
        #         neg.append(i)
        # zero_cnt = counter[0]
        # if zero_cnt >= 3:
        #     ans.append((0,0,0))
        # if not pos or not neg:
        #     return ans
        # pos.sort()
        # neg.sort()
        # if zero_cnt:
        #     for i in pos:
        #         if -i in counter:
        #             ans.append((-i, 0, i))

        # if len(pos) > 1:  # 取两个正数
        #     for a in neg:
        #         i = 0
        #         j = len(pos)-1
        #         target = -a
        #         while i < j:
        #             b, c = pos[i], pos[j]
        #             s = sum([a, b, c])
        #             if s == 0:
        #                 ans.append((a, b, c))
        #             if s >= 0:
        #                 j -= 1
        #             else:
        #                 i += 1
        # if len(neg) > 1:  # 取两个负数
        #     for a in pos:
        #         i = 0
        #         j = len(neg)-1
        #         target = -a
        #         while i < j:
        #             b, c = neg[i], neg[j]
        #             s = sum([a, b, c])
        #             if s == 0:
        #                 ans.append((a, b, c))
        #             if s >= 0:
        #                 j -= 1
        #             else:
        #                 i += 1
        # # return ans
        # return [list(i) for i in set(ans)]

        dic = {}
        res = []
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        pos =[i for i in dic if i > 0]
        neg =[i for i in dic if i < 0]
        neg.sort()
        if 0 in dic and dic[0] >= 3:
            res.append([0,0,0])
        for i in pos:
            for j in neg:
                k = -i-j
                if k in dic:
                    if (k==i or k==j) and dic[k] >= 2:
                        res.append([i,k,j])
                    elif i>k>j:
                        res.append([i,k,j])
                    if k < j:
                        break
        return res

if __name__ == "__main__":
    s = Solution().threeSum([-1,0,1,2,-1,-4])
    print(s)
    s = Solution().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
    print(s)

