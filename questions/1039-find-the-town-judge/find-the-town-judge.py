# -*- coding:utf-8 -*-


# English:
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
# Example 1:
# Input: n = 2, trust = [[1,2]] Output: 2
# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]] Output: 3
# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]] Output: -1
# Constraints:
# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n
#
# 中文:
# 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。
# 如果小镇法官真的存在，那么：
# 小镇法官不会信任任何人。
# 每个人（除了小镇法官）都信任这位小镇法官。
# 只有一个人同时满足属性 1 和属性 2 。
# 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
# 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
# 示例 1：
# 输入：n = 2, trust = [[1,2]] 输出：2
# 示例 2：
# 输入：n = 3, trust = [[1,3],[2,3]] 输出：3
# 示例 3：
# 输入：n = 3, trust = [[1,3],[2,3],[3,1]] 输出：-1
# 提示：
# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# trust 中的所有trust[i] = [ai, bi] 互不相同
# ai != bi
# 1 <= ai, bi <= n


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1 and not trust:
            return 1   # 只有一个人，且它是法官
        out_map = {}
        in_map = {}
        for fr, to in trust:
            in_map[to] = in_map.setdefault(to, 0) + 1
            out_map[fr] = out_map.setdefault(fr, 0) + 1

        ret = []
        for k, v in in_map.items():
            if v == N-1 and out_map.get(k, 0) == 0:
                ret.append(k)
        if len(ret) == 1:
            return ret[0]
        return -1
