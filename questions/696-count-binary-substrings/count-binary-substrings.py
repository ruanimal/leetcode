# -*- coding:utf-8 -*-

# <SUBID:19823207,UPDATE:20230205>
# English:
# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.
# Example 1:
# Input: s = "00110011" Output: 6 Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01". Notice that some of these substrings repeat and are counted the number of times they occur. Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
# Input: s = "10101" Output: 4 Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
# Constraints:
# 1 <= s.length <= 105
# s[i] is either '0' or '1'.
#
# 中文:
# 给定一个字符串 s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是成组连续的。
# 重复出现（不同位置）的子串也要统计它们出现的次数。
# 示例 1：
# 输入：s = "00110011" 输出：6 解释：6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。 注意，一些重复出现的子串（不同位置）要统计它们出现的次数。 另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。
# 示例 2：
# 输入：s = "10101" 输出：4 解释：有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。
# 提示：
# 1 <= s.length <= 105
# s[i] 为 '0' 或 '1'


#
# @lc app=leetcode.cn id=696 lang=python
#
# [696] 计数二进制子串
#
# https://leetcode-cn.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (45.98%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 6.6K
# Testcase Example:  '"00110"'
#
# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
#
# 重复出现的子串要计算它们出现的次数。
#
# 示例 1 :
#
#
# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
#
# 请注意，一些重复出现的子串要计算它们出现的次数。
#
# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
#
#
# 示例 2 :
#
#
# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
#
#
# 注意：
#
#
# s.length 在1到50,000之间。
# s 只包含“0”或“1”字符。
#
#
#
# # 解法1： 暴力求解， 复杂度大于 N**2
# class Solution(object):
#     cache = {}
#     def countBinarySubstrings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         ret = []
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 if (j - i) % 2 != 0:
#                     continue
#                 sub_s = s[i:j]
#                 if self.is_vaild(sub_s):
#                     ret.append(sub_s)
#         return len(ret)

#     @staticmethod
#     def is_vaild(s):
#         if s in Solution.cache:
#             return Solution.cache[s]

#         pre = None
#         change_count = 0
#         zero_count = 0
#         one_count = 0
#         for i in s:
#             if i == '0':
#                 zero_count += 1
#             else:
#                 one_count += 1
#             if pre is not None and i != pre:
#                 change_count += 1
#             pre = i
#         ret = (change_count == 1 and zero_count == one_count)
#         Solution.cache[s] = ret
#         return ret

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return

        ans = 0
        pre_len = 0
        cur_len = 1
        for i in range(1, len(s)):
            if (s[i] == s[i-1]):
                cur_len += 1
            else:
                pre_len = cur_len
                cur_len = 1
            if pre_len >= cur_len:
                ans += 1
        return ans

if __name__ == "__main__":
    s = Solution().countBinarySubstrings("00110011")
    print(s)

