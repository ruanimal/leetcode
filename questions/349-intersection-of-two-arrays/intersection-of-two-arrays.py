# -*- coding:utf-8 -*-

# <SUBID:314439744,UPDATE:20230205>
# English:
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2] Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] Output: [9,4] Explanation: [4,9] is also accepted.
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
#
# 中文:
# 给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2] 输出：[2]
# 示例 2：
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4] 输出：[9,4] 解释：[4,9] 也是可通过的
# 提示：
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (59.39%)
# Total Accepted:    16.8K
# Total Submissions: 27.4K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
#
#
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
#
# 说明:
#
#
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
#
#
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        暴力法
        排序, 然后逐个比较大小, 用列表储存相同元素, 比较时记住上一轮结束比较的位置
        """
        if not nums1 or not nums2:
            return

        nums1.sort()
        nums2.sort()

        ret = []
        begin_j = 0
        for i in range(len(nums1)):
            j = begin_j
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    break
                elif nums1[i] == nums2[j]:
                    ret.append(nums1[i])
                    begin_j = j
                    break
                else:
                    j += 1
        return list(set(ret))

if __name__ == "__main__":
    t = Solution().intersection(nums1 = [4,9,5,8], nums2 = [9,4,9,8,4])
    print(t)

