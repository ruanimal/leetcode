# -*- coding:utf-8 -*-


# English:
# Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
# Note that the letters wrap around.
# For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
# Example 1:
# Input: letters = ["c","f","j"], target = "a" Output: "c"
# Example 2:
# Input: letters = ["c","f","j"], target = "c" Output: "f"
# Example 3:
# Input: letters = ["c","f","j"], target = "d" Output: "f"
# Constraints:
# 2 <= letters.length <= 104
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.
#
# 中文:
# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
# 在比较时，字母是依序循环出现的。举个例子：
# 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
# 示例 1：
# 输入: letters = ["c", "f", "j"]，target = "a" 输出: "c"
# 示例 2:
# 输入: letters = ["c","f","j"], target = "c" 输出: "f"
# 示例 3:
# 输入: letters = ["c","f","j"], target = "d" 输出: "f"
# 提示：
# 2 <= letters.length <= 104
# letters[i] 是一个小写字母
# letters 按非递减顺序排序
# letters 最少包含两个不同的字母
# target 是一个小写字母


#
# @lc app=leetcode.cn id=744 lang=python
#
# [744] 网络延迟时间
#
# https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/description/
#
# algorithms
# Easy (41.37%)
# Total Accepted:    3.9K
# Total Submissions: 9.2K
# Testcase Example:  '["c","f","j"]\n"a"'
#
# 给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。
#
# 数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
#
# 示例:
#
#
# 输入:
# letters = ["c", "f", "j"]
# target = "a"
# 输出: "c"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "c"
# 输出: "f"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "d"
# 输出: "f"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "g"
# 输出: "j"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "j"
# 输出: "c"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "k"
# 输出: "c"
#
#
# 注:
#
#
# letters长度范围在[2, 10000]区间内。
# letters 仅由小写字母组成，最少包含两个不同的字母。
# 目标字母target 是一个小写字母。
#
#
#
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
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
                    return mid   # 查找到的位置加一
            return left

        next_letter = chr(ord(target)+1)
        idx = binary_search(letters, next_letter)
        return letters[idx%len(letters)]

if __name__ == "__main__":
    s = Solution().nextGreatestLetter(["e","e","e","e","e","e","n","n","n","s"], 'e')
    print(s)

