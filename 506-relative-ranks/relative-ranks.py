# -*- coding:utf-8 -*-


# English:
# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
# Example 1:
#
# Input: [5, 4, 3, 2, 1] Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"] Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.
# Note:
#
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
#
# 中文:
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
# (注：分数越高的选手，排名越靠前。)
# 示例 1:
# 输入: [5, 4, 3, 2, 1] 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"] 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal"). 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
# 提示:
# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。


#
# @lc app=leetcode.cn id=506 lang=python
#
# [506] 相对名次
#
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranks_map = {num: str(idx+1) for idx, num in enumerate(sorted(nums, reverse=True))}
        medels = {
            "1": "Gold Medal",
            "2": "Silver Medal",
            "3": "Bronze Medal",
        }
        return [medels.get(ranks_map[i], ranks_map[i]) for i in nums]

if __name__ == "__main__":
    s = Solution().findRelativeRanks([5, 4, 3, 2, 1])
    print(s)

