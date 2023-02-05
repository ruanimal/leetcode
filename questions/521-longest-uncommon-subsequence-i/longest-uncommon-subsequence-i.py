# -*- coding:utf-8 -*-

# <SUBID:317683839,UPDATE:20230205>
# English:
# Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If the longest uncommon subsequence does not exist, return -1.
# An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
# For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "a
# e
# b
# d
# c" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).
# Example 1:
# Input: a = "aba", b = "cdc" Output: 3 Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc". Note that "cdc" is also a longest uncommon subsequence.
# Example 2:
# Input: a = "aaa", b = "bbb" Output: 3 Explanation: The longest uncommon subsequences are "aaa" and "bbb".
# Example 3:
# Input: a = "aaa", b = "aaa" Output: -1 Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a.
# Constraints:
# 1 <= a.length, b.length <= 100
# a and b consist of lower-case English letters.
#
# 中文:
# 给你两个字符串 a 和 b，请返回 这两个字符串中 最长的特殊序列  的长度。如果不存在，则返回 -1 。
# 「最长特殊序列」 定义如下：该序列为 某字符串独有的最长子序列（即不能是其他字符串的子序列） 。
# 字符串 s 的子序列是在从 s 中删除任意数量的字符后可以获得的字符串。
# 例如，"abc" 是 "aebdc" 的子序列，因为删除 "aebdc" 中斜体加粗的字符可以得到 "abc" 。 "aebdc" 的子序列还包括 "aebdc" 、 "aeb" 和 "" (空字符串)。
# 示例 1：
# 输入: a = "aba", b = "cdc" 输出: 3 解释: 最长特殊序列可为 "aba" (或 "cdc")，两者均为自身的子序列且不是对方的子序列。
# 示例 2：
# 输入：a = "aaa", b = "bbb" 输出：3 解释: 最长特殊序列是 "aaa" 和 "bbb" 。
# 示例 3：
# 输入：a = "aaa", b = "aaa" 输出：-1 解释: 字符串 a 的每个子序列也是字符串 b 的每个子序列。同样，字符串 b 的每个子序列也是字符串 a 的子序列。
# 提示：
# 1 <= a.length, b.length <= 100
# a 和 b 由小写英文字母组成


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b :
            return -1
        return max(len(a),len(b))

