# -*- coding:utf-8 -*-

# <SUBID:314595993,UPDATE:20230205>
# English:
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b" Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab" Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab" Output: true
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.
#
# 中文:
# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
# 如果可以，返回 true ；否则返回 false 。
# magazine 中的每个字符只能在 ransomNote 中使用一次。
# 示例 1：
# 输入：ransomNote = "a", magazine = "b" 输出：false
# 示例 2：
# 输入：ransomNote = "aa", magazine = "ab" 输出：false
# 示例 3：
# 输入：ransomNote = "aa", magazine = "aab" 输出：true
# 提示：
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote 和 magazine 由小写英文字母组成


#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (46.10%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 15.1K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom)
# 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true
# ；否则返回 false。
#
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
#
# 注意：
#
# 你可以假设两个字符串均只含有小写字母。
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#
#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """hash计数法
        """
        from collections import Counter
        count_a = Counter(ransomNote)
        count_b = Counter(magazine)
        for k, v in count_a.items():
            if count_b.get(k, 0) >= v:
                continue
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution().canConstruct('aa', 'aab')
    print(s)

