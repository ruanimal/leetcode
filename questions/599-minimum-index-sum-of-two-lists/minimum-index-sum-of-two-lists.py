# -*- coding:utf-8 -*-

# <SUBID:318569952,UPDATE:20230205>
# English:
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.
# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"] Output: ["Shogun"] Explanation: The only common string is "Shogun".
# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"] Output: ["Shogun"] Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.
# Example 3:
# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"] Output: ["sad","happy"] Explanation: There are three common strings: "happy" with index sum = (0 + 1) = 1. "sad" with index sum = (1 + 0) = 1. "good" with index sum = (2 + 2) = 4. The strings with the least index sum are "sad" and "happy".
# Constraints:
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] and list2[i] consist of spaces ' ' and English letters.
# All the strings of list1 are unique.
# All the strings of list2 are unique.
# There is at least a common string between list1 and list2.
#
# 中文:
# 假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。
# 示例 1:
# 输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"] 输出: ["Shogun"] 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
# 示例 2:
# 输入:list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["KFC", "Shogun", "Burger King"] 输出: ["Shogun"] 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
# 提示:
# 1 <= list1.length, list2.length <= 1000
# 1 <= list1[i].length, list2[i].length <= 30
# list1[i] 和 list2[i] 由空格
# ' ' 和英文字母组成。
# list1 的所有字符串都是 唯一 的。
# list2 中的所有字符串都是 唯一 的。



class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        """哈希记录index
        """
        if not list1 or not list2:
            return

        map_a = {}
        for idx, i in enumerate(list1):
            map_a.setdefault(i, []).append(idx)

        min_index = 2000
        tmp = []
        for idx, i in enumerate(list2):
            if i in map_a and (map_a[i][0] + idx) <= min_index:
                min_index = map_a[i][0] + idx
                tmp.append((min_index, i))
        return [i[1] for i in tmp if i[0]==min_index]

