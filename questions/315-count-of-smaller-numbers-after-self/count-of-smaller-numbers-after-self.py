# -*- coding:utf-8 -*-

# <SUBID:286608674,UPDATE:20230205>
# English:
# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
# Example 1:
# Input: nums = [5,2,6,1] Output: [2,1,1,0] Explanation: To the right of 5 there are 2 smaller elements (2 and 1). To the right of 2 there is only 1 smaller element (1). To the right of 6 there is 1 smaller element (1). To the right of 1 there is 0 smaller element.
# Example 2:
# Input: nums = [-1] Output: [0]
# Example 3:
# Input: nums = [-1,-1] Output: [0,0]
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
# 中文:
# 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。
# 示例 1：
# 输入：nums = [5,2,6,1] 输出：[2,1,1,0] 解释： 5 的右侧有 2 个更小的元素 (2 和 1) 2 的右侧仅有 1 个更小的元素 (1) 6 的右侧有 1 个更小的元素 (1) 1 的右侧有 0 个更小的元素
# 示例 2：
# 输入：nums = [-1] 输出：[0]
# 示例 3：
# 输入：nums = [-1,-1] 输出：[0,0]
# 提示：
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


class Solution_A:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """暴力法, 时间超时"""

        if len(nums) == 0:
            return []

        length = len(nums)
        res = [0 for _ in nums]
        for i in range(length):
            for j in range(i+1, length):
                if nums[j] < nums[i]:
                    res[i] += 1
        return res

from collections import namedtuple

Pair = namedtuple('Pair', ['val', 'idx'])

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        归并排序
        merge时, 右半边数组的数据如果要移动到前方, 则逆序+1
        """

        self.tmp = [0] * len(nums)
        self.count = [0] * len(nums)
        nums = [Pair(val, idx) for idx, val in enumerate(nums)]
        self.sort(nums, 0, len(nums)-1)
        # print(nums)
        return self.count

    def sort(self, nums: List[Pair], low, high) -> List:
        if low == high:
            return
        mid = (low + high) // 2
        self.sort(nums, low, mid)
        self.sort(nums, mid+1, high)
        return self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high) -> List[Pair]:
        # print(nums[low: mid+1], nums[mid+1: high+1])
        self.tmp[low:high+1] = nums[low:high+1]
        i, j = low, mid+1
        p = low
        while p < high+1:
            if i == mid+1:   # 左侧空了
                nums[p] = self.tmp[j]
                j += 1
            elif j == high+1:  # 右侧空了, 当前位置比右侧所有都大
                nums[p] = self.tmp[i]
                self.count[nums[p].idx] += j - mid - 1
                i += 1
                # 左侧前进一位, 当前位置比右侧已处理的都大
            elif self.tmp[i].val <= self.tmp[j].val:
                nums[p] = self.tmp[i]
                self.count[nums[p].idx] += j - mid - 1
                i += 1
            else:
                nums[p] = self.tmp[j]
                j += 1
            p += 1

