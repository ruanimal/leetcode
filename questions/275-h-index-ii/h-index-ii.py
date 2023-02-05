# -*- coding:utf-8 -*-

# <SUBID:308032927,UPDATE:20230205>
# English:
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in an ascending order, return compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.
# If there are several possible values for h, the maximum one is taken as the h-index.
# You must write an algorithm that runs in logarithmic time.
# Example 1:
# Input: citations = [0,1,3,5,6] Output: 3 Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:
# Input: citations = [1,2,100] Output: 2
# Constraints:
# n == citations.length
# 1 <= n <= 105
# 0 <= citations[i] <= 1000
# citations is sorted in ascending order.
#
# 中文:
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 升序排列 。计算并返回该研究者的 h 指数。
# h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的 n - h 篇论文每篇被引用次数 不超过 h 次。
# 提示：如果 h 有多种可能的值，h 指数 是其中最大的那个。
# 请你设计并实现对数时间复杂度的算法解决此问题。
# 示例 1：
# 输入：citations = [0,1,3,5,6] 输出：3 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。   由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。
# 示例 2：
# 输入：citations = [1,2,100] 输出：2
# 提示：
# n == citations.length
# 1 <= n <= 105
# 0 <= citations[i] <= 1000
# citations 按 升序排列


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations[-1] == 0:
            return 0
        length = len(citations)
        left = 0
        right = length - 1
        while left < right:
            #  and (length - start) > citations[start]
            mid = (left + right) >> 1
            if (length - mid) > citations[mid]:
                left = mid + 1
            else:
                right = mid
        return length - left

