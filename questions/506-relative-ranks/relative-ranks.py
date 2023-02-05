# -*- coding:utf-8 -*-

# <SUBID:317680311,UPDATE:20230205>
# English:
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.
# Example 1:
# Input: score = [5,4,3,2,1] Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"] Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
# Example 2:
# Input: score = [10,3,8,9,4] Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"] Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
# Constraints:
# n == score.length
# 1 <= n <= 104
# 0 <= score[i] <= 106
# All the values in score are unique.
#
# 中文:
# 给你一个长度为 n 的整数数组 score ，其中 score[i] 是第 i 位运动员在比赛中的得分。所有得分都 互不相同 。
# 运动员将根据得分 决定名次 ，其中名次第 1 的运动员得分最高，名次第 2 的运动员得分第 2 高，依此类推。运动员的名次决定了他们的获奖情况：
# 名次第 1 的运动员获金牌 "Gold Medal" 。
# 名次第 2 的运动员获银牌 "Silver Medal" 。
# 名次第 3 的运动员获铜牌 "Bronze Medal" 。
# 从名次第 4 到第 n 的运动员，只能获得他们的名次编号（即，名次第 x 的运动员获得编号 "x"）。
# 使用长度为 n 的数组 answer 返回获奖，其中 answer[i] 是第 i 位运动员的获奖情况。
# 示例 1：
# 输入：score = [5,4,3,2,1] 输出：["Gold Medal","Silver Medal","Bronze Medal","4","5"] 解释：名次为 [1st, 2nd, 3rd, 4th, 5th] 。
# 示例 2：
# 输入：score = [10,3,8,9,4] 输出：["Gold Medal","5","Bronze Medal","Silver Medal","4"] 解释：名次为 [1st, 5th, 3rd, 2nd, 4th] 。
# 提示：
# n == score.length
# 1 <= n <= 104
# 0 <= score[i] <= 106
# score 中的所有值 互不相同


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """排序法"""

        ranks_map = {num: str(idx+1) for idx, num in enumerate(sorted(score, reverse=True))}
        medels = {
            "1": "Gold Medal",
            "2": "Silver Medal",
            "3": "Bronze Medal",
        }
        return [medels.get(ranks_map[i], ranks_map[i]) for i in score]
