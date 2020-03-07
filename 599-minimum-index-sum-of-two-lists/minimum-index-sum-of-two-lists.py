# -*- coding:utf-8 -*-


# English:
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
# Example 1:
#
# Input: ["Shogun", "Tapioca Express", "Burger King", "KFC"] ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"] Output: ["Shogun"] Explanation: The only restaurant they both like is "Shogun".
# Example 2:
#
# Input: ["Shogun", "Tapioca Express", "Burger King", "KFC"] ["KFC", "Shogun", "Burger King"] Output: ["Shogun"] Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# Note:
#
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.
#
# 中文:
# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
# 示例 1:
# 输入: ["Shogun", "Tapioca Express", "Burger King", "KFC"] ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"] 输出: ["Shogun"] 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
# 示例 2:
# 输入: ["Shogun", "Tapioca Express", "Burger King", "KFC"] ["KFC", "Shogun", "Burger King"] 输出: ["Shogun"] 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
# 提示:
# 两个列表的长度范围都在 [1, 1000]内。
# 两个列表中的字符串的长度将在[1，30]的范围内。
# 下标从0开始，到列表的长度减1。
# 两个列表都没有重复的元素。


#
# @lc app=leetcode.cn id=599 lang=python
#
# [599] 两个列表的最小索引总和
#
# https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (44.63%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 9.5K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
#
# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
#
# 你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
#
# 示例 1:
#
# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
#
#
# 示例 2:
#
# 输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
#
#
# 提示:
#
#
# 两个列表的长度范围都在 [1, 1000]内。
# 两个列表中的字符串的长度将在[1，30]的范围内。
# 下标从0开始，到列表的长度减1。
# 两个列表都没有重复的元素。
#
#
#
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        f[i] 当前位置的最小索引和
        最后一步时：
        1. 前面已经找到最小索引和， 则结果为 f[i-1]
        2. 前面没有找到，则
            list1[i] 是否在 list2[:i] 中
            list2[i] 是否在 list1[:i] 中
            取两者的最小值
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

if __name__ == "__main__":
    s = Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"])
    print(s)

