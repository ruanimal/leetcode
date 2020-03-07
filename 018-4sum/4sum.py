# -*- coding:utf-8 -*-


# English:
# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note:
# The solution set must not contain duplicate quadruplets.
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0. A solution set is: [ [-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2] ]
#
# 中文:
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：
# 答案中不可以包含重复的四元组。
# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。 满足要求的四元组集合为： [ [-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2] ]


#
# @lc app=leetcode.cn id=18 lang=python
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (35.95%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    30K
# Total Submissions: 83.5K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum_v1(self, nums, target):
        """暴力法，复杂度较高
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(index, nums, target, ans, route):
            if index >= len(nums):
                if target == 0 and len(route) == 4:
                    ans.add(tuple(route))
                return 
            # print(index, nums, target, ans, route)
            route.append(nums[index])
            helper(index+1, nums, target-nums[index], ans, route)
            route.pop()
            helper(index+1, nums, target, ans, route)

        if len(nums) < 4:
            return []
            
        nums.sort()
        ans = set()
        route = []
        helper(0, nums, target, ans, route)
        return list(list(i) for i in ans) 

    def fourSum_v2(self, nums, target):
        """双指针， 复杂度小于n^3"""
        
        if len(nums) < 4:
            return []

        nums.sort()
        ans = set()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j + 1
                right = len(nums) - 1
                while (left < right):
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif tmp < target:
                        left += 1
                    else:
                        right -= 1
        return list(list(i) for i in ans) 

    def fourSum(self, nums, target):
        """双指针叠加剪枝"""
        
        if len(nums) < 4:
            return []

        nums.sort()
        ans = set()

        for i in range(len(nums)-3):
            # 当数组最小值和都大于target 跳出
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            for j in range(i+1, len(nums)-2):
                left = j + 1
                right = len(nums) - 1
                while (left < right):
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif tmp < target:
                        left += 1
                    else:
                        right -= 1
        return list(list(i) for i in ans) 


        
if __name__ == "__main__":
    s = Solution().fourSum(nums = [1, 0, -1, 0, -2, 2], target = 0)
    print(s)


