# -*- coding:utf-8 -*-

# <SUBID:18617592,UPDATE:20230205>
# English:
# You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
# Return the number of boomerangs.
# Example 1:
# Input: points = [[0,0],[1,0],[2,0]] Output: 2 Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
# Example 2:
# Input: points = [[1,1],[2,2],[3,3]] Output: 2
# Example 3:
# Input: points = [[1,1]] Output: 0
# Constraints:
# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.
#
# 中文:
# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组 ，其中 i 和 j 之间的距离和 i 和 k 之间的欧式距离相等（需要考虑元组的顺序）。
# 返回平面上所有回旋镖的数量。
# 示例 1：
# 输入：points = [[0,0],[1,0],[2,0]] 输出：2 解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
# 示例 2：
# 输入：points = [[1,1],[2,2],[3,3]] 输出：2
# 示例 3：
# 输入：points = [[1,1]] 输出：0
# 提示：
# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -104 <= xi, yi <= 104
# 所有点都 互不相同


#
# @lc app=leetcode.cn id=447 lang=python
#
# [447] 回旋镖的数量
#
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import itertools

        ans = 0
        counts_map = {}
        for i in points:
            for j in points:
                x1, y1 = i
                x2, y2 = j
                dis = (x1-x2)**2 + (y1-y2)**2
                counts_map[dis] = counts_map.get(dis, 0) + 1
            for dis, count in counts_map.items():
                ans += count*(count-1)
            counts_map = {}
        return ans
if __name__ == "__main__":
    s = Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])
    print(s)


