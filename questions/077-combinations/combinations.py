# -*- coding:utf-8 -*-

# <SUBID:308623014,UPDATE:20230205>
# English:
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
# Example 1:
# Input: n = 4, k = 2 Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]] Explanation: There are 4 choose 2 = 6 total combinations. Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:
# Input: n = 1, k = 1 Output: [[1]] Explanation: There is 1 choose 1 = 1 total combination.
# Constraints:
# 1 <= n <= 20
# 1 <= k <= n
#
# 中文:
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
# 示例 1：
# 输入：n = 4, k = 2 输出： [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
# 示例 2：
# 输入：n = 1, k = 1 输出：[[1]]
# 提示：
# 1 <= n <= 20
# 1 <= k <= n




class SolutionV1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def backtrack(start, k, res, path):
            if k == 0:
                res.append(path[:])
                return
            for i in range(start, n+1):
                # 组合的话, 为了防止重复, 已遍历的数字不要重新遍历
                if (not path or path[-1] < i):
                    path.append(i)
                    backtrack(start+1, k-1, res, path)
                    path.pop()

        if (n < k) or n == 0 or k == 0:
            return []
        res = []
        backtrack(1, k, res, [])
        return res


# @lc code=start
class Solution(object):
    def combine(self, n: int, k: int) -> list:
        def backtrack(start, k):
            if k == 0:
                res.append(track[:])
                return
            # 组合的话, 为了防止重复, 已遍历的数字不要重新遍历, 所以从start开始
            for i in range(start, n+1):
                track.append(i)
                backtrack(i+1, k-1)
                track.pop()

        if (n < k) or n == 0 or k == 0:
            return []
        res = []
        track = []
        backtrack(1, k)
        return res

