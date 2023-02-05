# -*- coding:utf-8 -*-

# <SUBID:319664485,UPDATE:20230205>
# English:
# You are given an integer array deck where deck[i] represents the number written on the ith card.
# Partition the cards into one or more groups such that:
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.
# Example 1:
# Input: deck = [1,2,3,4,4,3,2,1] Output: true Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# Example 2:
# Input: deck = [1,1,1,2,2,2,3,3] Output: false Explanation: No possible partition.
# Constraints:
# 1 <= deck.length <= 104
# 0 <= deck[i] < 104
#
# 中文:
# 给定一副牌，每张牌上都写着一个整数。
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 仅当你可选的 X >= 2 时返回 true。
# 示例 1：
# 输入：deck = [1,2,3,4,4,3,2,1] 输出：true 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 示例 2：
# 输入：deck = [1,1,1,2,2,2,3,3] 输出：false 解释：没有满足要求的分组。
#
# 提示：
# 1 <= deck.length <= 104
# 0 <= deck[i] < 104


from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """暴力计数法
        """

        if not deck:
            return False
        counter = Counter(deck)
        min_count = min(counter.values())
        if min_count < 2:
            return False
        for i in range(2, min_count+1):
            if all(j % i == 0 for j in counter.values()):
                return True
        return False

