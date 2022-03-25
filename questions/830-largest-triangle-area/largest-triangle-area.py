# -*- coding:utf-8 -*-

# <SUBID:18365934,UPDATE:20220325>
# English:
# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
# Example 1:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]] Output: 2.00000 Explanation: The five points are shown in the above figure. The red triangle is the largest.
# Example 2:
# Input: points = [[1,0],[0,0],[0,1]] Output: 0.50000
# Constraints:
# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.
#
# 中文:
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
# 示例: 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]] 输出: 2 解释: 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
# 注意:
# 3 <= points.length <= 50.
# 不存在重复的点。
# -50 <= points[i][j] <= 50.
# 结果误差值在 10^-6 以内都认为是正确答案。


#
# @lc app=leetcode.cn id=812 lang=python
#
# [812] 旋转字符串
#
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        S=(x1y2 + x2y3 + x3y1- x1y3 - x2y1 - x3y2) /2;
        """
        # 求全组合
        import itertools

        ans = 0
        for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3):
            tmp = abs((x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2) / 2.0)
            ans = max(tmp, ans)
        return ans

if __name__ == "__main__":
    s = Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
    print(s)

