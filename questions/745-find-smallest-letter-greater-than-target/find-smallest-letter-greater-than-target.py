# -*- coding:utf-8 -*-

# <SUBID:319331003,UPDATE:20230205>
# English:
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
# Example 1:
# Input: letters = ["c","f","j"], target = "a" Output: "c" Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
# Example 2:
# Input: letters = ["c","f","j"], target = "c" Output: "f" Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
# Example 3:
# Input: letters = ["x","x","y","y"], target = "z" Output: "x" Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
# Constraints:
# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.
#
# 中文:
# 给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
# 返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。
# 示例 1：
# 输入: letters = ["c", "f", "j"]，target = "a" 输出: "c" 解释：letters 中字典上比 'a' 大的最小字符是 'c'。
# 示例 2:
# 输入: letters = ["c","f","j"], target = "c" 输出: "f" 解释：letters 中字典顺序上大于 'c' 的最小字符是 'f'。
# 示例 3:
# 输入: letters = ["x","x","y","y"], target = "z" 输出: "x" 解释：letters 中没有一个字符在字典上大于 'z'，所以我们返回 letters[0]。
# 提示：
# 2 <= letters.length <= 104
# letters[i] 是一个小写字母
# letters 按非递减顺序排序
# letters 最少包含两个不同的字母
# target 是一个小写字母



class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """简单二分查找
        """
        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return left

        next_letter = chr(ord(target)+1)  # 求下一个字母
        idx = binary_search(letters, next_letter)
        return letters[idx%len(letters)]

