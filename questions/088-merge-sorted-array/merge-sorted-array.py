# -*- coding:utf-8 -*-

# <SUBID:308668721,UPDATE:20230205>
# English:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 Output: [1,2,2,3,5,6] Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [
# 1
# ,
# 2
# ,2,
# 3
# ,5,6] with the underlined elements coming from nums1.
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0 Output: [1] Explanation: The arrays we are merging are [1] and []. The result of the merge is [1].
# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1 Output: [1] Explanation: The arrays we are merging are [] and [1]. The result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?
#
# 中文:
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
# 示例 1：
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 输出：[1,2,2,3,5,6] 解释：需要合并 [1,2,3] 和 [2,5,6] 。 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
# 示例 2：
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0 输出：[1] 解释：需要合并 [1] 和 [] 。 合并结果是 [1] 。
# 示例 3：
# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1 输出：[1] 解释：需要合并的数组是 [] 和 [1] 。 合并结果是 [1] 。 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
# 提示：
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
# 进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？


#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (42.48%)
# Total Accepted:    36.2K
# Total Submissions: 83.3K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
#
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
#
#


class SolutionA(object):
    def merge(self, nums1: list, m: int, nums2: list, n: int):
        """
        暴力法
        思路： 将nums2中的逐个插入到nums1合适的位置，调整m的大小，如果某一个nums2中的值大于nums1最后一个值
              则将nums2剩下的值全部添加到nums1后边
        """

        for i in range(n):
            for j in range(m):
                if nums2[i] < nums1[j]:
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    m += 1
                    break
                if m == len(nums1):
                    return
            else:
                for k, num in enumerate(nums2[i:]):
                    nums1[m+k] = num
                return

class Solution(object):
    def merge(self, nums1: list, m: int, nums2: list, n: int):
        """
        反方向开始合并操作, 避免insert
        """

        i = m-1
        j = n-1
        while i+j+1 >= 0:
            # print(i, j, nums1)
            if i >= 0 and j >= 0:
                if nums1[i] >= nums2[j]:
                    nums1[i+j+1] = nums1[i]
                    i -= 1
                else:
                    nums1[i+j+1] = nums2[j]
                    j -= 1
            elif j < 0:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:  # i < 0
                nums1[i+j+1] = nums2[j]
                j -= 1
        return nums1

# @lc code=end

s = Solution().merge(
    nums1 = [1,2,3,0,0,0], m = 3,
    nums2 = [2,5,6],       n = 3,
)
print(s)


