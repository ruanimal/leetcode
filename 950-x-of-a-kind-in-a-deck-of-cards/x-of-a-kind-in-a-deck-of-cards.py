# -*- coding:utf-8 -*-


# English:
# In a deck of cards, each card has an integer written on it.
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
# Each group has exactly X cards.
# All the cards in each group have the same integer.
# Example 1:
# Input: deck = [1,2,3,4,4,3,2,1] Output: true Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
# Example 2:
# Input: deck = [1,1,1,2,2,2,3,3] Output: false´ Explanation: No possible partition.
# Example 3:
# Input: deck = [1] Output: false Explanation: No possible partition.
# Example 4:
# Input: deck = [1,1] Output: true Explanation: Possible partition [1,1].
# Example 5:
# Input: deck = [1,1,2,2,2,2] Output: true Explanation: Possible partition [1,1],[2,2],[2,2].
# Constraints:
# 1 <= deck.length <= 10^4
# 0 <= deck[i] < 10^4
#
# 中文:
# 给定一副牌，每张牌上都写着一个整数。
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 仅当你可选的 X >= 2 时返回 true。
# 示例 1：
# 输入：[1,2,3,4,4,3,2,1] 输出：true 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 示例 2：
# 输入：[1,1,1,2,2,2,3,3] 输出：false 解释：没有满足要求的分组。
# 示例 3：
# 输入：[1] 输出：false 解释：没有满足要求的分组。
# 示例 4：
# 输入：[1,1] 输出：true 解释：可行的分组是 [1,1]
# 示例 5：
# 输入：[1,1,2,2,2,2] 输出：true 解释：可行的分组是 [1,1]，[2,2]，[2,2]
#
# 提示：
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000


#
# @lc app=leetcode.cn id=914 lang=python
#
# [914] 卡牌分组
#
# https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (30.31%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 12.9K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# 给定一副牌，每张牌上都写着一个整数。
#
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
#
#
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
#
#
# 仅当你可选的 X >= 2 时返回 true。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
#
#
# 示例 2：
#
# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
#
#
# 示例 3：
#
# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
#
#
# 示例 4：
#
# 输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
#
#
# 示例 5：
#
# 输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]
#
#
#
# 提示：
#
#
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
#
#
#
#
#
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter

        def func(n):
            import math
            for i in range(1, int(math.sqrt(n))+1):
                a, b = divmod(n, i)
                if b == 0:
                    yield i
                    yield a

        if not deck:
            return False
        counter = Counter(deck)
        print(counter)
        tmp = list(set(counter.values()))
        if len(counter) == 1:
            return len([i for i in func(tmp[0]) if i != 1]) > 0
        tmp_set = set(i for i in func(tmp[0]) if i != 1)
        for i in tmp[1:]:
            for j in func(i):
                if j in tmp_set:
                    break
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution().hasGroupsSizeX([1,1,1,1])
    print(s)
    s = Solution().hasGroupsSizeX([1,1,1,1,2,2])
    print(s)
    s = Solution().hasGroupsSizeX([1])
    print(s)
    s = Solution().hasGroupsSizeX([])
    print(s)
    s = Solution().hasGroupsSizeX([1,2,3,4,4,3,2,1])
    print(s)

