# -*- coding:utf-8 -*-


# English:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"] Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"] Output: "" Explanation: There is no common prefix among the input strings.
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.
#
# 中文:
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1：
# 输入：strs = ["flower","flow","flight"] 输出："fl"
# 示例 2：
# 输入：strs = ["dog","racecar","car"] 输出："" 解释：输入不存在公共前缀。
# 提示：
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成


#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.02%)
# Likes:    582
# Dislikes: 0
# Total Accepted:    87.6K
# Total Submissions: 260.1K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#

class Tried(dict):
    def __init__(self):
        self.count = 0


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        tried = Tried()
        for s in strs:
            tmp = tried
            for i in s:
                if i not in tmp:
                    tmp[i] = Tried()
                tmp.count += 1
                tmp = tmp[i]

        ans = ''
        tmp = tried
        # print(tried)
        while tried:
            if tried.count != len(strs) or len(tried) > 1:
                break
            k, tried = list(tried.items())[0]
            ans += k
        return ans

if __name__ == "__main__":
    s = Solution().longestCommonPrefix(["flower","flow","flight"])
    print(s)
    s = Solution().longestCommonPrefix(["a","b","c"])
    print(s)
    s = Solution().longestCommonPrefix(["baaa","b"])
    print(s)
    s = Solution().longestCommonPrefix(["b","b"])
    print(s)
    s = Solution().longestCommonPrefix(["b","bcb"])
    print(s)
    s = Solution().longestCommonPrefix(["b",""])
    print(s)



