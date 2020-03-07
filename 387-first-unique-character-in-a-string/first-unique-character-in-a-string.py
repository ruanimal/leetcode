# -*- coding:utf-8 -*-


# English:
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Examples:
# s = "leetcode" return 0. s = "loveleetcode", return 2.
# Note: You may assume the string contain only lowercase letters.
#
# 中文:
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 案例:
# s = "leetcode" 返回 0. s = "loveleetcode", 返回 2.
# 注意事项：您可以假定该字符串只包含小写字母。


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



