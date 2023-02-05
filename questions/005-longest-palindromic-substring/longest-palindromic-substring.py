# -*- coding:utf-8 -*-

# <SUBID:301771080,UPDATE:20230205>
# English:
# Given a string s, return the longest palindromic substring in s.
# Example 1:
# Input: s = "babad" Output: "bab" Explanation: "aba" is also a valid answer.
# Example 2:
# Input: s = "cbbd" Output: "bb"
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
# 中文:
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
# 示例 1：
# 输入：s = "babad" 输出："bab" 解释："aba" 同样是符合题意的答案。
# 示例 2：
# 输入：s = "cbbd" 输出："bb"
# 提示：
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成


#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (24.97%)
# Likes:    960
# Dislikes: 0
# Total Accepted:    68.7K
# Total Submissions: 268.9K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # 暴力求解, 太慢 n**2
        # if len(s) <= 1:
        #     return s
        # ans = ''
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         t = s[i:j+1]
        #         if t[::-1] == t and len(t) > len(ans):
        #             ans = t
        # return ans

        # # v2 暴力求解, 剪枝, timeout
        # if len(s) <= 1:
        #     return s
        # ans = ''
        # for i in range(len(s)):
        #     if (len(s) - i + 1) <= len(ans):
        #         break
        #     for j in range(len(s)-1, i-1, -1):
        #         t = s[i:j+1]
        #         if len(t) <= len(ans):
        #             break
        #         if t[::-1] == t and len(t) > len(ans):
        #             ans = t
        # return ans

        """
        解决这类 “最优子结构” 问题，可以考虑使用 “动态规划”的方法：1、定义 “状态”；2、找到 “状态转移方程”。

        在下面的说明中，s[j, i] 表示原始字符串的一个子串，j、i 分别是索引的边界值，使用左闭、右闭区间表示左右端点可以取到。

        1、定义 “状态”，这里 “状态”数组是二维数组。

        dp[j][i] 表示子串 s[j, i]（包括区间左右端点）是否构成回文串，是一个二维布尔型数组。即如果子串 s[j, i] 是回文串，那么 dp[j][i] = true。

        2、找到 “状态转移方程”。

        首先，我们很清楚一个事实：

        如果 s[j, i] 是一个回文串，例如 “abccba”，那么这个回文串两边各往里面收缩一个字符（如果可以的话）的子串 s[j + 1, i - 1] 也一定是回文串，即：如果 dp[j][i] == true 成立，一定有 dp[j + 1][i - 1] = true 成立。

        反过来，如果已知 dp[j + 1, i - 1] == true 成立，就可以通过比较 s[j] 和 s[i] 进而得到 dp[j, i]。

        注意：

        1、此时我们要保证 [j + 1, i - 1] 能够形成区间，因此有 j + 1 < i - 1，整理得 j - i < -2，或者 i - j > 2。

        2、如果 [j + 1, i - 1] 不能形成区间，即 i - j <= 2 ，只需要判断 s[j] == s[i] 即可，因此考虑“回文串两边各往里面收缩一个字符”的时候，二者之一成立即可。

        于是整理成“状态转移方程”：

        dp[j, i] = (s[j] == s[i] and (i - j <= 2 or dp[j + 1, i - 1]))

        编码实现细节：因为要构成子串 j 一定小于等于 i ，我们只关心 “状态”数组“下三角”的那部分取值。理解上面的“状态转移方程”中的 (j >= i - 2 or dp[j + 1, i - 1]) 这部分是关键。

        这里我要提出一个疑问：为什么在动态规划的算法中，不用考虑回文串长度的奇偶性呢。想一想，答案就在状态转移方程里面。

        动态规划的方法事实上有点像“中心扩散法”的逆过程，想一想是不是这么回事。
        """

        # 动态规划
        if len(s) <= 1:
            return s

        ans = s[0]
        dp = [[0 for _ in s] for _ in s]
        for i in range(len(s)):
            dp[i][i] = 1
            for j in range(i):
                if s[i] == s[j] and (i-j < 2 or dp[j+1][i-1]):
                    dp[j][i] = 1
                    if (i - j + 1) > len(ans):
                        ans = s[j:i+1]
        return ans


if __name__ == "__main__":
    s = Solution().longestPalindrome('babcb')
    print(s)
    s = Solution().longestPalindrome('ba')
    print(s)
    s = Solution().longestPalindrome('ba')
    print(s)


