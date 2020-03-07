# -*- coding:utf-8 -*-


# English:
# You are given an array A of strings.
# A move onto S consists of swapping any two even indexed characters of S, or any two odd indexed characters of S.
# Two strings S and T are special-equivalent if after any number of moves onto S, S == T.
# For example, S = "zzxy" and T = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz" that swap S[0] and S[2], then S[1] and S[3].
# Now, a group of special-equivalent strings from A is a non-empty subset of A such that:
# Every pair of strings in the group are special equivalent, and;
# The group is the largest size possible (ie., there isn't a string S not in the group such that S is special equivalent to every string in the group)
# Return the number of groups of special-equivalent strings from A.
# Example 1:
# Input: ["abcd","cdab","cbad","xyzz","zzxy","zzyx"] Output: 3 Explanation: One group is ["abcd", "cdab", "cbad"], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these. The other two groups are ["xyzz", "zzxy"] and ["zzyx"]. Note that in particular, "zzxy" is not special equivalent to "zzyx".
# Example 2:
# Input: ["abc","acb","bac","bca","cab","cba"] Output: 3
# Note:
# 1 <= A.length <= 1000
# 1 <= A[i].length <= 20
# All A[i] have the same length.
# All A[i] consist of only lowercase letters.
#
# 中文:
# 你将得到一个字符串数组 A。
# 如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是特殊等价的。
# 一次移动包括选择两个索引 i 和 j，且 i ％ 2 == j ％ 2，交换 S[j] 和 S [i]。
# 现在规定，A 中的特殊等价字符串组是 A 的非空子集 S，这样不在 S 中的任何字符串与 S 中的任何字符串都不是特殊等价的。
# 返回 A 中特殊等价字符串组的数量。
# 示例 1：
# 输入：["a","b","c","a","c","c"] 输出：3 解释：3 组 ["a","a"]，["b"]，["c","c","c"]
# 示例 2：
# 输入：["aa","bb","ab","ba"] 输出：4 解释：4 组 ["aa"]，["bb"]，["ab"]，["ba"]
# 示例 3：
# 输入：["abc","acb","bac","bca","cab","cba"] 输出：3 解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
# 示例 4：
# 输入：["abcd","cdab","adcb","cbad"] 输出：1 解释：1 组 ["abcd","cdab","adcb","cbad"]
# 提示：
# 1 <= A.length <= 1000
# 1 <= A[i].length <= 20
# 所有 A[i] 都具有相同的长度。
# 所有 A[i] 都只由小写字母组成。


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

