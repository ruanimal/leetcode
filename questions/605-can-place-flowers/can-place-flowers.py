# -*- coding:utf-8 -*-

# <SUBID:318577941,UPDATE:20230205>
# English:
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1 Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2 Output: false
# Constraints:
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
#
# 中文:
# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
# 给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
# 示例 1：
# 输入：flowerbed = [1,0,0,0,1], n = 1 输出：true
# 示例 2：
# 输入：flowerbed = [1,0,0,0,1], n = 2 输出：false
# 提示：
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] 为 0 或 1
# flowerbed 中不存在相邻的两朵花
# 0 <= n <= flowerbed.length


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """程序模拟法
        每个空地分块处理
        """
        if not flowerbed:
            return
        space_len = 1 if (flowerbed[0] == 0) else 0   # 处理开头为空地的情况
        ans = 0
        for i in flowerbed:
            if i == 0:
                space_len += 1
            elif i == 1 and space_len > 0:
                ans += (space_len-1) // 2
                space_len = 0
        if space_len:  # 处理末尾为空地的情况
            ans += space_len // 2
        return ans >= n

