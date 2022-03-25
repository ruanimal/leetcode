# -*- coding:utf-8 -*-

# <SUBID:20762604,UPDATE:20220325>
# English:
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode" Output: 0
# Example 2:
# Input: s = "loveleetcode" Output: 2
# Example 3:
# Input: s = "aabb" Output: -1
# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.
#
# 中文:
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
# 示例 1：
# 输入: s = "leetcode" 输出: 0
# 示例 2:
# 输入: s = "loveleetcode" 输出: 2
# 示例 3:
# 输入: s = "aabb" 输出: -1
# 提示:
# 1 <= s.length <= 105
# s 只包含小写字母


#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (37.70%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    31.9K
# Total Submissions: 82.4K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.
#
#
#
#
# 注意事项：您可以假定该字符串只包含小写字母。
#
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        counter = {}
        for idx, i in enumerate(s):
            counter.setdefault(i, []).append(idx)

        tmp = sum((i[1] for i in counter.items() if len(i[1])==1), [])
        tmp.sort()
        return tmp[0] if tmp else -1

if __name__ == "__main__":
    s = Solution().firstUniqChar('leetcode')
    print(s)



