# -*- coding:utf-8 -*-

# <SUBID:319522495,UPDATE:20230205>
# English:
# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
# Example 1:
# Input: s = "loveleetcode", c = "e" Output: [3,2,1,0,1,0,0,1,2,2,1,0] Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed). The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3. The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2. For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1. The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
# Example 2:
# Input: s = "aaab", c = "b" Output: [3,2,1,0]
# Constraints:
# 1 <= s.length <= 104
# s[i] and c are lowercase English letters.
# It is guaranteed that c occurs at least once in s.
#
# 中文:
# 给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。
# 返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。
# 两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。
# 示例 1：
# 输入：s = "loveleetcode", c = "e" 输出：[3,2,1,0,1,0,0,1,2,2,1,0] 解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。 距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。 距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。 对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。 距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。
# 示例 2：
# 输入：s = "aaab", c = "b" 输出：[3,2,1,0]
# 提示：
# 1 <= s.length <= 104
# s[i] 和 c 均为小写英文字母
# 题目数据保证 c 在 s 中至少出现一次


class SolutionA:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """暴力法
        不能用动态规划， 因为不满足后无效性
        """
        e_indexs = [idx for idx, i in enumerate(s) if i==c]
        ret = []
        for idx, i in enumerate(s):
            # 可用二分查找求最近的e
            ret.append(min(abs(idx-j) for j in e_indexs))
        return ret


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """两次遍历
        左侧距离和右侧距离
        """

        MAX = 10001
        ans = []
        index = -1
        for i in range(len(s)):
            if s[i] == c:
                index = i
                ans.append(0)
            elif index != -1:
                ans.append(i-index)
            else:
                ans.append(MAX)

        index = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                index = i
                ans[i] = 0
            elif index != -1:
                ans[i] = min(ans[i], index-i)
            else:
                ans[i] = ans[i]
        return ans
