# -*- coding:utf-8 -*-


# English:
# In a string
# s
# of lowercase letters, these letters form consecutive groups of the same character.
# For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".
# A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].
# A group is considered large if it has 3 or more characters.
# Return the intervals of every large group sorted in increasing order by start index.
# Example 1:
# Input: s = "abbxxxxzzy" Output: [[3,6]] Explanation: "xxxx" is the only large group with start index 3 and end index 6.
# Example 2:
# Input: s = "abc" Output: [] Explanation: We have groups "a", "b", and "c", none of which are large groups.
# Example 3:
# Input: s = "abcdddeeeeaabbbcd" Output: [[3,5],[6,9],[12,14]] Explanation: The large groups are "ddd", "eeee", and "bbb".
# Constraints:
# 1 <= s.length <= 1000
# s contains lowercase English letters only.
#
# 中文:
# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
# 例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。
# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。
# 示例 1：
# 输入：s = "abbxxxxzzy" 输出：[[3,6]] 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
# 示例 2：
# 输入：s = "abc" 输出：[] 解释："a","b" 和 "c" 均不是符合要求的较大分组。
# 示例 3：
# 输入：s = "abcdddeeeeaabbbcd" 输出：[[3,5],[6,9],[12,14]] 解释：较大分组为 "ddd", "eeee" 和 "bbb"
# 示例 4：
# 输入：s = "aba" 输出：[]
# 提示：
# 1 <= s.length <= 1000
# s 仅含小写英文字母


#
# @lc app=leetcode.cn id=830 lang=python
#
# [830] 最大三角形面积
#
# https://leetcode-cn.com/problems/positions-of-large-groups/description/
#
# algorithms
# Easy (40.62%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 9.9K
# Testcase Example:  '"abbxxxxzzy"'
#
# 在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。
#
# 例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
#
# 我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。
#
# 最终结果按照字典顺序输出。
#
# 示例 1:
#
#
# 输入: "abbxxxxzzy"
# 输出: [[3,6]]
# 解释: "xxxx" 是一个起始于 3 且终止于 6 的较大分组。
#
#
# 示例 2:
#
#
# 输入: "abc"
# 输出: []
# 解释: "a","b" 和 "c" 均不是符合要求的较大分组。
#
#
# 示例 3:
#
#
# 输入: "abcdddeeeeaabbbcd"
# 输出: [[3,5],[6,9],[12,14]]
#
# 说明:  1 <= S.length <= 1000
#
#
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ans = []
        pre = 1
        for i in range(1, len(S)):
            if S[i-1] != S[i]:
                if pre >= 3:
                    ans.append([i-pre, i-1])
                pre = 1
            else:
                pre += 1
        if pre >= 3:
            ans.append([len(S)-pre, len(S)-1])
        return ans

if __name__ == "__main__":
    s = Solution().largeGroupPositions('abcdddeeee')
    print(s)


