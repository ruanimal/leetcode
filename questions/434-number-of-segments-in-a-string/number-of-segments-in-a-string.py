# -*- coding:utf-8 -*-

# <SUBID:21033524,UPDATE:20230205>
# English:
# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
# Example 1:
# Input: s = "Hello, my name is John" Output: 5 Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:
# Input: s = "Hello" Output: 1
# Constraints:
# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.
#
# 中文:
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
# 示例:
# 输入: "Hello, my name is John" 输出: 5 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。


#
# @lc app=leetcode.cn id=434 lang=python
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (30.12%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 19.5K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# 示例:
#
# 输入: "Hello, my name is John"
# 输出: 5
#
#
#
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        in_word = False
        ans = 0
        for i in s:
            if in_word:
                if i != ' ':
                    continue
                else:
                    in_word = False
            else:
                if i != ' ':
                    ans += 1
                    in_word = True
                else:
                    continue
        return ans

if __name__ == "__main__":
    s = Solution().countSegments("love live! mu\'sic forever")
    print(s)
    s = Solution().countSegments( "H")
    print(s)
    s = Solution().countSegments( "")
    print(s)


