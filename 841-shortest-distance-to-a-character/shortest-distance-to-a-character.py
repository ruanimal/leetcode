# -*- coding:utf-8 -*-


# English:
# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
# Example 1:
# Input: S = "loveleetcode", C = 'e' Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# Note:
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
#
# 中文:
# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
# 示例 1:
# 输入: S = "loveleetcode", C = 'e' 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 说明:
# 字符串 S 的长度范围为 [1, 10000]。
# C 是一个单字符，且保证是字符串 S 里的字符。
# S 和 C 中的所有字母均为小写字母。


#
# @lc app=leetcode.cn id=821 lang=python
#
# [821] 打砖块
#
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        不能用动态规划， 因为不满足后无效性
        """
        e_indexs = [idx for idx, i in enumerate(S) if i==C]
        # e_indexs.sort()
        ret = []
        for idx, i in enumerate(S):
            # 可用二分查找求最近的e
            ret.append(min(abs(idx-j) for j in e_indexs))
        return ret

if __name__ == "__main__":
    s = Solution().shortestToChar(S = "loveleetcode", C = 'e')
    print(s)


