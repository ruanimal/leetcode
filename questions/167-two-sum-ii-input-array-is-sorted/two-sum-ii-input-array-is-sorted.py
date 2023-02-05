# -*- coding:utf-8 -*-

# <SUBID:311888172,UPDATE:20230205>
# English:
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.
# Example 1:
# Input: numbers = [
# 2
# ,
# 7
# ,11,15], target = 9 Output: [1,2] Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:
# Input: numbers = [
# 2
# ,3,
# 4
# ], target = 6 Output: [1,3] Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:
# Input: numbers = [
# -1
# ,
# 0
# ], target = -1 Output: [1,2] Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
#
# 中文:
# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
# 你所设计的解决方案必须只使用常量级的额外空间。
# 示例 1：
# 输入：numbers = [2,7,11,15], target = 9 输出：[1,2] 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
# 示例 2：
# 输入：numbers = [2,3,4], target = 6 输出：[1,3] 解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
# 示例 3：
# 输入：numbers = [-1,0], target = -1 输出：[1,2] 解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
# 提示：
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers 按 非递减顺序 排列
# -1000 <= target <= 1000
# 仅存在一个有效答案



class SolutionA(object):
    def twoSum(self, numbers: List[int], target: int) -> int:
        """
        hash法, 将number:index存到dict中, 判断 target - number 是否在dict中
        """
        index_map = {}
        for idx, elem in enumerate(numbers):
            index_map.setdefault(elem, []).append(idx)

        for idx, i in enumerate(numbers):
            extra = (target - i)
            extra_idx = index_map.get(extra, [])
            for idx2 in extra_idx:
                if idx == idx2:
                    continue
                return [idx+1, idx2+1]
        return []

class Solution(object):
    def twoSum(self, numbers: List[int], target: int) -> int:
        """
        双指针法
        """
        if len(numbers) <= 1:
            return []
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]   # 下标从1开始
        return []
