# -*- coding:utf-8 -*-


# English:
# Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.
# Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.
# So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.
# Note:
# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.
# Example 1:
# Input: [1,2,3],[2] Output: 1 Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
# Example 2:
# Input: [1,2,3,4],[1,4] Output: 1 Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
#
# 中文:
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
# 说明:
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。
# 示例 1:
# 输入: [1,2,3],[2] 输出: 1 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
# 示例 2:
# 输入: [1,2,3,4],[1,4] 输出: 1 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。


#
# @lc app=leetcode.cn id=475 lang=python
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Easy (26.06%)
# Total Accepted:    2.1K
# Total Submissions: 8.1K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
#
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。
#
# 说明:
#
#
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
# 所有供暖器都遵循你的半径标准，加热的半径也一样。
#
#
# 示例 1:
#
#
# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
#
#
# 示例 2:
#
#
# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
#
#
#
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # 超时了
        # def all_can_cover(x):
        #     ret = set()
        #     need_houses = set(houses)
        #     for k, v in can_hourses_map.items():
        #         if k < x:
        #             need_houses -= v
        #     for house in need_houses:
        #         for heater in heaters:
        #             if heater - x <= house <= heater + x:
        #                 ret.add(house)
        #                 break
        #     can_hourses_map[x] = ret
        #     return len(ret) == len(need_houses)

        # def binary_search():
        #     left = 0
        #     right = 10**9
        #     while left <= right:
        #         mid = (left+right) // 2
        #         if all_can_cover(mid):
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     return left

        # if not houses or not heaters:
        #     return
        # heaters.sort()
        # houses.sort()
        # can_hourses_map = {}
        # return binary_search()

        houses.sort()
        heaters.sort()
        l1 = len(heaters)
        l2 = len(houses)
        if l1 == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))
        res = 0
        j = 0
        m = l2 - 1
        while m >= 0 and houses[m] >= heaters[-1]:
            m -= 1
        if m != l2 - 1:
            res = houses[-1] - heaters[-1]
        n = 0
        while n < l2 and houses[n] <= heaters[0]:
            n += 1
        if n != 0:
            res = max(res, heaters[0] - houses[0] )
        for i in range(n, m + 1):
            while houses[i] > heaters[j]:
                j += 1
            if houses[i] == heaters[j]:
                continue
            res = max(res, min(houses[i] - heaters[j - 1], heaters[j] - houses[i]))
        return res


if __name__ == "__main__":
    s = Solution().findRadius([1,2,3,4],[1,4])
    print(s)
    s = Solution().findRadius([1,2,3], [1])
    print(s)


