# -*- coding:utf-8 -*-

# <SUBID:319419123,UPDATE:20230205>
# English:
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb" Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ" Output: 0
# Constraints:
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
#
# 中文:
# 给你一个字符串 jewels 代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。 stones 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
# 字母区分大小写，因此 "a" 和 "A" 是不同类型的石头。
# 示例 1：
# 输入：jewels = "aA", stones = "aAAbbbb" 输出：3
# 示例 2：
# 输入：jewels = "z", stones = "ZZ" 输出：0
# 提示：
# 1 <= jewels.length, stones.length <= 50
# jewels 和 stones 仅由英文字母组成
# jewels 中的所有字符都是 唯一的


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_j = set(jewels)
        ret = 0
        for i in stones:
            if i in set_j:
                ret += 1
        return ret

