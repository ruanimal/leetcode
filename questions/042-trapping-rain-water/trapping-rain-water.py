# -*- coding:utf-8 -*-

# <SUBID:22443510,UPDATE:20230205>
# English:
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6 Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
# Input: height = [4,2,0,3,2,5] Output: 9
# Constraints:
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105
#
# 中文:
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1] 输出：6 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
# 输入：height = [4,2,0,3,2,5] 输出：9
# 提示：
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (43.59%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 39.8K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        right_maxs = [0 for _ in range(len(height))]
        right_maxs[-1] = height[-1]

        for i in range(len(height)-2, -1, -1):
            right_maxs[i] = max(height[i], right_maxs[i+1])

        ans = 0
        left_max = height[0]
        for i in range(1, len(height)):
            # print(left_max, right_maxs[i])
            limit = min(left_max, right_maxs[i])
            space = limit - height[i]
            if space > 0:
                ans += space
            left_max = max(left_max, height[i])
        return ans

if __name__ == "__main__":
    s = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(s)



