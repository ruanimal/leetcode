# -*- coding:utf-8 -*-


# English:
# Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
# Example 1:
#
# Input: [3, 1, 4, 1, 5], k = 2 Output: 2 Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
#
# Input:[1, 2, 3, 4, 5], k = 1 Output: 4 Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
#
# Input: [1, 3, 1, 5, 4], k = 0 Output: 1 Explanation: There is one 0-diff pair in the array, (1, 1).
# Note:
#
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].
#
# 中文:
# 给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.
# 示例 1:
# 输入: [3, 1, 4, 1, 5], k = 2 输出: 2 解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。 尽管数组中有两个1，但我们只应返回不同的数对的数量。
# 示例 2:
# 输入:[1, 2, 3, 4, 5], k = 1 输出: 4 解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
# 示例 3:
# 输入: [1, 3, 1, 5, 4], k = 0 输出: 1 解释: 数组中只有一个 0-diff 数对，(1, 1)。
# 注意:
# 数对 (i, j) 和数对 (j, i) 被算作同一数对。
# 数组的长度不超过10,000。
# 所有输入的整数的范围在 [-1e7, 1e7]。


#
# @lc app=leetcode.cn id=532 lang=python
#
# [532] 数组中的K-diff数对
#
# https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/description/
#
# algorithms
# Easy (31.42%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 14.9K
# Testcase Example:  '[3,1,4,1,5]\n2'
#
# 给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和
# j 都是数组中的数字，且两数之差的绝对值是 k.
#
# 示例 1:
#
#
# 输入: [3, 1, 4, 1, 5], k = 2
# 输出: 2
# 解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个1，但我们只应返回不同的数对的数量。
#
#
# 示例 2:
#
#
# 输入:[1, 2, 3, 4, 5], k = 1
# 输出: 4
# 解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
#
#
# 示例 3:
#
#
# 输入: [1, 3, 1, 5, 4], k = 0
# 输出: 1
# 解释: 数组中只有一个 0-diff 数对，(1, 1)。
#
#
# 注意:
#
#
# 数对 (i, j) 和数对 (j, i) 被算作同一数对。
# 数组的长度不超过10,000。
# 所有输入的整数的范围在 [-1e7, 1e7]。
#
#
#
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        from collections import Counter
        nums_set = Counter(nums)

        if k == 0:
            return sum(1 for _, v in nums_set.items() if v >= 2)

        ans = 0
        for i in nums_set:
            if (i - k) in nums_set:
                ans += 1
        return ans

if __name__ == "__main__":
    s = Solution().findPairs([1, 2, 3, 4, 5], k = 1)
    print(s)
    s = Solution().findPairs([1, 1,1,1], k = 0)
    print(s)
    s = Solution().findPairs([1,3,1,5,4], 0)
    print(s)


