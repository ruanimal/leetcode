# -*- coding:utf-8 -*-

# <SUBID:20916974,UPDATE:20220325>
# English:
# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
# Return that maximum distance to the closest person.
# Example 1:
# Input: seats = [1,0,0,0,1,0,1] Output: 2 Explanation: If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2. If Alex sits in any other open seat, the closest person has distance 1. Thus, the maximum distance to the closest person is 2.
# Example 2:
# Input: seats = [1,0,0,0] Output: 3 Explanation: If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away. This is the maximum distance possible, so the answer is 3.
# Example 3:
# Input: seats = [0,1] Output: 1
# Constraints:
# 2 <= seats.length <= 2 * 104
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.
#
# 中文:
# 给你一个数组 seats 表示一排座位，其中 seats[i] = 1 代表有人坐在第 i 个座位上，seats[i] = 0 代表座位 i 上是空的（下标从 0 开始）。
# 至少有一个空座位，且至少有一人已经坐在座位上。
# 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
# 返回他到离他最近的人的最大距离。
# 示例 1：
# 输入：seats = [1,0,0,0,1,0,1] 输出：2 解释： 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。 因此，他到离他最近的人的最大距离是 2 。
# 示例 2：
# 输入：seats = [1,0,0,0] 输出：3 解释： 如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。 这是可能的最大距离，所以答案是 3 。
# 示例 3：
# 输入：seats = [0,1] 输出：1
# 提示：
# 2 <= seats.length <= 2 * 104
# seats[i] 为 0 或 1
# 至少有一个 空座位
# 至少有一个 座位上有人


#
# @lc app=leetcode.cn id=849 lang=python
#
# [849] 到最近的人的最大距离
#
# https://leetcode-cn.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Easy (34.85%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 10.7K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# 在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
#
# 至少有一个空座位，且至少有一人坐在座位上。
#
# 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
#
# 返回他到离他最近的人的最大距离。
#
# 示例 1：
#
# 输入：[1,0,0,0,1,0,1]
# 输出：2
# 解释：
# 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
# 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
# 因此，他到离他最近的人的最大距离是 2 。
#
#
# 示例 2：
#
# 输入：[1,0,0,0]
# 输出：3
# 解释：
# 如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
# 这是可能的最大距离，所以答案是 3 。
#
#
# 提示：
#
#
# 1 <= seats.length <= 20000
# seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。
#
#
#
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_val = 0
        cur = 0 if seats[0]  else 1
        in_zeros = not seats[0]
        s = seats
        for i in range(1, len(seats)):
            if s[i] == 0:
                cur += 1
            elif s[i-1] != s[i]:   # 当前是1, 且刚从0 -> 1
                if not max_val and seats[0]==0:
                    cur = 2 * cur
                max_val = max(cur, max_val)
                cur = 0
        max_val = max(cur*2, max_val)
        return (max_val + 1)//2

if __name__ == "__main__":
    s = Solution().maxDistToClosest([0,0,0,0,1,0,0,0,0,0,1,0,0,0])
    print(s)
    s = Solution().maxDistToClosest([0, 1])
    print(s)

