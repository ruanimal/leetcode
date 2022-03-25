# -*- coding:utf-8 -*-

# <SUBID:21370603,UPDATE:20220325>
# English:
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7] Output: 49 Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1] Output: 1
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104
#
# 中文:
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。
# 示例 1：
# 输入：[1,8,6,2,5,4,8,3,7] 输出：49 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 示例 2：
# 输入：height = [1,1] 输出：1
# 提示：
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104


#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (55.28%)
# Likes:    606
# Dislikes: 0
# Total Accepted:    52.1K
# Total Submissions: 92.8K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
# 示例:
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
#
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # # v1.暴力法
        # if len(height) < 2:
        #     return

        # ans = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         ans = max(ans, min(height[i], height[j]) * (j - i))
        # return ans

        if len(height) < 2:
            return

        i = 0
        j = len(height)-1
        ans = 0
        while i < j:
            ans = max(ans, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans

if __name__ == "__main__":
    s = Solution().maxArea([1,8,6,2,5,4,8,3,7])
    print(s)

