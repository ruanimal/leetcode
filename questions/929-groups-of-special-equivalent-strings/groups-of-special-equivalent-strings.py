# -*- coding:utf-8 -*-

# <SUBID:18236455,UPDATE:20220325>
# English:
# You are given an array of strings of the same length words.
# In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].
# Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == words[j].
# For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
# A group of special-equivalent strings from words is a non-empty subset of words such that:
# Every pair of strings in the group are special equivalent, and
# The group is the largest size possible (i.e., there is not a string words[i] not in the group such that words[i] is special-equivalent to every string in the group).
# Return the number of groups of special-equivalent strings from words.
# Example 1:
# Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"] Output: 3 Explanation: One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings is all pairwise special equivalent to these. The other two groups are ["xyzz", "zzxy"] and ["zzyx"]. Note that in particular, "zzxy" is not special equivalent to "zzyx".
# Example 2:
# Input: words = ["abc","acb","bac","bca","cab","cba"] Output: 3
# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 20
# words[i] consist of lowercase English letters.
# All the strings are of the same length.
#
# 中文:
# 给你一个字符串数组 words。
# 一步操作中，你可以交换字符串 words[i] 的任意两个偶数下标对应的字符或任意两个奇数下标对应的字符。
# 对两个字符串 words[i] 和 words[j] 而言，如果经过任意次数的操作，words[i] == words[j] ，那么这两个字符串是 特殊等价 的。
# 例如，words[i] = "zzxy" 和 words[j] = "xyzz" 是一对 特殊等价 字符串，因为可以按 "zzxy" -> "xzzy" -> "xyzz" 的操作路径使 words[i] == words[j] 。
# 现在规定，words 的 一组特殊等价字符串 就是 words 的一个同时满足下述条件的非空子集：
# 该组中的每一对字符串都是 特殊等价 的
# 该组字符串已经涵盖了该类别中的所有特殊等价字符串，容量达到理论上的最大值（也就是说，如果一个字符串不在该组中，那么这个字符串就 不会 与该组内任何字符串特殊等价）
# 返回 words 中 特殊等价字符串组 的数量。
# 示例 1：
# 输入：words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"] 输出：3 解释： 其中一组为 ["abcd", "cdab", "cbad"]，因为它们是成对的特殊等价字符串，且没有其他字符串与这些字符串特殊等价。 另外两组分别是 ["xyzz", "zzxy"] 和 ["zzyx"]。特别需要注意的是，"zzxy" 不与 "zzyx" 特殊等价。
# 示例 2：
# 输入：words = ["abc","acb","bac","bca","cab","cba"] 输出：3 解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
# 提示：
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 20
# 所有 words[i] 都只由小写字母组成。
# 所有 words[i] 都具有相同的长度。


#
# @lc app=leetcode.cn id=893 lang=python
#
# [893] 特殊等价字符串组
#
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = set()
        for i in A:
            i_even = sorted(i[::2])
            i_odd = sorted(i[1:][::2])
            new_i = ''.join(i_even+i_odd)
            if new_i not in ans:
                ans.add(new_i)
        return len(ans)

if __name__ == "__main__":
    s = Solution().numSpecialEquivGroups(["abcd","cdab","adcb","cbad"])
    print(s)

